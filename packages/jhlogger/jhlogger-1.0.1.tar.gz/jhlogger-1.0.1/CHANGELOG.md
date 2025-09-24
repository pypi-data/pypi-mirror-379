# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-09-18

### Added

- Initial release of ConfigurableLogger
- Configurable log levels with dynamic runtime changes
- Structured JSON output with 4-space indentation and sorted keys
- Full traceback support for DEBUG level logging
- Exception details capture for ERROR level logging
- Automatic caller information detection (filename, function, class, line number)
- Third-party service integration (CloudWatch, Sentry, Bugsnag)
- Relative file paths for enhanced security
- Environment-aware configuration
- Support for bound context logging
- Comprehensive test suite with 92%+ coverage
- Complete documentation and examples
- MIT License

### Features

- **Security**: Uses relative file paths to prevent system information exposure
- **Performance**: Efficient CloudWatch batching and lazy evaluation
- **Flexibility**: Configurable processors and custom data fields
- **Reliability**: Comprehensive error handling and fallback mechanisms
- **Usability**: Simple API with both convenience functions and class-based usage

### Dependencies

- structlog >= 23.0.0
- watchtower >= 3.0.0
- sentry-sdk >= 1.0.0

### Python Support

- Python 3.8+
- Tested on Python 3.8, 3.9, 3.10, 3.11, 3.12
