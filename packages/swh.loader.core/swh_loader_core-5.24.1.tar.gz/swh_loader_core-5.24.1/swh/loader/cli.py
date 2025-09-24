# Copyright (C) 2019-2023 The Software Heritage developers
# See the AUTHORS file at the top-level directory of this distribution
# License: GNU General Public License version 3, or any later version
# See top-level LICENSE file for more information

from importlib.metadata import entry_points

# WARNING: do not import unnecessary things here to keep cli startup time under
# control
import logging
from typing import Any

import click

from swh.core.cli import CONTEXT_SETTINGS
from swh.core.cli import swh as swh_cli_group

logger = logging.getLogger(__name__)


LOADERS = {
    entry_point.name.split(".", 1)[1]: entry_point
    for entry_point in entry_points(group="swh.workers")
    if entry_point.name.split(".", 1)[0] == "loader"
}

SUPPORTED_LOADERS = sorted(list(LOADERS))


def get_loader(name: str, **kwargs) -> Any:
    """Given a loader name, instantiate it.

    Args:
        name: Loader's name
        kwargs: Configuration dict (url...)

    Returns:
        An instantiated loader

    """
    if name not in LOADERS:
        raise ValueError(
            "Invalid loader %s: only supported loaders are %s"
            % (name, SUPPORTED_LOADERS)
        )

    registry_entry = LOADERS[name].load()()
    logger.debug(f"registry: {registry_entry}")
    loader_cls = registry_entry["loader"]
    logger.debug(f"loader class: {loader_cls}")
    return loader_cls.from_config(**kwargs)


@swh_cli_group.group(name="loader", context_settings=CONTEXT_SETTINGS)
@click.option(
    "--config-file",
    "-C",
    default=None,
    type=click.Path(
        exists=True,
        dir_okay=False,
    ),
    help="Configuration file.",
)
@click.pass_context
def loader(ctx, config_file):
    """Loader cli tools"""
    from os import environ

    from swh.core.config import read

    ctx.ensure_object(dict)
    logger.debug("ctx: %s", ctx)

    if not config_file:
        config_file = environ.get("SWH_CONFIG_FILENAME")

    ctx.obj["config"] = read(config_file)
    logger.debug("config_file: %s", config_file)
    logger.debug("config: %s", ctx.obj["config"])


@loader.command(name="run", context_settings=CONTEXT_SETTINGS)
@click.argument("type", type=click.Choice(SUPPORTED_LOADERS))
@click.argument("url")
@click.argument("options", nargs=-1)
@click.pass_context
def run(ctx, type, url, options):
    """Ingest with loader <type> the origin located at <url>

    Expected configuration:

    \b
    * :ref:`cli-config-storage`
    * :ref:`cli-config-metadata_fetcher_credentials`

    """
    import iso8601

    from swh.scheduler.cli.utils import parse_options

    conf = ctx.obj.get("config", {})
    if "storage" not in conf:
        logger.warning(
            "No storage configuration detected, using an in-memory storage instead."
        )
        conf["storage"] = {"cls": "memory"}

    (_, kw) = parse_options(options)
    logger.debug(f"kw: {kw}")
    visit_date = kw.get("visit_date")
    if visit_date and isinstance(visit_date, str):
        visit_date = iso8601.parse_date(visit_date)
        kw["visit_date"] = visit_date

    loader = get_loader(
        type,
        url=url,
        storage=conf["storage"],
        metadata_fetcher_credentials=conf.get("metadata_fetcher_credentials"),
        **kw,
    )
    result = loader.load()

    visit_status = loader.storage.origin_visit_status_get_latest(
        url, loader.visit.visit
    )
    msg = f"{result} for origin '{url}'"
    directory = kw.get("directory")
    if directory:
        msg = msg + f" and directory '{directory}'"
    click.echo(msg)
    ctx.exit(code=0 if (visit_status and visit_status.status == "full") else 1)


@loader.command(name="list", context_settings=CONTEXT_SETTINGS)
@click.argument("type", default="all", type=click.Choice(["all"] + SUPPORTED_LOADERS))
@click.pass_context
def list(ctx, type):
    """List supported loaders and optionally their arguments"""
    import inspect

    if type == "all":
        loaders = ", ".join(SUPPORTED_LOADERS)
        click.echo(f"Supported loaders: {loaders}")
    else:
        registry_entry = LOADERS[type].load()()
        loader_cls = registry_entry["loader"]
        doc = inspect.getdoc(loader_cls).strip()

        # Hack to get the signature of the class even though it subclasses
        # Generic, which reimplements __new__.
        # See <https://bugs.python.org/issue40897>
        signature = inspect.signature(loader_cls.__init__)
        signature_str = str(signature).replace("self, ", "")

        click.echo(f"Loader: {doc}\nsignature: {signature_str}")
