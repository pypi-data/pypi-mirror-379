from typing import Any, Literal, Optional
import threading
from datetime import datetime as dt

template = 'Please install the package {p} (e.g. run "pip install {p}") .'
try:
    import requests
except ImportError:
    raise ImportError(template.format(p="requests"))
try:
    import json
except ImportError:
    raise ImportError(template.format(p="json"))
try:
    import colorama
except ImportError:
    raise ImportError(template.format(p="colorama"))


class ServerError(EnvironmentError):
    pass


class NumParallelError(EnvironmentError):
    pass


class Requestor(object):
    def __init__(
        self,
        host: str,
        session: Optional[requests.Session] = None,
        verbose: bool = True,
    ):
        is_in_notebook = False
        try:
            shell = get_ipython().__class__.__name__  # type: ignore
            is_in_notebook = shell == "ZMQInteractiveShell"
        except NameError:
            pass
        if not is_in_notebook:
            colorama.init()

        if session is None:
            self.session = requests.Session()
        else:
            self.session = session
        self.verbose = verbose
        self.lock = threading.Lock()
        self.host = host

    def print_message(
        self,
        message_str: str,
        message_time: Optional[str] = None,
        message_level: Literal["debug", "info", "warning", "error"] = "info",
    ) -> None:
        if message_time is None:
            message_time = dt.now().strftime("%Y-%m-%d %H:%M:%S")
        DATE = colorama.Style.BRIGHT
        RESET = colorama.Style.RESET_ALL
        if message_level == "error":
            STYLE = colorama.Fore.RED + colorama.Style.BRIGHT
        elif message_level == "warning":
            STYLE = colorama.Fore.YELLOW
        elif message_level == "info":
            STYLE = colorama.Fore.GREEN
        else:
            STYLE = colorama.Style.DIM

        print(DATE + message_time + ": " + RESET + STYLE + message_str + RESET)

    def inform(self, message: str) -> None:
        self.print_message(message_str=message, message_level="info")

    def warn(self, message: str) -> None:
        self.print_message(message_str=message, message_level="warning")

    def _headers(self) -> dict[str, str]:
        return {"_client_token": "selfhosted"}

    def _check_status_code(self, purpose: str, answer: dict[str, Any]) -> None:
        if answer["status_code"] == 500:
            raise ServerError("An internal server error occured. Check the log files.")
        if answer["status_code"] == 400:
            raise ServerError(f"Could not {purpose}. {answer['error']}")
        if answer["status_code"] == 202:
            raise NumParallelError(f"Could not {purpose}. {answer['error']}")
        del answer["status_code"]

    def _print_messages(self, answer: dict[str, Any]) -> None:
        if not self.verbose:
            return
        status_code = answer["status_code"]
        if status_code >= 200 and status_code < 300:
            if "messages" in answer:
                messages = json.loads(answer["messages"])
                for idx in sorted(messages["message"]):
                    message_str = messages["message"][idx]
                    message_level = messages["level"][idx]
                    message_time = messages["datetime"][idx]
                    self.print_message(message_str, message_time, message_level)

    def get(
        self,
        purpose: str,
        object: Optional[str] = None,
        type: Optional[str] = None,
        id: Optional[str] = None,
    ) -> dict[str, Any]:
        url = self.host
        if object is not None:
            url += "/" + object
        if type is not None:
            url += "/" + type
        if id is not None:
            url += "/" + id

        try:
            with self.lock:
                r = self.session.get(url, headers=self._headers())
        except requests.exceptions.ConnectionError:
            raise EnvironmentError(
                "Could not connect to server. "
                f"Please check if the optimization server is running on {self.host}."
            )

        try:
            answer = r.json()
        except Exception as err:
            raise EnvironmentError(
                f"Cannot decode answer: {err} \n {r._content!r}"
            ) from err

        self._print_messages(answer)
        self._check_status_code(purpose, answer)
        return answer

    def post(
        self,
        purpose: str,
        object: str,
        operation: str,
        id: Optional[str] = None,
        data: Optional[dict[str, Any]] = None,
    ) -> dict[str, Any]:
        # make dummy data to ensure this is interpreted as post request by server
        if data is None:
            data = {"0": 0}
        url = self.host + "/" + object + "/" + operation
        if id is not None:
            url += "/" + id
        try:
            with self.lock:
                r = self.session.post(
                    url,
                    data={key: json.dumps(val) for key, val in data.items()},
                    headers=self._headers(),
                )

        except requests.exceptions.ConnectionError:
            raise EnvironmentError(
                "Could not connect to server. Please check "
                f"if the optimization server is running on {self.host}."
            )

        try:
            answer = r.json()
        except Exception as err:
            raise EnvironmentError(
                f"Cannot decode answer: {err} \n {r._content!r}"
            ) from err

        self._print_messages(answer)
        self._check_status_code(purpose, answer)

        return answer
