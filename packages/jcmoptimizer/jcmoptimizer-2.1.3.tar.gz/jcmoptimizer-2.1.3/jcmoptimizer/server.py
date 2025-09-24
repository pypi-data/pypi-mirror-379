from typing import Any, Optional, Callable
from io import BufferedRandom
import os
import sys
import json
import tempfile
import time
import subprocess

from .client import Client

def _server_response(
    log_file: BufferedRandom, error_file: BufferedRandom, max_lines: int = 10
) -> str:
    """Get stdout and stderr from server"""
    log_file.seek(0)
    error_file.seek(0)
    log = [line.decode("charmap") for line in log_file.readlines()]
    errs = [line.decode("charmap") for line in error_file.readlines()]
    return "".join(log[-max_lines:]) + " " + "".join(errs[-max_lines:])


class TimeoutError(Exception):
    pass


class Popen(subprocess.Popen):
    def __del__(self, _maxsize: Any = sys.maxsize, _warn: Any = None) -> None:
        # capture ResourceWarning: subprocess XXX is still running
        def warn(*args: Any, **kwargs: Any) -> None:
            pass

        super().__del__(_maxsize, _warn=warn)


class Server:

    """This class provides methods for starting and stopping a self-hosted
    optimization server on the local computer. Example::

       server = Server()
       client = Client(host=server.host)
       study = client.create_study(...)

    Args:
      jcm_optimizer_path: The path of the JCMoptimizer installation.
      port: The port that the optimization server is listening to.
         If not specified, the port is chosen automatically.
      persistent: If true, the server continues to run even after
         the Python script has finished. To shutdown a local server
         later on, one can reconnect to it::

            client = Client(host="http://localhost:4554")
            client.shutdown_server()
      timeout: The maximum amount of time to wait for the server startup.
      max_retries: The maximum number of attempts to start the server
         after a timeout.

    """

    def __init__(
        self,
        jcm_optimizer_path: Optional[str] = None,
        port: Optional[int] = None,
        persistent: bool = False,
        timeout: float = 40.0,
        max_retries: int = 1,
    ) -> None:
        for trial in range(1 + max_retries):
            try:
                self._start_server(
                    jcm_optimizer_path=jcm_optimizer_path,
                    port=port,
                    persistent=persistent,
                    timeout=timeout,
                )
                break
            except TimeoutError as err:
                if trial == max_retries:
                    raise EnvironmentError(
                        f"Could not start optimization server after {timeout:.0f}s "
                        f"for {1 + max_retries} attempts. "
                        f"{'Server response: ' + str(err) if str(err) else ''}"
                    ) from err

    def _start_server(
        self,
        jcm_optimizer_path: Optional[str],
        port: Optional[int],
        persistent: bool,
        timeout: float,
    ) -> None:
        if jcm_optimizer_path is None:
            jcm_optimizer_path = os.path.abspath(
                os.path.join(os.path.dirname(__file__), "..", "..", "..")
            )

        jcm_optimizer_path = os.path.abspath(os.path.expanduser(jcm_optimizer_path))
        if "WIN" in sys.platform.upper():
            JCMoptimizer = os.path.join(
                jcm_optimizer_path, "server", "JCMoptimizer.exe"
            )
        else:
            JCMoptimizer = os.path.join(
                jcm_optimizer_path, "server", "bin", "JCMoptimizer.bin"
            )

        if not os.path.exists(JCMoptimizer):
            raise ValueError(
                f"The path '{jcm_optimizer_path}' does not contain a valid "
                "JCMoptimizer installation."
            )

        # get clean environment
        env = os.environ.copy()
        env.pop("PYTHONDEVMODE", None)

        # Start JCMoptimizer
        cmd: list[str] = [f'"{JCMoptimizer}"']
        if port is not None:
            cmd.append(f"--port {port}")
        cmd.append("--print_json")
        if not persistent:
            cmd.append(f"--calling_pid {os.getpid()}")
        close_fds = os.name != "nt"

        # Generate temporary files for errors and log
        with (
            tempfile.TemporaryFile() as error_file,
            tempfile.TemporaryFile() as log_file,
        ):
            Popen(
                " ".join(cmd),
                shell=True,
                stdout=log_file,
                stderr=error_file,
                close_fds=close_fds,
                universal_newlines=True,
                bufsize=1,
                start_new_session=True,
                env=env,
            )

            # Poll process for new output until first line with port information
            line = b""
            for _ in range(round(10 * timeout)):
                error_file.seek(0)
                if len(error_file.readlines()):
                    response = _server_response(log_file, error_file)
                    raise EnvironmentError(
                        "Could not start optimization server. "
                        f"Server response: \n{response}"
                    )

                log_file.seek(0)
                for line in iter(log_file.readline, b""):
                    if line[:17] == b'{"optimizer_port"':
                        break
                else:
                    time.sleep(0.1)
                    continue
                break
            else:
                response = _server_response(log_file, error_file)
                raise TimeoutError(response)
            try:
                info = json.loads(line)
            except Exception as err:
                response = _server_response(log_file, error_file)
                raise EnvironmentError(
                    "Could not start optimization server. "
                    f"Server response: \n{response}"
                ) from err

        self._port = int(info["optimizer_port"])
        self._pid = int(info["pid"])

    @property
    def port(self) -> int:
        """The port that the server is listening on"""
        return self._port

    @property
    def host(self) -> str:
        """The host name of the server"""
        return f"http://localhost:{self._port}"

    @property
    def pid(self) -> int:
        """The process id of the server."""
        return self._pid

    def shutdown(self, force: bool = False) -> None:
        """Shuts down the optimization server.

        Args:
          force: If true, the optimization server is closed even if a study
            is not yet finished.
        """
        Client(self.host).shutdown_server(force)
