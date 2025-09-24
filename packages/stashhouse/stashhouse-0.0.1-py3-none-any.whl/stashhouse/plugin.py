import multiprocessing
from importlib.metadata import entry_points
from typing import (
    Protocol,
    runtime_checkable,
    TypedDict,
    NotRequired,
    Unpack,
    TYPE_CHECKING, Generator,
)

if TYPE_CHECKING:
    from . import server
    # noinspection PyUnresolvedReferences
    from importlib.metadata import EntryPoint


class PluginOptions(TypedDict, total=False):
    enable: NotRequired[bool]


@runtime_checkable
class Plugin(Protocol):

    # noinspection PyUnusedLocal
    def __init__(
        self,
        server_options: "server.ServerOptions",
        exited: multiprocessing.Event,
        **kwargs: Unpack[PluginOptions]
    ) -> None:
        self.server_options = server_options
        self.exited = exited
        ...

    def run(self) -> None: ...


def find_server_plugins() -> Generator["EntryPoint", None, None]:
    yield from entry_points(group="stashhouse.plugins.server")


def _run_server_plugin(plugin: "EntryPoint", *args, **kwargs) -> None:
    plugin_instance: Plugin = plugin.load()(*args, **kwargs)
    plugin_instance.run()


def run_server_plugin(*args, **kwargs) -> multiprocessing.Process:
    return multiprocessing.Process(target=_run_server_plugin, args=args, kwargs=kwargs)


__all__ = ("PluginOptions", "Plugin", "find_server_plugins", "run_server_plugin")
