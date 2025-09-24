import contextlib
import logging
import multiprocessing
import pathlib
from typing import Self, Any, NamedTuple

from . import plugin

logger = logging.getLogger(__name__)


class ServerOptions(NamedTuple):
    host: str = "127.0.0.1"
    directory: pathlib.Path = pathlib.Path("data")


class Server:

    def __init__(self, options: ServerOptions | None = None, **plugin_options):
        self.options = options
        if self.options is None:
            self.options = ServerOptions()

        self.exited = multiprocessing.Event()
        self.plugin_options = plugin_options
        self._plugins: contextlib.ExitStack = contextlib.ExitStack()
        self._processes: list[multiprocessing.Process] = []

    def _load_plugin(self, plugin_entry) -> None:
        plugin_options: plugin.PluginOptions | dict[str, Any] = self.plugin_options.get(
            plugin_entry.name, {}
        )

        plugin_enabled: bool = plugin_options.get("enable", True)
        if not plugin_enabled:
            logger.info("Plugin disabled: %s", plugin_entry.name)
            return

        logger.info("Loading plugin: %s", plugin_entry.name)
        plugin_process: multiprocessing.Process = plugin.run_server_plugin(
            plugin_entry, self.options, self.exited, **plugin_options
        )
        plugin_process.start()
        self._processes.append(plugin_process)
        self._plugins.callback(plugin_process.join)

    def start(self) -> None:
        try:
            for plugin_entry in plugin.find_server_plugins():
                self._load_plugin(plugin_entry)
        except:
            self.stop()
            raise

    def stop(self) -> None:
        self.exited.set()
        self._plugins.close()

    def join(self, timeout: float | None = None) -> None:
        for process in self._processes:
            process.join(timeout)

    def __enter__(self) -> Self:
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.stop()


__all__ = ("Server", "ServerOptions")
