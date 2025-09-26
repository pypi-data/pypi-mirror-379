# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.6] - 2025-09-12

### Fixed

- **CRITICAL**: Fixed response format compatibility with Spider MCP server API
- Updated client to handle new server response format: `{"status": {"success": true/false, ...}, ...}`
- Fixed error handling to properly parse server error responses
- Improved data transformation to convert server response to expected client format
- Enhanced parser identification in response metadata

### Changed

- Response parsing now handles nested status objects from server
- Error messages now properly extracted from server error responses
- Parser information now correctly formatted in `status_detail.parser_used`

### Tested

- Comprehensive testing with 35 parsers showing 91.4% success rate
- All major site categories working: news, deals, education, forums
- Performance verified: average 2.58s response time

## [0.1.5] - 2025-08-15

### Added

- Enhanced error handling with more specific error categories
- Improved retry logic for browser pool exhaustion
- Better session management with app-specific isolation

## [0.1.0] - 2025-01-17

### Added

- Initial release of spider-mcp-client
- `SpiderMCPClient` class with full API support
- `parse_url()` method for web scraping
- `check_parser()` method to verify parser availability
- `get_parsers()` method to list available parsers
- Built-in retry logic with exponential backoff
- Rate limiting with configurable delays
- Comprehensive error handling with specific exception types
- Context manager support for automatic cleanup
- Type hints for better IDE experience
- Session isolation with custom app names
- Image download support
- Full documentation and examples

### Features

- ✅ Simple one-method API for parsing URLs
- ✅ Automatic retries with exponential backoff
- ✅ Rate limiting to respect server resources
- ✅ Clear exception hierarchy for error handling
- ✅ Optional image download and localization
- ✅ Session isolation for multiple applications
- ✅ Context manager support
- ✅ Full typing support
- ✅ Comprehensive documentation

### Dependencies

- requests>=2.25.0
- typing-extensions>=4.0.0 (Python <3.10)

### Python Support

- Python 3.8+
- Tested on Python 3.8, 3.9, 3.10, 3.11, 3.12
