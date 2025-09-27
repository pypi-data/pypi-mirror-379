import argparse
import asyncio
import logging
import os
import sys
import traceback
from dataclasses import dataclass
from pathlib import Path
from typing import Optional, cast

import shtab
from chromadb.types import Where

from vectorcode.subcommands.vectorise import (
    VectoriseStats,
    chunked_add,
    exclude_paths_by_spec,
    find_exclude_specs,
    remove_orphanes,
)

try:  # pragma: nocover
    from mcp import ErrorData, McpError
    from mcp.server.fastmcp import FastMCP
except ModuleNotFoundError as e:  # pragma: nocover
    print(
        f"{e.__class__.__name__}:MCP Python SDK not installed. Please install it by installing `vectorcode[mcp]` dependency group.",
        file=sys.stderr,
    )
    sys.exit(1)

from vectorcode.cli_utils import (
    Config,
    LockManager,
    cleanup_path,
    config_logging,
    expand_globs,
    expand_path,
    find_project_config_dir,
    get_project_config,
    load_config_file,
)
from vectorcode.common import (
    ClientManager,
    get_collection,
    get_collections,
    list_collection_files,
)
from vectorcode.subcommands.prompt import prompt_by_categories
from vectorcode.subcommands.query import get_query_result_files

logger = logging.getLogger(name=__name__)
locks = LockManager()


@dataclass
class MCPConfig:
    n_results: int = 10
    ls_on_start: bool = False


mcp_config = MCPConfig()


def get_arg_parser():
    parser = argparse.ArgumentParser(prog="vectorcode-mcp-server")
    parser.add_argument(
        "--number",
        "-n",
        type=int,
        default=10,
        help="Default number of files to retrieve.",
    )
    parser.add_argument(
        "--ls-on-start",
        action="store_true",
        default=False,
        help="Whether to include the output of `vectorcode ls` in the tool description.",
    )
    shtab.add_argument_to(
        parser,
        ["-s", "--print-completion"],
        parent=parser,
        help="Print completion script.",
    )
    return parser


default_project_root: Optional[str] = None
default_config: Optional[Config] = None


async def list_collections() -> list[str]:
    names: list[str] = []
    async with ClientManager().get_client(
        await load_config_file(default_project_root)
    ) as client:
        async for col in get_collections(client):
            if col.metadata is not None:
                names.append(cleanup_path(str(col.metadata.get("path"))))
        logger.info("Retrieved the following collections: %s", names)
        return names


async def vectorise_files(paths: list[str], project_root: str) -> dict[str, int]:
    logger.info(
        f"vectorise tool called with the following args: {paths=}, {project_root=}"
    )
    project_root = os.path.expanduser(project_root)
    if not os.path.isdir(project_root):
        logger.error(f"Invalid project root: {project_root}")
        raise McpError(
            ErrorData(code=1, message=f"{project_root} is not a valid path.")
        )
    config = await get_project_config(project_root)
    try:
        async with ClientManager().get_client(config) as client:
            collection = await get_collection(client, config, True)
            if collection is None:  # pragma: nocover
                raise McpError(
                    ErrorData(
                        code=1,
                        message=f"Failed to access the collection at {project_root}. Use `list_collections` tool to get a list of valid paths for this field.",
                    )
                )
            paths = [os.path.expanduser(i) for i in await expand_globs(paths)]
            final_config = await config.merge_from(
                Config(
                    files=[i for i in paths if os.path.isfile(i)],
                    project_root=project_root,
                )
            )
            for ignore_spec in find_exclude_specs(final_config):
                if os.path.isfile(ignore_spec):
                    logger.info(f"Loading ignore specs from {ignore_spec}.")
                    paths = exclude_paths_by_spec((str(i) for i in paths), ignore_spec)

            stats = VectoriseStats()
            collection_lock = asyncio.Lock()
            stats_lock = asyncio.Lock()
            max_batch_size = await client.get_max_batch_size()
            semaphore = asyncio.Semaphore(os.cpu_count() or 1)
            tasks = [
                asyncio.create_task(
                    chunked_add(
                        str(file),
                        collection,
                        collection_lock,
                        stats,
                        stats_lock,
                        final_config,
                        max_batch_size,
                        semaphore,
                    )
                )
                for file in paths
            ]
            for i, task in enumerate(asyncio.as_completed(tasks), start=1):
                await task

            await remove_orphanes(collection, collection_lock, stats, stats_lock)

        return stats.to_dict()
    except Exception as e:  # pragma: nocover
        if isinstance(e, McpError):
            logger.error("Failed to access collection at %s", project_root)
            raise
        else:
            raise McpError(
                ErrorData(
                    code=1,
                    message="\n".join(traceback.format_exception(e)),
                )
            ) from e


async def query_tool(
    n_query: int, query_messages: list[str], project_root: str
) -> list[str]:
    """
    n_query: number of files to retrieve;
    query_messages: keywords to query.
    collection_path: Directory to the repository;
    """
    logger.info(
        f"query tool called with the following args: {n_query=}, {query_messages=}, {project_root=}"
    )
    project_root = os.path.expanduser(project_root)
    if not os.path.isdir(project_root):
        logger.error("Invalid project root: %s", project_root)
        raise McpError(
            ErrorData(
                code=1,
                message="Use `list_collections` tool to get a list of valid paths for this field.",
            )
        )
    config = await get_project_config(project_root)
    try:
        async with ClientManager().get_client(config) as client:
            collection = await get_collection(client, config, False)

            if collection is None:  # pragma: nocover
                raise McpError(
                    ErrorData(
                        code=1,
                        message=f"Failed to access the collection at {project_root}. Use `list_collections` tool to get a list of valid paths for this field.",
                    )
                )
            query_config = await config.merge_from(
                Config(n_result=n_query, query=query_messages)
            )
            logger.info("Built the final config: %s", query_config)
            result_paths = await get_query_result_files(
                collection=collection,
                configs=query_config,
            )
            results: list[str] = []
            for result in result_paths:
                if isinstance(result, str):
                    if os.path.isfile(result):
                        with open(result) as fin:
                            rel_path = os.path.relpath(result, config.project_root)
                            results.append(
                                f"<path>{rel_path}</path>\n<content>{fin.read()}</content>",
                            )
            logger.info("Retrieved the following files: %s", result_paths)
            return results

    except Exception as e:  # pragma: nocover
        if isinstance(e, McpError):
            logger.error("Failed to access collection at %s", project_root)
            raise
        else:
            raise McpError(
                ErrorData(
                    code=1,
                    message="\n".join(traceback.format_exception(e)),
                )
            ) from e


async def ls_files(project_root: str) -> list[str]:
    """
    project_root: Directory to the repository. MUST be from the vectorcode `ls` tool or user input;
    """
    configs = await get_project_config(expand_path(project_root, True))
    async with ClientManager().get_client(configs) as client:
        return await list_collection_files(await get_collection(client, configs, False))


async def rm_files(files: list[str], project_root: str):
    """
    files: list of paths of the files to be removed;
    project_root: Directory to the repository. MUST be from the vectorcode `ls` tool or user input;
    """
    configs = await get_project_config(expand_path(project_root, True))
    async with ClientManager().get_client(configs) as client:
        try:
            collection = await get_collection(client, configs, False)
            files = [str(expand_path(i, True)) for i in files if os.path.isfile(i)]
            if files:
                await collection.delete(where=cast(Where, {"path": {"$in": files}}))
            else:  # pragma: nocover
                logger.warning(f"All paths were invalid: {files}")
        except ValueError:  # pragma: nocover
            logger.warning(f"Failed to find the collection at {configs.project_root}")
            return


async def mcp_server():
    global default_config, default_project_root

    local_config_dir = await find_project_config_dir(".")

    default_instructions = "\n".join(
        "\n".join(i) for i in prompt_by_categories.values()
    )
    if local_config_dir is not None:
        logger.info("Found project config: %s", local_config_dir)
        project_root = str(Path(local_config_dir).parent.resolve())

        default_project_root = project_root
        default_config = await get_project_config(project_root)
        default_config.project_root = project_root
        async with ClientManager().get_client(default_config) as client:
            logger.info("Collection initialised for %s.", project_root)

            if client is None:
                if mcp_config.ls_on_start:  # pragma: nocover
                    logger.warning(
                        "Failed to initialise a chromadb client. Ignoring --ls-on-start flag."
                    )
            else:
                if mcp_config.ls_on_start:
                    logger.info(
                        "Adding available collections to the server instructions."
                    )
                    default_instructions += (
                        "\nYou have access to the following collections:\n"
                    )
                    for name in await list_collections():
                        default_instructions += f"<collection>{name}</collection>"

    mcp = FastMCP("VectorCode", instructions=default_instructions)
    mcp.add_tool(
        fn=list_collections,
        name="ls",
        description="\n".join(
            prompt_by_categories["ls"] + prompt_by_categories["general"]
        ),
    )

    mcp.add_tool(
        fn=query_tool,
        name="query",
        description="\n".join(
            prompt_by_categories["query"] + prompt_by_categories["general"]
        ),
    )

    mcp.add_tool(
        fn=vectorise_files,
        name="vectorise",
        description="\n".join(
            prompt_by_categories["vectorise"] + prompt_by_categories["general"]
        ),
    )

    mcp.add_tool(
        fn=rm_files,
        name="files_rm",
        description="Remove files from VectorCode embedding database.",
    )

    mcp.add_tool(
        fn=ls_files,
        name="files_ls",
        description="List files that have been indexed by VectorCode.",
    )

    return mcp


def parse_cli_args(args: Optional[list[str]] = None) -> MCPConfig:
    parser = get_arg_parser()
    parsed_args = parser.parse_args(args or sys.argv[1:])
    return MCPConfig(n_results=parsed_args.number, ls_on_start=parsed_args.ls_on_start)


async def run_server():  # pragma: nocover
    try:
        mcp = await mcp_server()
        await mcp.run_stdio_async()
    finally:
        await ClientManager().kill_servers()
        return 0


def main():  # pragma: nocover
    global mcp_config
    config_logging("vectorcode-mcp-server", stdio=False)
    mcp_config = parse_cli_args()
    assert mcp_config.n_results > 0 and mcp_config.n_results % 1 == 0, (
        "--number must be used with a positive integer!"
    )
    return asyncio.run(run_server())


if __name__ == "__main__":  # pragma: nocover
    main()
