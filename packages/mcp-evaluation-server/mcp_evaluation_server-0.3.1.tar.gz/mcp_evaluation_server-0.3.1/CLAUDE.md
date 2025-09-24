# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an MCP (Model Context Protocol) Evaluation Server - a tool evaluation and recommendation system built with Python and FastMCP. It provides intelligent search, evaluation, and ranking of MCP tools with comprehensive testing and performance analysis.

## Development Environment

### Package Management
- **Primary**: UV (modern Python package manager)
- **Python Version**: 3.12+ (minimum 3.11)
- **Dependencies**: Managed through `pyproject.toml`

### Key Commands
```bash
# Install dependencies
uv sync

# Install with development dependencies
uv sync --dev

# Run the MCP server
uv run python -m mcp_evaluation_server.main

# Run HTTP server mode
uv run python server.py

# Run tests
uv run pytest
uv run pytest tests/ -m "unit"
uv run pytest tests/ -m "integration"

# Code formatting
uv run black mcp_evaluation_server/ tests/
uv run isort mcp_evaluation_server/ tests/

# Type checking
uv run mypy mcp_evaluation_server/

# Build package
uv build
```

## Architecture

### Core Components

1. **FastMCP Server** (`main.py`)
   - MCP server implementation using FastMCP framework
   - Supports both stdio and HTTP transport modes
   - Handles tool registration and request processing

2. **Database Layer** (`database.py`)
   - Supabase PostgreSQL integration
   - Implements comprehensive data validation and error handling
   - Features intelligent query fallback mechanisms
   - Includes retry logic and timeout handling

3. **Data Models** (`models.py`)
   - Pydantic models for type safety
   - MCP tool information, test results, search filters
   - Validation and serialization logic

4. **Tool Functions** (`tools.py`)
   - Modular tool implementations
   - Basic search, detailed tool information, test statistics
   - Performance data retrieval

5. **Configuration** (`config.py`)
   - Secure configuration management with encryption
   - Environment variable handling
   - C extension support for enhanced security

### Database Schema

The system uses two main Supabase tables:
- `mcp_tools`: Core tool information and metadata
- `mcp_test_results`: Test execution results and performance data

### Security Features

- Encrypted configuration management
- C extension support for sensitive data protection
- Secure key handling with fragment-based storage
- Environment-based configuration

## Development Notes

### Code Style
- **Line length**: 88 characters (Black default)
- **Type hints**: Required for all functions and methods
- **Imports**: Sorted with isort
- **Documentation**: Comprehensive docstrings in Chinese

### Testing Approach
- Unit tests for individual components
- Integration tests for database operations
- Test markers: `unit`, `integration`, `slow`
- Coverage reporting available

### Error Handling
- Custom exception classes in `exceptions.py`
- Comprehensive logging throughout
- Graceful degradation for database failures
- Retry mechanisms for transient errors

### Performance Considerations
- Lazy initialization of database connections
- Query result caching
- Pagination support for large datasets
- Efficient data validation and parsing

## MCP Tools Available

1. **search_mcp_tools_basic**: Fast, lightweight tool search
2. **get_mcp_tool_details**: Comprehensive tool information
3. **get_tool_test_stats**: Test statistics and success rates
4. **get_tool_performance_data**: Performance metrics and trends
5. **health_check**: Service status and database connectivity

## Configuration

Environment variables (see `.env.example`):
- `SUPABASE_URL`: Supabase project URL
- `SUPABASE_SERVICE_ROLE_KEY`: Database access key
- `MCP_TOOLS_TABLE`: Tools table name
- `MCP_TEST_RESULTS_TABLE`: Test results table name
- `LOG_LEVEL`: Logging verbosity
- `LOG_FILE`: Log file path

## Build and Deployment

The project supports both source and wheel distribution with optional C extensions for enhanced security. Use `uv build` for packaging and consult `setup.py` for build configuration details.