from . import server


def main() -> None:
    with server.Server() as stashhouse:
        stashhouse.join()


__all__ = ("main",)
