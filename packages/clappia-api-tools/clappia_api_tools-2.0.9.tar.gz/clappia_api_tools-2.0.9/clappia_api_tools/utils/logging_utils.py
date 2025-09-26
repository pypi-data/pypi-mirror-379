import sys
from datetime import datetime
from enum import Enum


class Colors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


class LogLevel(Enum):
    DEBUG = 0
    INFO = 1
    WARNING = 2
    ERROR = 3
    CRITICAL = 4


class Logger:
    def __init__(
        self,
        name: str = "Logger",
        level: LogLevel = LogLevel.INFO,
        timestamp_format: str = "%Y-%m-%d %H:%M:%S",
    ):
        self.name = name
        self.level = level
        self.timestamp_format = timestamp_format

        self.colors = {
            LogLevel.DEBUG: Colors.OKBLUE,
            LogLevel.INFO: Colors.OKGREEN,
            LogLevel.WARNING: Colors.WARNING,
            LogLevel.ERROR: Colors.FAIL,
            LogLevel.CRITICAL: Colors.HEADER,
        }
        self.reset_color = Colors.ENDC

    def _should_log(self, level: LogLevel) -> bool:
        return level.value >= self.level.value

    def _format_message(self, level: LogLevel, message: str) -> str:
        timestamp = datetime.now().strftime(self.timestamp_format)
        return f"[{timestamp}] [{self.name}] [{level.name}] {message}"

    def _log(self, level: LogLevel, message: str) -> None:
        if not self._should_log(level):
            return

        message_str = str(message)
        formatted_message = self._format_message(level, message_str)

        supports_color = hasattr(sys.stdout, "isatty") and sys.stdout.isatty()

        if supports_color:
            color = self.colors.get(level, "")
            colored_message = f"{color}{formatted_message}{self.reset_color}"
        else:
            colored_message = formatted_message

        output_stream = (
            sys.stderr if level.value >= LogLevel.WARNING.value else sys.stdout
        )
        print(colored_message, file=output_stream)

    def debug(self, message: str) -> None:
        self._log(LogLevel.DEBUG, message)

    def info(self, message: str) -> None:
        self._log(LogLevel.INFO, message)

    def warning(self, message: str) -> None:
        self._log(LogLevel.WARNING, message)

    def error(self, message: str) -> None:
        self._log(LogLevel.ERROR, message)

    def critical(self, message: str) -> None:
        self._log(LogLevel.CRITICAL, message)

    def set_level(self, level: LogLevel) -> None:
        self.level = level


_default_logger = Logger()


def get_logger(name: str = "Logger", level: LogLevel = LogLevel.INFO) -> Logger:
    return Logger(name, level)


def debug(message: str) -> None:
    _default_logger.debug(message)


def info(message: str) -> None:
    _default_logger.info(message)


def warning(message: str) -> None:
    _default_logger.warning(message)


def error(message: str) -> None:
    _default_logger.error(message)


def critical(message: str) -> None:
    _default_logger.critical(message)


def set_level(level: LogLevel) -> None:
    _default_logger.set_level(level)


__all__ = [
    "LogLevel",
    "critical",
    "debug",
    "error",
    "get_logger",
    "info",
    "set_level",
    "warning",
]
