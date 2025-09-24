"""
JH Logger - Core logging functionality.

This module provides the main ConfigurableLogger class and convenience
functions
for structured JSON logging with CloudWatch, Sentry, and other integrations.
"""

import contextlib
import datetime
import inspect
import logging
import os
import sys
import traceback
from enum import Enum
from typing import Any, Callable, Dict, List, Optional, Union

import sentry_sdk
import structlog
from watchtower import CloudWatchLogHandler


class LogLevel(Enum):
    """Enumeration for log levels."""

    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"


class ConfigurableLogger:
    """
    A feature-rich, configurable logging module with structured JSON output.

    This logger provides comprehensive logging capabilities including:
    - Structured JSON logging with pretty formatting
    - CloudWatch integration for AWS environments
    - Sentry error tracking
    - Enhanced debugging with caller information
    - Configurable log levels and custom processors
    """

    def __init__(
        self,
        name: str = "configurable-logger",
        log_level: Union[LogLevel, str] = LogLevel.INFO,
        enable_cloudwatch: bool = True,
        enable_sentry: bool = True,
        enable_bugsnag: bool = True,
        cloudwatch_log_group: Optional[str] = None,
        include_system_info: bool = True,
        custom_processors: Optional[List[Callable]] = None,
    ):
        """
        Initialize the ConfigurableLogger.

        Args:
            name: Logger name/identifier
            log_level: Minimum log level (LogLevel enum or string)
            enable_cloudwatch: Enable CloudWatch integration
            enable_sentry: Enable Sentry error tracking
            enable_bugsnag: Enable Bugsnag integration (legacy support)
            cloudwatch_log_group: CloudWatch log group name
            include_system_info: Include system metadata in logs
            custom_processors: List of custom structlog processors
        """
        self.name = name
        self.log_level = self._normalize_log_level(log_level)
        self.enable_cloudwatch = enable_cloudwatch
        self.enable_sentry = enable_sentry
        self.enable_bugsnag = enable_bugsnag
        self.cloudwatch_log_group = cloudwatch_log_group
        self.include_system_info = include_system_info
        self.custom_processors = custom_processors or []

        # Environment variables
        self.app_env = os.getenv("APP_ENV", "development")
        self.country = os.getenv("COUNTRY", "Unknown")

        # Configure the logger
        self.logger = self._configure_logger()

    def _normalize_log_level(self, level: Union[LogLevel, str]) -> str:
        """Normalize log level to string format."""
        if isinstance(level, LogLevel):
            return level.value
        if isinstance(level, str):
            return level.upper()
        raise ValueError(f"Invalid log level: {level}")

    def _get_caller_info(self) -> Dict[str, Any]:
        """
        Get information about the calling function/method.

        Returns:
            Dictionary with caller information including filename, function,
            line number, etc.
        """
        try:
            # Skip 3 frames: this method, _format_log_entry, and the public
            # logging method
            frame = inspect.currentframe()
            for _ in range(3):
                frame = frame.f_back if frame else None

            if not frame:
                return {}

            filename = frame.f_code.co_filename
            function_name = frame.f_code.co_name
            line_number = frame.f_lineno

            # Extract module name
            module_name = inspect.getmodulename(filename) or "unknown"

            # Try to determine class name if we're in a method
            class_name = None
            if "self" in frame.f_locals:
                class_name = frame.f_locals["self"].__class__.__name__
            elif "cls" in frame.f_locals:
                class_name = frame.f_locals["cls"].__name__

            return {
                "filename": os.path.basename(filename),
                "file_path": filename,
                "function": function_name,
                "line_number": line_number,
                "module": module_name,
                "class": class_name,
            }

        except Exception:
            return {}

    def _add_system_info(
        self, logger: Any, method_name: str, event_dict: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Add system information to log entries."""
        if not self.include_system_info:
            return event_dict

        system_info = {
            "country": self.country,
            "environment": self.app_env,
            "service": self.name,
            "timestamp_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "process_id": os.getpid(),
        }

        return {**event_dict, **system_info}

    def _add_caller_info_processor(
        self, logger: Any, method_name: str, event_dict: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Add caller information to log entries."""
        caller_info = self._get_caller_info()
        if caller_info:
            event_dict["caller"] = caller_info
        return event_dict

    def _configure_logger(self) -> structlog.BoundLogger:
        """Configure and return the structured logger."""
        # Build processor chain
        processors = [
            structlog.stdlib.filter_by_level,
            structlog.stdlib.add_logger_name,
            structlog.stdlib.add_log_level,
            structlog.stdlib.PositionalArgumentsFormatter(),
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            self._add_system_info,
            self._add_caller_info_processor,
        ]

        # Add custom processors
        processors.extend(self.custom_processors)

        # Add JSON processor for formatting
        processors.append(
            structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
        )

        # Configure structlog
        structlog.configure(
            processors=processors,  # type: ignore[arg-type]
            wrapper_class=structlog.stdlib.BoundLogger,
            logger_factory=structlog.stdlib.LoggerFactory(),
            cache_logger_on_first_use=True,
        )

        # Get standard library logger
        stdlib_logger = logging.getLogger(self.name)
        stdlib_logger.setLevel(getattr(logging, self.log_level))

        # Clear existing handlers to avoid duplication
        stdlib_logger.handlers.clear()

        # Add console handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(getattr(logging, self.log_level))
        stdlib_logger.addHandler(console_handler)

        # Add CloudWatch handler if enabled
        if self.enable_cloudwatch and self.cloudwatch_log_group:
            try:
                cloudwatch_handler = CloudWatchLogHandler(
                    log_group=self.cloudwatch_log_group,
                    stream_name=f"{self.name}-{os.getpid()}",
                )
                cloudwatch_handler.setLevel(getattr(logging, self.log_level))
                stdlib_logger.addHandler(cloudwatch_handler)
            except Exception:
                # CloudWatch setup failed, continue without it
                pass

        return structlog.get_logger(self.name)  # type: ignore[no-any-return]

    def _format_log_entry(
        self,
        level: str,
        message: str,
        data: Optional[Dict[str, Any]] = None,
        exception: Optional[Exception] = None,
    ) -> Dict[str, Any]:
        """Format a log entry with all metadata."""
        entry: Dict[str, Any] = {
            "message": message,
            "level": level,
        }

        if data:
            entry["data"] = data

        if exception:
            entry["exception"] = {
                "type": type(exception).__name__,
                "message": str(exception),
                "traceback": (
                    traceback.format_exception(type(exception), exception, exception.__traceback__)
                    if exception.__traceback__
                    else []
                ),
            }

        return entry

    def debug(self, message: str, data: Optional[Dict[str, Any]] = None, **kwargs: Any) -> None:
        """Log a DEBUG level message."""
        log_data = self._format_log_entry("DEBUG", message, data)
        self.logger.debug(message, **log_data, **kwargs)

    def info(self, message: str, data: Optional[Dict[str, Any]] = None, **kwargs: Any) -> None:
        """Log an INFO level message."""
        log_data = self._format_log_entry("INFO", message, data)
        self.logger.info(message, **log_data, **kwargs)

    def warning(self, message: str, data: Optional[Dict[str, Any]] = None, **kwargs: Any) -> None:
        """Log a WARNING level message."""
        log_data = self._format_log_entry("WARNING", message, data)
        self.logger.warning(message, **log_data, **kwargs)

    def warn(self, message: str, data: Optional[Dict[str, Any]] = None, **kwargs: Any) -> None:
        """Alias for warning method."""
        self.warning(message, data, **kwargs)

    def error(
        self,
        message: str,
        data: Optional[Dict[str, Any]] = None,
        exception: Optional[Exception] = None,
        **kwargs: Any,
    ) -> None:
        """Log an ERROR level message."""
        log_data = self._format_log_entry("ERROR", message, data, exception)
        self.logger.error(message, **log_data, **kwargs)

        # Send to Sentry if enabled and exception provided
        if self.enable_sentry and exception:
            with contextlib.suppress(Exception):
                # Sentry integration failed, continue
                sentry_sdk.capture_exception(exception)

    def critical(
        self,
        message: str,
        data: Optional[Dict[str, Any]] = None,
        exception: Optional[Exception] = None,
        **kwargs: Any,
    ) -> None:
        """Log a CRITICAL level message."""
        log_data = self._format_log_entry("CRITICAL", message, data, exception)
        self.logger.critical(message, **log_data, **kwargs)

        # Send to Sentry if enabled and exception provided
        if self.enable_sentry and exception:
            with contextlib.suppress(Exception):
                # Sentry integration failed, continue
                sentry_sdk.capture_exception(exception)

    def log(
        self,
        level: Union[LogLevel, str],
        message: str,
        data: Optional[Dict[str, Any]] = None,
        exception: Optional[Exception] = None,
        **kwargs: Any,
    ) -> None:
        """Log a message at the specified level."""
        normalized_level = self._normalize_log_level(level)

        if normalized_level not in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
            raise ValueError(f"Invalid log level: {level}")

        log_data = self._format_log_entry(normalized_level, message, data, exception)

        if normalized_level == "DEBUG":
            self.logger.debug(message, **log_data, **kwargs)
        elif normalized_level == "INFO":
            self.logger.info(message, **log_data, **kwargs)
        elif normalized_level == "WARNING":
            self.logger.warning(message, **log_data, **kwargs)
        elif normalized_level == "ERROR":
            self.logger.error(message, **log_data, **kwargs)
            if self.enable_sentry and exception:
                with contextlib.suppress(Exception):
                    sentry_sdk.capture_exception(exception)
        elif normalized_level == "CRITICAL":
            self.logger.critical(message, **log_data, **kwargs)
            if self.enable_sentry and exception:
                with contextlib.suppress(Exception):
                    sentry_sdk.capture_exception(exception)

    def bind(self, **kwargs: Any) -> structlog.BoundLogger:
        """Create a bound logger with additional context."""
        return self.logger.bind(**kwargs)

    def set_level(self, level: Union[LogLevel, str]) -> None:
        """Dynamically change the log level."""
        self.log_level = self._normalize_log_level(level)

        # Update the standard library logger level
        stdlib_logger = logging.getLogger(self.name)
        stdlib_logger.setLevel(getattr(logging, self.log_level))

        # Update all handlers
        for handler in stdlib_logger.handlers:
            handler.setLevel(getattr(logging, self.log_level))

    def get_logger(self) -> structlog.BoundLogger:
        """Get the underlying structlog logger."""
        return self.logger


# Global logger instance for convenience functions
_default_logger = None


def _get_default_logger() -> ConfigurableLogger:
    """Get or create the default logger instance."""
    global _default_logger
    if _default_logger is None:
        _default_logger = ConfigurableLogger()
    return _default_logger


def create_logger(
    name: str = "configurable-logger",
    log_level: Union[LogLevel, str] = LogLevel.INFO,
    **kwargs: Any,
) -> ConfigurableLogger:
    """
    Create a new ConfigurableLogger instance.

    Args:
        name: Logger name
        log_level: Minimum log level
        **kwargs: Additional logger configuration options

    Returns:
        ConfigurableLogger instance
    """
    return ConfigurableLogger(name=name, log_level=log_level, **kwargs)


# Convenience functions for module-level logging
def debug(message: str, data: Optional[Dict[str, Any]] = None, **kwargs: Any) -> None:
    """Log a DEBUG level message using the default logger."""
    _get_default_logger().debug(message, data, **kwargs)


def info(message: str, data: Optional[Dict[str, Any]] = None, **kwargs: Any) -> None:
    """Log an INFO level message using the default logger."""
    _get_default_logger().info(message, data, **kwargs)


def warning(message: str, data: Optional[Dict[str, Any]] = None, **kwargs: Any) -> None:
    """Log a WARNING level message using the default logger."""
    _get_default_logger().warning(message, data, **kwargs)


def warn(message: str, data: Optional[Dict[str, Any]] = None, **kwargs: Any) -> None:
    """Alias for warning function."""
    warning(message, data, **kwargs)


def error(
    message: str,
    data: Optional[Dict[str, Any]] = None,
    exception: Optional[Exception] = None,
    **kwargs: Any,
) -> None:
    """Log an ERROR level message using the default logger."""
    _get_default_logger().error(message, data, exception, **kwargs)


def critical(
    message: str,
    data: Optional[Dict[str, Any]] = None,
    exception: Optional[Exception] = None,
    **kwargs: Any,
) -> None:
    """Log a CRITICAL level message using the default logger."""
    _get_default_logger().critical(message, data, exception, **kwargs)


def log(
    level: Union[LogLevel, str],
    message: str,
    data: Optional[Dict[str, Any]] = None,
    exception: Optional[Exception] = None,
    **kwargs: Any,
) -> None:
    """Log a message at the specified level using the default logger."""
    _get_default_logger().log(level, message, data, exception, **kwargs)
