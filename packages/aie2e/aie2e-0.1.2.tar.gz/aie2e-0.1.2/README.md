# AIE2E MCP Server

The Python server component of the AI-powered end-to-end testing framework. This package provides the Model Context Protocol (MCP) server that executes browser automation tasks using AI agents.

## Description

AIE2E MCP Server is the backend component that powers the AI End-to-End Testing Framework. It provides a Model Context Protocol (MCP) server for running browser-based tests using AI agents and supports both stdio and HTTP transport mechanisms.

## Prerequisites

- **Python** >= 3.11
- **Chrome or Chromium browser** (automatically downloaded if not found)
- **pip** for package management

## Installation

### From PyPI (Recommended)

```bash
pip install aie2e-server
```

### From Source (Development)

```bash
git clone https://github.com/aie2e/aie2e-server.git
cd aie2e-server
pip install -r requirements.txt
pip install -e .
```

### Verify Installation

Test that the server is installed correctly:

```bash
python -m aie2e.mcp_server --help
```

## Usage

The MCP server can be run with two different transport mechanisms:

### Stdio Transport (Default)

The stdio transport is used by default and is recommended for most use cases. You must specify the LLM configuration:

```bash
python -m aie2e.mcp_server --model "gpt-4" --llm-provider "openai" --api-key "your-api-key"
```

Or explicitly specify stdio transport:

```bash
python -m aie2e.mcp_server --transport stdio --model "gemini-2.5-pro" --llm-provider "google" --api-key "your-api-key"
```

### HTTP Transport

The HTTP transport uses Server-Sent Events (SSE) over HTTP and is useful for remote connections:

```bash
python -m aie2e.mcp_server --transport http --host 127.0.0.1 --port 3001 --model "claude-3-sonnet" --llm-provider "anthropic" --api-key "your-api-key"

# Run in headless mode (no browser UI)
python -m aie2e.mcp_server --transport http --port 3001 --model "gpt-4" --llm-provider "openai" --headless
```

### Using Environment Variables

The API key can be set using environment variables instead of command line arguments. 
Use the standard environment variable name for your chosen provider, as supported by Browser-Use

```bash
# Set the API key as an environment variable
export OPENAI_API_KEY="your-openai-key"
export ANTHROPIC_API_KEY="your-anthropic-key"
export GOOGLE_API_KEY="your-google-key"

# Run without --api-key argument
python -m aie2e.mcp_server --model "gpt-4" --llm-provider "openai"
```

## MCP Protocol

The server implements the Model Context Protocol (MCP) and provides the following tool:

### `run_test_session`

Executes browser-based test sessions using AI agents.

**Server Configuration (Command Line):**
The server configuration is set once at startup via command line arguments:
- `--model`: AI model to use (e.g., "gemini-2.5-pro", "gpt-4") - **Required**
- `--llm-provider`: LLM provider (e.g., "google", "openai", "anthropic") - **Required**
- `--api-key`: API key for the LLM provider (optional, can use environment variables like `OPENAI_API_KEY`)
- `--headless`: Run browser in headless mode (default: false)

**MCP Tool Parameters:**
- `description`: Description of the test session
- `tests`: Array of test cases to execute
- `allowed_domains`: List of allowed domains for navigation (optional)
- `sensitive_data`: Sensitive data for form filling (optional)

## Integration

The MCP server is designed to work with MCP-compatible clients. For JavaScript/TypeScript projects, use the [AIE2E Node.js client](https://github.com/aie2e/aie2e-client) which automatically connects to this server.

### Using with AIE2E Client

The most common usage is with the AIE2E Node.js client:

```bash
# Install both components
npm install --save-dev aie2e
pip install aie2e-server

# The client automatically manages the server via stdio transport
npx aie2e ./tests
```

## Troubleshooting

### Common Issues

**"ModuleNotFoundError: No module named 'aie2e'"**
- Ensure you ran the installation: `pip install aie2e-server`
- Check your Python environment: `python -c "import aie2e; print('Installation OK')"`

**"Command not found: python"**
- On some systems, use `python3` instead of `python`
- Ensure Python is installed and in your PATH

**Browser issues**
- The server automatically downloads Chrome/Chromium if not found
- On Linux, you may need: `sudo apt-get install chromium-browser`
- On macOS with Homebrew: `brew install chromium`

**Permission errors**
- Try running with elevated privileges if needed
- Ensure your user has permission to create browser profiles

### Getting Help

- Check the [issues page](https://github.com/aie2e/aie2e-server/issues) for known problems
- Create a new issue with your error message and system information

### Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## Related Projects

- [AIE2E Client](https://github.com/aie2e/aie2e-client) - Node.js client component
- [Model Context Protocol](https://github.com/modelcontextprotocol) - Protocol specification
- [Browser Use](https://github.com/browser-use/browser-use) - Underlying browser automation library

## License

MIT License - see [LICENSE](LICENSE) for details