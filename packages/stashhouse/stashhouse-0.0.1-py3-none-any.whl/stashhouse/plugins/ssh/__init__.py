import asyncio
import functools
import logging
import multiprocessing
import os
import uuid
from typing import Awaitable

import asyncssh

from ... import server


logger = logging.getLogger(__name__)


class _SCPServer(asyncssh.SSHServer):
    def connection_made(self, conn) -> None:
        remote_host, remote_port = conn.get_extra_info("peername")
        logger.info(f"Connection received from {remote_host!s}:{remote_port!s}")

    # noinspection PyUnusedLocal
    def begin_auth(self, username) -> bool:
        del username
        return False


class _SFTPServer(asyncssh.SFTPServer):
    def __init__(self, chan, directory: str):
        self.directory = os.path.join(directory, str(uuid.uuid4()))
        super().__init__(chan, chroot=self.directory.encode())

    async def open(self, path, pflags, attrs) -> object | Awaitable[object]:
        writing = (
            (pflags & os.O_WRONLY) or (pflags & os.O_RDWR) or (pflags & os.O_APPEND)
        )
        creating = (pflags & os.O_CREAT) != 0

        if writing or creating:
            mapped_path = self.map_path(path)
            if os.path.exists(mapped_path):
                return super().open(path, pflags, attrs)

            os.makedirs(os.path.dirname(mapped_path), exist_ok=True)

        return super().open(path, pflags, attrs)


class SSHServer:
    def __init__(
        self,
        server_options: server.ServerOptions,
        exited: multiprocessing.Event,
        port: int = 22,
        backlog: int = 32,
    ):
        self.server_options = server_options
        self.backlog = backlog
        self.exited = exited
        self.port = port

        self.host_key = asyncssh.generate_private_key("ssh-rsa")

    async def _run(self) -> None:
        server = await asyncssh.listen(
            self.server_options.host,
            self.port,
            allow_scp=True,
            server_host_keys=[self.host_key],
            server_factory=_SCPServer,
            sftp_factory=functools.partial(
                _SFTPServer, directory=self.server_options.directory
            ),
        )

        while not self.exited.is_set():
            await asyncio.sleep(1.0)

        server.close()
        await server.wait_closed()

    def run(self) -> None:
        asyncio.run(self._run())


__all__ = ("SSHServer",)
