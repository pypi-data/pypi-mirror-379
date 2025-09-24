"""
JH Logger - A feature-rich, configurable logging module with structured JSON
output.

This module provides comprehensive logging capabilities including:
- Structured JSON logging
- CloudWatch integration
- Sentry error tracking
- Configurable log levels and formats
- Enhanced debugging features
"""

__version__ = "1.0.0"
__author__ = "JH Dev"
__email__ = "dev@jacarandahealth.org"
__description__ = "A feature-rich, configurable logging module with structured JSON output"

from .logger import (
    ConfigurableLogger,
    LogLevel,
    create_logger,
    critical,
    debug,
    error,
    info,
    log,
    warn,
    warning,
)

__all__ = [
    "ConfigurableLogger",
    "LogLevel",
    "create_logger",
    "debug",
    "info",
    "warning",
    "warn",
    "error",
    "critical",
    "log",
]
