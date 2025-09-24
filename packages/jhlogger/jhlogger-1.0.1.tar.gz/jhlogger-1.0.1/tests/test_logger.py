import logging
import os
import unittest
import unittest.mock
from unittest.mock import patch

from jhlogger import (
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


class TestLogLevel(unittest.TestCase):
    """Test LogLevel enum functionality."""

    def test_log_level_values(self):
        """Test that LogLevel enum has correct values."""
        self.assertEqual(LogLevel.DEBUG.value, "DEBUG")
        self.assertEqual(LogLevel.INFO.value, "INFO")
        self.assertEqual(LogLevel.WARNING.value, "WARNING")
        self.assertEqual(LogLevel.ERROR.value, "ERROR")
        self.assertEqual(LogLevel.CRITICAL.value, "CRITICAL")


class TestConfigurableLogger(unittest.TestCase):
    """Test ConfigurableLogger class functionality."""

    def setUp(self):
        """Set up test fixtures."""
        self.test_logger = None
        # Clear any existing handlers to avoid interference
        logging.getLogger("test-logger").handlers.clear()

    def tearDown(self):
        """Clean up after tests."""
        if self.test_logger:
            # Clear handlers to prevent interference with other tests
            std_logger = logging.getLogger(self.test_logger.name)
            std_logger.handlers.clear()

    def test_initialization_default_values(self):
        """Test logger initialization with default values."""
        logger = ConfigurableLogger()
        self.test_logger = logger

        self.assertEqual(logger.name, "configurable-logger")
        self.assertEqual(logger.log_level, "INFO")
        self.assertTrue(logger.enable_cloudwatch)
        self.assertTrue(logger.enable_sentry)
        self.assertTrue(logger.enable_bugsnag)
        self.assertIsNone(logger.cloudwatch_log_group)
        self.assertTrue(logger.include_system_info)
        self.assertEqual(logger.custom_processors, [])

    def test_initialization_custom_values(self):
        """Test logger initialization with custom values."""
        custom_processors = [lambda x, y, z: z]
        logger = ConfigurableLogger(
            name="test-service",
            log_level=LogLevel.DEBUG,
            enable_cloudwatch=False,
            enable_sentry=False,
            enable_bugsnag=False,
            cloudwatch_log_group="custom-group",
            include_system_info=False,
            custom_processors=custom_processors,
        )
        self.test_logger = logger

        self.assertEqual(logger.name, "test-service")
        self.assertEqual(logger.log_level, "DEBUG")
        self.assertFalse(logger.enable_cloudwatch)
        self.assertFalse(logger.enable_sentry)
        self.assertFalse(logger.enable_bugsnag)
        self.assertEqual(logger.cloudwatch_log_group, "custom-group")
        self.assertFalse(logger.include_system_info)
        self.assertEqual(logger.custom_processors, custom_processors)

    def test_normalize_log_level_enum(self):
        """Test log level normalization with LogLevel enum."""
        logger = ConfigurableLogger()
        self.test_logger = logger

        self.assertEqual(logger._normalize_log_level(LogLevel.DEBUG), "DEBUG")
        self.assertEqual(logger._normalize_log_level(LogLevel.INFO), "INFO")
        self.assertEqual(logger._normalize_log_level(LogLevel.WARNING), "WARNING")
        self.assertEqual(logger._normalize_log_level(LogLevel.ERROR), "ERROR")
        self.assertEqual(logger._normalize_log_level(LogLevel.CRITICAL), "CRITICAL")

    def test_normalize_log_level_string(self):
        """Test log level normalization with string values."""
        logger = ConfigurableLogger()
        self.test_logger = logger

        self.assertEqual(logger._normalize_log_level("debug"), "DEBUG")
        self.assertEqual(logger._normalize_log_level("info"), "INFO")
        self.assertEqual(logger._normalize_log_level("warning"), "WARNING")
        self.assertEqual(logger._normalize_log_level("error"), "ERROR")
        self.assertEqual(logger._normalize_log_level("critical"), "CRITICAL")

    def test_normalize_log_level_invalid(self):
        """Test log level normalization with invalid values."""
        logger = ConfigurableLogger()
        self.test_logger = logger

        # Test with invalid type (integer)
        with self.assertRaises(ValueError) as context:
            logger._normalize_log_level(123)
        self.assertIn("Invalid log level: 123", str(context.exception))

        # Test with invalid type (list)
        with self.assertRaises(ValueError) as context:
            logger._normalize_log_level([])
        self.assertIn("Invalid log level: []", str(context.exception))

    @patch.dict(os.environ, {"APP_ENV": "test", "COUNTRY": "TestCountry"})
    def test_environment_variables(self):
        """Test that environment variables are correctly read."""
        logger = ConfigurableLogger()
        self.test_logger = logger

        self.assertEqual(logger.app_env, "test")
        self.assertEqual(logger.country, "TestCountry")

    def test_get_caller_info(self):
        """Test caller information detection."""
        logger = ConfigurableLogger()
        self.test_logger = logger

        # The _get_caller_info method skips 3 frames, so it will get the test
        # method
        caller_info = logger._get_caller_info()

        self.assertIsInstance(caller_info, dict)
        self.assertIn("filename", caller_info)
        self.assertIn("file_path", caller_info)
        self.assertIn("function", caller_info)
        self.assertIn("line_number", caller_info)
        self.assertIn("module", caller_info)
        # Due to frame skipping, this will be the test method name
        self.assertTrue(caller_info["filename"].endswith(".py"))

    def test_get_caller_info_with_class(self):
        """Test caller information detection from within a class method."""
        logger = ConfigurableLogger()
        self.test_logger = logger

        # Test that caller info includes basic structure
        caller_info = logger._get_caller_info()

        self.assertIsInstance(caller_info, dict)
        self.assertIn("function", caller_info)
        self.assertIn("class", caller_info)  # May be None for functions

    @patch("jhlogger.logger.inspect.currentframe")
    def test_get_caller_info_with_cls_in_locals(self, mock_currentframe):
        """Test caller information detection when 'cls' is in frame locals."""

        # Create a mock frame that simulates a class method call
        class TestClass:
            pass

        # Create a chain of mock frames to simulate frame walking
        # The _get_caller_info method skips 3 frames
        final_frame = unittest.mock.MagicMock()
        final_frame.f_code.co_filename = "/test/path/test_file.py"
        final_frame.f_code.co_name = "test_classmethod"
        final_frame.f_lineno = 42
        final_frame.f_locals = {"cls": TestClass}  # Simulate classmethod with 'cls'
        final_frame.f_back = None

        frame3 = unittest.mock.MagicMock()
        frame3.f_back = final_frame

        frame2 = unittest.mock.MagicMock()
        frame2.f_back = frame3

        frame1 = unittest.mock.MagicMock()
        frame1.f_back = frame2

        # Return the initial frame - _get_caller_info will walk to the final frame
        mock_currentframe.return_value = frame1

        logger = ConfigurableLogger()
        self.test_logger = logger

        caller_info = logger._get_caller_info()

        self.assertIsInstance(caller_info, dict)
        self.assertEqual(caller_info["function"], "test_classmethod")
        self.assertEqual(caller_info["class"], "TestClass")
        self.assertEqual(caller_info["filename"], "test_file.py")
        self.assertEqual(caller_info["line_number"], 42)

    @patch("jhlogger.logger.inspect.currentframe")
    def test_get_caller_info_no_frame(self, mock_currentframe):
        """Test caller information when no frame is available."""
        # Mock currentframe to return None after first call
        mock_currentframe.return_value = None

        logger = ConfigurableLogger()
        self.test_logger = logger

        caller_info = logger._get_caller_info()
        self.assertEqual(caller_info, {})

    @patch("jhlogger.logger.inspect.currentframe")
    def test_get_caller_info_exception_handling(self, mock_currentframe):
        """Test caller information exception handling."""
        # Mock currentframe to raise an exception
        mock_currentframe.side_effect = Exception("Frame access error")

        logger = ConfigurableLogger()
        self.test_logger = logger

        # Should return empty dict when exception occurs
        caller_info = logger._get_caller_info()
        self.assertEqual(caller_info, {})

    def test_add_system_info_enabled(self):
        """Test system info addition when enabled."""
        logger = ConfigurableLogger(include_system_info=True)
        self.test_logger = logger

        event_dict = {}
        result = logger._add_system_info(None, None, event_dict)

        self.assertIn("country", result)
        self.assertIn("environment", result)
        self.assertIn("service", result)
        self.assertIn("timestamp_utc", result)
        self.assertIn("process_id", result)
        self.assertEqual(result["service"], logger.name)

    def test_add_system_info_disabled(self):
        """Test system info addition when disabled."""
        logger = ConfigurableLogger(include_system_info=False)
        self.test_logger = logger

        event_dict = {"existing_key": "existing_value"}
        result = logger._add_system_info(None, None, event_dict)

        self.assertEqual(result, {"existing_key": "existing_value"})

    def test_set_level_string(self):
        """Test dynamic log level change with string."""
        logger = ConfigurableLogger(log_level=LogLevel.INFO)
        self.test_logger = logger

        logger.set_level("DEBUG")
        self.assertEqual(logger.log_level, "DEBUG")

    def test_set_level_enum(self):
        """Test dynamic log level change with enum."""
        logger = ConfigurableLogger(log_level=LogLevel.INFO)
        self.test_logger = logger

        logger.set_level(LogLevel.ERROR)
        self.assertEqual(logger.log_level, "ERROR")

    @patch("jhlogger.logger.CloudWatchLogHandler")
    def test_cloudwatch_handler_setup_success(self, mock_cloudwatch):
        """Test successful CloudWatch handler setup."""
        mock_handler = mock_cloudwatch.return_value

        logger = ConfigurableLogger(enable_cloudwatch=True, cloudwatch_log_group="test-group")
        self.test_logger = logger

        # Verify CloudWatch handler was created with correct parameters
        mock_cloudwatch.assert_called_once()
        call_args = mock_cloudwatch.call_args
        self.assertEqual(call_args[1]["log_group"], "test-group")
        self.assertIn("stream_name", call_args[1])

        # Verify handler was configured
        mock_handler.setLevel.assert_called_once()

    @patch("jhlogger.logger.CloudWatchLogHandler")
    def test_cloudwatch_handler_setup_failure(self, mock_cloudwatch):
        """Test CloudWatch handler setup failure handling."""
        # Mock CloudWatchLogHandler to raise an exception
        mock_cloudwatch.side_effect = Exception("AWS credentials not found")

        # Should not raise exception, should handle gracefully
        logger = ConfigurableLogger(enable_cloudwatch=True, cloudwatch_log_group="test-group")
        self.test_logger = logger

        # Logger should still be created successfully
        self.assertIsNotNone(logger.logger)

    def test_cloudwatch_disabled(self):
        """Test logger creation with CloudWatch disabled."""
        logger = ConfigurableLogger(enable_cloudwatch=False)
        self.test_logger = logger

        # Should create logger successfully without CloudWatch
        self.assertIsNotNone(logger.logger)
        self.assertFalse(logger.enable_cloudwatch)

    def test_cloudwatch_enabled_no_log_group(self):
        """Test CloudWatch enabled but no log group specified."""
        logger = ConfigurableLogger(enable_cloudwatch=True, cloudwatch_log_group=None)
        self.test_logger = logger

        # Should create logger successfully without CloudWatch handler
        self.assertIsNotNone(logger.logger)
        self.assertTrue(logger.enable_cloudwatch)
        self.assertIsNone(logger.cloudwatch_log_group)

    def test_get_logger_method(self):
        """Test get_logger method returns the underlying structlog logger."""
        logger = ConfigurableLogger()
        self.test_logger = logger

        underlying_logger = logger.get_logger()

        # Should return the same logger instance
        self.assertEqual(underlying_logger, logger.logger)
        self.assertTrue(hasattr(underlying_logger, "info"))
        self.assertTrue(hasattr(underlying_logger, "debug"))


class TestLoggingMethods(unittest.TestCase):
    """Test logging methods functionality."""

    def setUp(self):
        """Set up test fixtures."""
        # Create a simple logger for basic testing
        self.test_logger = ConfigurableLogger(
            name="test-logger",
            log_level=LogLevel.DEBUG,
            enable_cloudwatch=False,  # Disable for testing
            include_system_info=False,  # Simplify output for testing
        )

    def tearDown(self):
        """Clean up after tests."""
        # Clear handlers
        std_logger = logging.getLogger(self.test_logger.name)
        std_logger.handlers.clear()

    def test_debug_logging(self):
        """Test DEBUG level logging."""
        # Test that debug method exists and can be called
        try:
            self.test_logger.debug("Test debug message", data={"key": "value"})
        except Exception as e:
            self.fail(f"Debug logging failed: {e}")

    def test_info_logging(self):
        """Test INFO level logging."""
        # Test that info method exists and can be called
        try:
            self.test_logger.info("Test info message", data={"user_id": "123"})
        except Exception as e:
            self.fail(f"Info logging failed: {e}")

    def test_warning_logging(self):
        """Test WARNING level logging."""
        try:
            self.test_logger.warning("Test warning message")
        except Exception as e:
            self.fail(f"Warning logging failed: {e}")

    def test_error_logging_without_exception(self):
        """Test ERROR level logging without exception."""
        try:
            self.test_logger.error("Test error message", data={"error_code": "E001"})
        except Exception as e:
            self.fail(f"Error logging failed: {e}")

    def test_error_logging_with_exception(self):
        """Test ERROR level logging with exception."""
        test_exception = ValueError("Test exception message")
        try:
            self.test_logger.error("Test error with exception", exception=test_exception)
        except Exception as e:
            self.fail(f"Error logging with exception failed: {e}")

    def test_critical_logging(self):
        """Test CRITICAL level logging."""
        try:
            self.test_logger.critical("Test critical message")
        except Exception as e:
            self.fail(f"Critical logging failed: {e}")

    def test_generic_log_method(self):
        """Test generic log method with different levels."""
        # Test with string level
        try:
            self.test_logger.log("INFO", "Test generic info")
        except Exception as e:
            self.fail(f"Generic log method failed: {e}")

        # Test with enum level
        try:
            self.test_logger.log(LogLevel.ERROR, "Test generic error")
        except Exception as e:
            self.fail(f"Generic log method with enum failed: {e}")

    def test_log_method_invalid_level(self):
        """Test generic log method with invalid level."""
        with self.assertRaises(ValueError):
            self.test_logger.log("INVALID", "Test message")

    def test_warn_alias(self):
        """Test that warn is an alias for warning."""
        try:
            self.test_logger.warn("Test warn message")
        except Exception as e:
            self.fail(f"Warn alias failed: {e}")

    @patch("sentry_sdk.capture_exception")
    def test_sentry_integration_error(self, mock_capture):
        """Test Sentry integration for error logging."""
        sentry_logger = ConfigurableLogger(enable_sentry=True)
        test_exception = RuntimeError("Test runtime error")

        sentry_logger.error("Test sentry error", exception=test_exception)

        mock_capture.assert_called_once_with(test_exception)

    @patch("sentry_sdk.capture_exception")
    def test_sentry_integration_critical(self, mock_capture):
        """Test Sentry integration for critical logging."""
        sentry_logger = ConfigurableLogger(enable_sentry=True)
        test_exception = RuntimeError("Test runtime error")

        sentry_logger.critical("Test sentry critical", exception=test_exception)

        mock_capture.assert_called_once_with(test_exception)

    def test_log_method_all_levels(self):
        """Test log method with all different log levels."""
        logger = ConfigurableLogger(
            log_level=LogLevel.DEBUG, enable_cloudwatch=False, enable_sentry=False
        )

        # Test DEBUG branch
        try:
            logger.log(LogLevel.DEBUG, "Test debug via log method")
            logger.log("DEBUG", "Test debug string via log method")
        except Exception as e:
            self.fail(f"DEBUG log method failed: {e}")

        # Test INFO branch
        try:
            logger.log(LogLevel.INFO, "Test info via log method")
            logger.log("INFO", "Test info string via log method")
        except Exception as e:
            self.fail(f"INFO log method failed: {e}")

        # Test WARNING branch
        try:
            logger.log(LogLevel.WARNING, "Test warning via log method")
            logger.log("WARNING", "Test warning string via log method")
        except Exception as e:
            self.fail(f"WARNING log method failed: {e}")

        # Test ERROR branch
        try:
            logger.log(LogLevel.ERROR, "Test error via log method")
            logger.log("ERROR", "Test error string via log method")
        except Exception as e:
            self.fail(f"ERROR log method failed: {e}")

        # Test CRITICAL branch
        try:
            logger.log(LogLevel.CRITICAL, "Test critical via log method")
            logger.log("CRITICAL", "Test critical string via log method")
        except Exception as e:
            self.fail(f"CRITICAL log method failed: {e}")

    @patch("sentry_sdk.capture_exception")
    def test_log_method_sentry_integration(self, mock_capture):
        """Test Sentry integration through log method."""
        logger = ConfigurableLogger(enable_sentry=True)
        test_exception = ValueError("Test exception for log method")

        # Test ERROR level with Sentry
        logger.log(LogLevel.ERROR, "Test error with sentry", exception=test_exception)
        mock_capture.assert_called_with(test_exception)

        # Reset mock
        mock_capture.reset_mock()

        # Test CRITICAL level with Sentry
        logger.log("CRITICAL", "Test critical with sentry", exception=test_exception)
        mock_capture.assert_called_with(test_exception)

    @patch("sentry_sdk.capture_exception")
    def test_sentry_integration_exception_handling(self, mock_capture):
        """Test Sentry integration when capture_exception raises an exception."""
        # Make sentry_sdk.capture_exception raise an exception
        mock_capture.side_effect = Exception("Sentry service unavailable")

        logger = ConfigurableLogger(enable_sentry=True)
        test_exception = RuntimeError("Original exception")

        # Should not raise exception, should handle gracefully
        try:
            logger.error("Test error with failing sentry", exception=test_exception)
            logger.critical("Test critical with failing sentry", exception=test_exception)
            logger.log("ERROR", "Test log error with failing sentry", exception=test_exception)
            logger.log(
                "CRITICAL",
                "Test log critical with failing sentry",
                exception=test_exception,
            )
        except Exception as e:
            self.fail(f"Logger should handle Sentry failures gracefully, but got: {e}")

    def test_format_log_entry_with_exception_no_traceback(self):
        """Test _format_log_entry with exception that has no traceback."""
        logger = ConfigurableLogger()

        # Create exception without traceback
        test_exception = ValueError("Test exception")
        # Ensure __traceback__ is None
        test_exception.__traceback__ = None

        log_entry = logger._format_log_entry("ERROR", "Test message", None, test_exception)

        self.assertIn("exception", log_entry)
        self.assertEqual(log_entry["exception"]["type"], "ValueError")
        self.assertEqual(log_entry["exception"]["message"], "Test exception")
        self.assertEqual(log_entry["exception"]["traceback"], [])

    def test_bound_logger(self):
        """Test bound logger functionality."""
        bound_logger = self.test_logger.bind(request_id="req_123", user_id="user_456")

        # Bound logger should be a structlog bound logger
        self.assertTrue(hasattr(bound_logger, "info"))
        self.assertTrue(hasattr(bound_logger, "bind"))

        # Test that it can log without error
        try:
            bound_logger.info("Test bound message")
        except Exception as e:
            self.fail(f"Bound logger failed: {e}")


class TestConvenienceFunctions(unittest.TestCase):
    """Test module-level convenience functions."""

    def test_debug_function(self):
        """Test debug convenience function."""
        try:
            debug("Test debug message", data={"key": "value"})
        except Exception as e:
            self.fail(f"Debug function failed: {e}")

    def test_info_function(self):
        """Test info convenience function."""
        try:
            info("Test info message", data={"user": "test"})
        except Exception as e:
            self.fail(f"Info function failed: {e}")

    def test_warning_function(self):
        """Test warning convenience function."""
        try:
            warning("Test warning message")
        except Exception as e:
            self.fail(f"Warning function failed: {e}")

    def test_warn_function_alias(self):
        """Test warn convenience function alias."""
        try:
            warn("Test warn message")
        except Exception as e:
            self.fail(f"Warn function failed: {e}")

    def test_error_function(self):
        """Test error convenience function."""
        test_exception = ValueError("Test error")
        try:
            error("Test error message", data={"code": "E001"}, exception=test_exception)
        except Exception as e:
            self.fail(f"Error function failed: {e}")

    def test_critical_function(self):
        """Test critical convenience function."""
        try:
            critical("Test critical message")
        except Exception as e:
            self.fail(f"Critical function failed: {e}")

    def test_log_function(self):
        """Test log convenience function."""
        try:
            log(LogLevel.INFO, "Test log message", data={"test": True})
        except Exception as e:
            self.fail(f"Log function failed: {e}")


class TestCreateLogger(unittest.TestCase):
    """Test create_logger convenience function."""

    def test_create_logger_default(self):
        """Test create_logger with default parameters."""
        test_logger = create_logger()

        self.assertIsInstance(test_logger, ConfigurableLogger)
        self.assertEqual(test_logger.name, "configurable-logger")
        self.assertEqual(test_logger.log_level, "INFO")

    def test_create_logger_custom(self):
        """Test create_logger with custom parameters."""
        test_logger = create_logger(
            name="custom-service", log_level=LogLevel.DEBUG, enable_cloudwatch=False
        )

        self.assertIsInstance(test_logger, ConfigurableLogger)
        self.assertEqual(test_logger.name, "custom-service")
        self.assertEqual(test_logger.log_level, "DEBUG")
        self.assertFalse(test_logger.enable_cloudwatch)


class TestBasicFunctionality(unittest.TestCase):
    """Test basic logger functionality."""

    def test_logger_creation(self):
        """Test that logger can be created without errors."""
        test_logger = ConfigurableLogger()
        self.assertIsNotNone(test_logger)
        self.assertIsNotNone(test_logger.logger)

    def test_all_log_levels_exist(self):
        """Test that all log level methods exist."""
        test_logger = ConfigurableLogger()

        self.assertTrue(hasattr(test_logger, "debug"))
        self.assertTrue(hasattr(test_logger, "info"))
        self.assertTrue(hasattr(test_logger, "warning"))
        self.assertTrue(hasattr(test_logger, "warn"))
        self.assertTrue(hasattr(test_logger, "error"))
        self.assertTrue(hasattr(test_logger, "critical"))
        self.assertTrue(hasattr(test_logger, "log"))

    def test_logger_methods_callable(self):
        """Test that logger methods can be called without error."""
        test_logger = ConfigurableLogger(enable_cloudwatch=False)

        try:
            test_logger.debug("Debug test")
            test_logger.info("Info test")
            test_logger.warning("Warning test")
            test_logger.error("Error test")
            test_logger.critical("Critical test")
        except Exception as e:
            self.fail(f"Logger method failed: {e}")


if __name__ == "__main__":
    unittest.main()
