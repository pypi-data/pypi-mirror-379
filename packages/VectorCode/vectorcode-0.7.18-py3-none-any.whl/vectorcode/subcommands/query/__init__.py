import json
import logging
import os
from typing import Any, cast

from chromadb import Where
from chromadb.api.models.AsyncCollection import AsyncCollection
from chromadb.api.types import IncludeEnum, QueryResult
from chromadb.errors import InvalidCollectionException, InvalidDimensionException
from tree_sitter import Point

from vectorcode.chunking import Chunk, StringChunker
from vectorcode.cli_utils import (
    Config,
    QueryInclude,
    cleanup_path,
    expand_globs,
    expand_path,
)
from vectorcode.common import (
    ClientManager,
    get_collection,
    get_embedding_function,
    verify_ef,
)
from vectorcode.subcommands.query import types as vectorcode_types
from vectorcode.subcommands.query.reranker import (
    RerankerError,
    get_reranker,
)

logger = logging.getLogger(name=__name__)


def convert_query_results(
    chroma_result: QueryResult, queries: list[str]
) -> list[vectorcode_types.QueryResult]:
    """Convert chromadb query result to in-house query results"""
    assert chroma_result["documents"] is not None
    assert chroma_result["distances"] is not None
    assert chroma_result["metadatas"] is not None
    assert chroma_result["ids"] is not None

    chroma_results_list: list[vectorcode_types.QueryResult] = []
    for q_i in range(len(queries)):
        q = queries[q_i]
        documents = chroma_result["documents"][q_i]
        distances = chroma_result["distances"][q_i]
        metadatas = chroma_result["metadatas"][q_i]
        ids = chroma_result["ids"][q_i]
        for doc, dist, meta, _id in zip(documents, distances, metadatas, ids):
            chunk = Chunk(text=doc, id=_id)
            if meta.get("start"):
                chunk.start = Point(int(meta.get("start", 0)), 0)
            if meta.get("end"):
                chunk.end = Point(int(meta.get("end", 0)), 0)
            if meta.get("path"):
                chunk.path = str(meta["path"])
            chroma_results_list.append(
                vectorcode_types.QueryResult(
                    chunk=chunk,
                    path=str(meta.get("path", "")),
                    query=(q,),
                    scores=(-dist,),
                )
            )
    return chroma_results_list


async def get_query_result_files(
    collection: AsyncCollection, configs: Config
) -> list[str | Chunk]:
    query_chunks = []
    assert configs.query, "Query messages cannot be empty."
    chunker = StringChunker(configs)
    for q in configs.query:
        query_chunks.extend(str(i) for i in chunker.chunk(q))

    configs.query_exclude = [
        expand_path(i, True)
        for i in await expand_globs(configs.query_exclude)
        if os.path.isfile(i)
    ]
    if (await collection.count()) == 0:
        logger.error("Empty collection!")
        return []
    try:
        if len(configs.query_exclude):
            logger.info(f"Excluding {len(configs.query_exclude)} files from the query.")
            filter: dict[str, Any] = {"path": {"$nin": configs.query_exclude}}
        else:
            filter = {}
        num_query = configs.n_result
        if QueryInclude.chunk in configs.include:
            if filter:
                filter = {"$and": [filter.copy(), {"start": {"$gte": 0}}]}
            else:
                filter["start"] = {"$gte": 0}
        else:
            num_query = await collection.count()
            if configs.query_multiplier > 0:
                num_query = min(
                    int(configs.n_result * configs.query_multiplier),
                    await collection.count(),
                )
                logger.info(f"Querying {num_query} chunks for reranking.")
        query_embeddings = get_embedding_function(configs)(query_chunks)
        if isinstance(configs.embedding_dims, int) and configs.embedding_dims > 0:
            query_embeddings = [e[: configs.embedding_dims] for e in query_embeddings]
        chroma_query_results: QueryResult = await collection.query(
            query_embeddings=query_embeddings,
            n_results=num_query,
            include=[
                IncludeEnum.metadatas,
                IncludeEnum.distances,
                IncludeEnum.documents,
            ],
            where=cast(Where, filter) or None,
        )
    except IndexError:
        # no results found
        return []

    reranker = get_reranker(configs)
    converted_results = convert_query_results(chroma_query_results, configs.query)
    return await reranker.rerank(converted_results)


async def build_query_results(
    collection: AsyncCollection, configs: Config
) -> list[dict[str, str | int]]:
    assert configs.project_root

    def make_output_path(path: str, absolute: bool) -> str:
        if absolute:
            if os.path.isabs(path):
                return path
            return os.path.abspath(os.path.join(str(configs.project_root), path))
        else:
            rel_path = os.path.relpath(path, configs.project_root)
            if isinstance(rel_path, bytes):  # pragma: nocover
                # for some reasons, some python versions report that `os.path.relpath` returns a string.
                rel_path = rel_path.decode()
            return rel_path

    structured_result = []
    for res in await get_query_result_files(collection, configs):
        if isinstance(res, str):
            output_path = make_output_path(res, configs.use_absolute_path)
            io_path = make_output_path(res, True)
            if not os.path.isfile(io_path):
                logger.warning(f"{io_path} is no longer a valid file.")
                continue
            with open(io_path) as fin:
                structured_result.append({"path": output_path, "document": fin.read()})
        else:
            res = cast(Chunk, res)
            assert res.path, f"{res} has no `path` attribute."
            structured_result.append(
                {
                    "path": make_output_path(res.path, configs.use_absolute_path)
                    if res.path is not None
                    else None,
                    "chunk": res.text,
                    "start_line": res.start.row if res.start is not None else None,
                    "end_line": res.end.row if res.end is not None else None,
                    "chunk_id": res.id,
                }
            )
    for result in structured_result:
        if result.get("path") is not None:
            result["path"] = cleanup_path(result["path"])
    return structured_result


async def query(configs: Config) -> int:
    if (
        QueryInclude.chunk in configs.include
        and QueryInclude.document in configs.include
    ):
        logger.error(
            "Having both chunk and document in the output is not supported!",
        )
        return 1
    async with ClientManager().get_client(configs) as client:
        try:
            collection = await get_collection(client, configs, False)
            if not verify_ef(collection, configs):
                return 1
        except (ValueError, InvalidCollectionException) as e:
            logger.error(
                f"{e.__class__.__name__}: There's no existing collection for {configs.project_root}",
            )
            return 1
        except InvalidDimensionException as e:
            logger.error(
                f"{e.__class__.__name__}: The collection was embedded with a different embedding model.",
            )
            return 1
        except IndexError as e:  # pragma: nocover
            logger.error(
                f"{e.__class__.__name__}: Failed to get the collection. Please check your config."
            )
            return 1

        if not configs.pipe:
            print("Starting querying...")

        if QueryInclude.chunk in configs.include:
            if len((await collection.get(where={"start": {"$gte": 0}}))["ids"]) == 0:
                logger.warning(
                    """
    This collection doesn't contain line range metadata. Falling back to `--include path document`. 
    Please re-vectorise it to use `--include chunk`.""",
                )
                configs.include = [QueryInclude.path, QueryInclude.document]

        try:
            structured_result = await build_query_results(collection, configs)
        except RerankerError as e:  # pragma: nocover
            # error logs should be handled where they're raised
            logger.error(f"{e.__class__.__name__}")
            return 1

        if configs.pipe:
            print(json.dumps(structured_result))
        else:
            for idx, result in enumerate(structured_result):
                for include_item in configs.include:
                    print(f"{include_item.to_header()}{result.get(include_item.value)}")
                if idx != len(structured_result) - 1:
                    print()
        return 0
