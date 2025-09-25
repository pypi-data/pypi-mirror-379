"""
Server execution through the command-line.

Accepts arguments from the command-line and start the server.
"""

import argparse
import pathlib
from typing import TYPE_CHECKING, Sequence

from . import server, plugin

if TYPE_CHECKING:
    # noinspection PyProtectedMember
    from importlib.metadata import EntryPoint


def _parser(**kwargs) -> argparse.ArgumentParser:
    """
    Creates an argument parser.

    The argument parser will always consist of server options and
    may include additional options derived from installed plugins.

    Args:
        **kwargs: Keyword arguments to pass for parser initialization.

    Returns:
        An argument parser instance.
    """

    parser = argparse.ArgumentParser(**kwargs)
    parser.add_argument(
        "--host", "-H", default="127.0.0.1", help="Address to listen on"
    )
    parser.add_argument(
        "--directory",
        "-d",
        default="data",
        type=pathlib.Path,
        help="Directory to store data in",
    )

    register_plugin: "EntryPoint"
    for register_plugin in plugin.find_cli_register_plugins():
        registrar: plugin.PluginArgumentRegistrar = register_plugin.load()
        registrar(register_plugin.name, parser)

    return parser


def _parse_arguments(
    args: Sequence[str] | None = None, namespace: argparse.Namespace = None, **kwargs
) -> tuple[server.ServerOptions, dict[str, plugin.PluginOptions]]:
    """
    Parse arguments while leveraging installed plugins.

    Args:
        args: Sequence of arguments to parse.
        namespace: Namespace of options.
        **kwargs: Keyword arguments to pass for parser initialization.

    Returns:
        A tuple of server options and a dictionary of plugin options.
        The plugin options dictionary consists of string dictionary keys
        representing plugin names and dictionary (str -> Any) values.
    """

    parser: argparse.ArgumentParser = _parser(**kwargs)
    args: argparse.Namespace = parser.parse_args(args, namespace)

    # Extract our server options
    server_options: server.ServerOptions = server.ServerOptions(
        host=args.host, directory=args.directory
    )

    plugin_options: dict[str, plugin.PluginOptions] = {}
    parser_plugin: "EntryPoint"
    for parser_plugin in plugin.find_cli_parse_plugins():
        parser: plugin.PluginArgumentParser = parser_plugin.load()
        plugin_options[parser_plugin.name] = parser(parser_plugin.name, args)

    return server_options, plugin_options


def main(
    args: Sequence[str] | None = None, namespace: argparse.Namespace = None, **kwargs
) -> None:
    """
    Parse arguments and start the server accordingly.

    Args:
        args: Sequence of arguments to parse.
        namespace: Namespace of options.
        **kwargs: Keyword arguments to pass for parser initialization.
    """

    options, plugin_options = _parse_arguments(args, namespace, **kwargs)
    with server.Server(options, **plugin_options) as stashhouse:
        try:
            stashhouse.join()
        except KeyboardInterrupt:
            stashhouse.stop()
            stashhouse.join()


__all__ = ("main",)
