import asyncio
import importlib
import logging
from contextlib import contextmanager
from multiprocessing import cpu_count
from time import perf_counter_ns

import click

import wool
from wool._worker_pool import WorkerPool

DEFAULT_PORT = 48800


# public
class WorkerPoolCommand(click.core.Command):
    """
    Custom Click command class for worker pool commands.

    :param default_host: Default host address.
    :param default_port: Default port number.
    :param default_authkey: Default authentication key.
    """

    def __init__(
        self,
        *args,
        default_uri=None,
        **kwargs,
    ):
        params = kwargs.pop("params", [])
        params = [
            click.Option(["--uri", "-u"], type=str, default=default_uri),
            *params,
        ]
        super().__init__(*args, params=params, **kwargs)


@contextmanager
def timer():
    """
    Context manager to measure the execution time of a code block.

    :return: A function to retrieve the elapsed time.
    """
    start = end = perf_counter_ns()
    try:
        yield lambda: end - start
    finally:
        end = perf_counter_ns()


def to_bytes(context: click.Context, parameter: click.Parameter, value: str):
    """
    Convert the given value to bytes.

    :param context: Click context.
    :param parameter: Click parameter.
    :param value: Value to convert.
    :return: The converted value in bytes.
    """
    if value is None:
        return b""
    return value.encode("utf-8")


def assert_nonzero(
    context: click.Context, parameter: click.Parameter, value: int
) -> int:
    """
    Assert that the given value is non-zero.

    :param context: Click context.
    :param parameter: Click parameter.
    :param value: Value to check.
    :return: The original value if it is non-zero.
    """
    del context, parameter  # Unused parameters
    if value is None:
        return value
    assert value >= 0
    return value


def debug(ctx, param, value):
    """
    Enable debugging mode with a specified port.

    :param ctx: The Click context object.
    :param param: The parameter being handled.
    :param value: The port number for the debugger.
    """
    if not value or ctx.resilient_parsing:
        return

    import debugpy

    debugpy.listen(5678)
    click.echo("Waiting for debugger to attach...")
    debugpy.wait_for_client()
    click.echo("Debugger attached")


@click.group()
@click.option(
    "--debug",
    "-d",
    callback=debug,
    expose_value=False,
    help=(
        "Run with debugger listening on the specified port. Execution will "
        "block until the debugger is attached."
    ),
    is_eager=True,
    type=int,
)
@click.option(
    "--verbosity",
    "-v",
    count=True,
    default=3,
    help="Verbosity level for logging.",
    type=int,
)
def cli(verbosity: int):
    """
    CLI command group with options for verbosity, debugging, and version.

    :param verbosity: Verbosity level for logging.
    """
    log_level = {
        4: logging.DEBUG,
        3: logging.INFO,
        2: logging.WARNING,
        1: logging.ERROR,
    }.get(verbosity, logging.INFO)

    logging.getLogger().setLevel(log_level)
    logging.info(f"Set log level to {logging.getLevelName(log_level)}")


@cli.group()
def pool():
    """
    CLI command group for managing worker pools.
    """
    pass


@pool.command(cls=WorkerPoolCommand)
@click.option("--size", "-s", type=int, default=cpu_count(), callback=assert_nonzero)
@click.option(
    "modules",
    "--module",
    "-m",
    multiple=True,
    type=str,
    help=(
        "Python module containing workerpool task definitions to be "
        "executed by this pool."
    ),
)
def start(uri, size, modules):
    """
    Start a worker pool with the specified configuration.

    :param uri: The URI for the worker pool.
    :param size: The number of worker processes in the pool.
    :param modules: Python modules containing task definitions.
    """
    for module in modules:
        importlib.import_module(module)

    async def run_pool():
        async with WorkerPool(size=size):
            try:
                while True:
                    await asyncio.sleep(1)
            except KeyboardInterrupt:
                logging.info("Shutting down worker pool...")

    asyncio.run(run_pool())


@pool.command(cls=WorkerPoolCommand)
@click.option(
    "--wait",
    "-w",
    is_flag=True,
    default=False,
    help="Wait for in-flight tasks to complete before shutting down.",
)
def stop(uri, wait):
    """
    Shut down the worker pool.

    :param uri: The URI of the worker pool.
    :param wait: Whether to wait for in-flight tasks to complete.
    """
    raise NotImplementedError


@cli.command(cls=WorkerPoolCommand)
def ping(uri):
    """
    Ping the worker pool to check connectivity.

    :param uri: The URI of the worker pool.
    """

    async def run():
        if uri:
            async with WorkerPool(uri):
                with timer() as t:
                    for _ in range(1):
                        await _ping()
        else:
            async with WorkerPool(size=1):
                await asyncio.sleep(0)
                with timer() as t:
                    for _ in range(1000):
                        await _ping()
        click.echo(f"Ping: {t() // 1000000} ms")

    asyncio.run(run())


@wool.work
async def _ping(x=False):
    """
    Asynchronous task to log a ping message.

    :return: None
    """
