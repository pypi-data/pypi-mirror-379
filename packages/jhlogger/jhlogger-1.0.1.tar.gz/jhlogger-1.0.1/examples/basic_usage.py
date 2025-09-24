#!/usr/bin/env python3
"""
Basic usage examples for ConfigurableLogger.
"""

from jhlogger import ConfigurableLogger, LogLevel, critical, debug, error, info, warning


def basic_logging_examples():
    """Demonstrate basic logging functionality."""
    print("=== Basic Logging Examples ===\n")

    # Simple messages
    info("Application started successfully")
    warning("This is a warning message")

    # With additional data
    info(
        "User logged in",
        data={
            "user_id": "12345",
            "username": "john_doe",
            "ip_address": "192.168.1.100",
        },
    )

    # ERROR with exception
    try:
        _ = 10 / 0  # This will raise an exception
    except ZeroDivisionError as e:
        error("Division by zero error occurred", data={"operation": "10 / 0"}, exception=e)

    # DEBUG with full traceback
    debug("Debug information", data={"debug_flag": True, "step": "initialization"})


def custom_logger_example():
    """Demonstrate custom logger creation."""
    print("\n=== Custom Logger Example ===\n")

    # Create a custom logger with specific configuration
    logger = ConfigurableLogger(
        name="my-custom-service",
        log_level=LogLevel.DEBUG,
        enable_cloudwatch=False,  # Disable for demo
        include_system_info=True,
    )

    logger.info("Custom logger initialized")
    logger.debug("Debug mode enabled", data={"config": "custom"})

    # Test all log levels
    logger.debug("Debug message")
    logger.info("Info message")
    logger.warning("Warning message")
    logger.error("Error message")
    logger.critical("Critical message")


def class_based_example():
    """Demonstrate class-based logging."""
    print("\n=== Class-based Logging Example ===\n")

    class UserService:
        def __init__(self):
            self.logger = ConfigurableLogger(name="user-service")

        def create_user(self, username: str, email: str):
            self.logger.info(
                "Creating new user",
                data={"username": username, "email": email, "action": "create_user"},
            )

            try:
                # Simulate some processing
                if "@" not in email:
                    raise ValueError("Invalid email format")

                self.logger.info(
                    "User created successfully",
                    data={"username": username, "result": "success"},
                )

            except ValueError as e:
                self.logger.error(
                    "Failed to create user",
                    data={"username": username, "email": email},
                    exception=e,
                )

    # Use the service
    service = UserService()
    service.create_user("john_doe", "john@example.com")
    service.create_user("invalid_user", "invalid-email")  # This will cause an error


def bound_context_example():
    """Demonstrate bound context logging."""
    print("\n=== Bound Context Example ===\n")

    logger = ConfigurableLogger(name="context-demo")

    # Log with bound context (adds context to all subsequent logs)
    bound_logger = logger.bind(request_id="req_789012", session_id="sess_345678")

    bound_logger.info("Processing request with bound context")
    bound_logger.warning("Rate limit approaching", data={"remaining_requests": 5})


if __name__ == "__main__":
    print("ConfigurableLogger - Basic Usage Examples\n" + "=" * 50)

    try:
        basic_logging_examples()
        custom_logger_example()
        class_based_example()
        bound_context_example()

        print("\n" + "=" * 50)
        print("All examples completed successfully!")
        print("\nNote: All JSON logs are formatted with 4-space indentation and sorted keys")
        print("for enhanced readability and consistency.")

    except Exception as e:
        critical("Examples failed with unexpected error", exception=e)
