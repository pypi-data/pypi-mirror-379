# WavespeedMCP

## [English](README.md) ｜ [中文文档](README.zh.md)

WavespeedMCP is a Model Control Protocol (MCP) server implementation for WaveSpeed AI services. It provides a standardized interface for accessing WaveSpeed's image and video generation capabilities through the MCP protocol.

## Features

- **Advanced Image Generation**: Create high-quality images from text prompts with support for image-to-image generation, inpainting, and LoRA models
- **Dynamic Video Generation**: Transform static images into videos with customizable motion parameters
- **Optimized Performance**: Enhanced API polling with intelligent retry logic and detailed progress tracking
- **Flexible Resource Handling**: Support for URL, Base64, and local file output modes
- **Comprehensive Error Handling**: Specialized exception hierarchy for precise error identification and recovery
- **Robust Logging**: Detailed logging system for monitoring and debugging
- **Multiple Configuration Options**: Support for environment variables, command-line arguments, and configuration files

## Installation

### Prerequisites

- Python 3.11+
- WaveSpeed API key (obtain from [WaveSpeed AI](https://wavespeed.ai))

### Setup

Install directly from PyPI:

```bash
pip install wavespeed-mcp
```

### MCP Configuration

To use WavespeedMCP with your IDE or application, add the following configuration:

```json
{
  "mcpServers": {
    "WaveSpeed": {
      "command": "wavespeed-mcp",
      "env": {
        "WAVESPEED_API_KEY": "your-api-key-here",
        "WAVESPEED_LOG_FILE": "/tmp/wavespeed-mcp.log"
      }
    }
  }
}
```

## Usage

### Running the Server

Start the WavespeedMCP server:

```bash
wavespeed-mcp --api-key your_api_key_here
```

### Claude Desktop Integration

WavespeedMCP can be integrated with Claude Desktop. To generate the necessary configuration file:

```bash
python -m wavespeed_mcp --api-key your_api_key_here --config-path /path/to/claude/config
```

This command generates a `claude_desktop_config.json` file that configures Claude Desktop to use WavespeedMCP tools. After generating the configuration:

1. Start the WavespeedMCP server using the `wavespeed-mcp` command
2. Launch Claude Desktop, which will use the configured WavespeedMCP tools

## Configuration Options

WavespeedMCP can be configured through:

1. **Environment Variables**:

   - `WAVESPEED_API_KEY`: Your WaveSpeed API key (required)
   - `WAVESPEED_API_HOST`: API host URL (default: https://api.wavespeed.ai)
   - `WAVESPEED_MCP_BASE_PATH`: Base path for saving generated files (default: ~/Desktop)
   - `WAVESPEED_API_RESOURCE_MODE`: Resource output mode - `url`, `local`, or `base64` (default: url)
   - `WAVESPEED_LOG_LEVEL`: Logging level - DEBUG, INFO, WARNING, ERROR (default: INFO)
   - `WAVESPEED_LOG_FILE`: Optional log file path (if not set, logs to console)
   - `WAVESPEED_API_TEXT_TO_IMAGE_ENDPOINT`: Custom endpoint for text-to-image generation (default: /wavespeed-ai/flux-dev)
   - `WAVESPEED_API_IMAGE_TO_IMAGE_ENDPOINT`: Custom endpoint for image-to-image generation (default: /wavespeed-ai/flux-kontext-pro)
   - `WAVESPEED_API_VIDEO_ENDPOINT`: Custom endpoint for video generation (default: /wavespeed-ai/wan-2.1/i2v-480p-lora)

### Timeouts

WavespeedMCP supports two types of timeouts. Configure them via environment variables:

- `WAVESPEED_REQUEST_TIMEOUT`: Per-HTTP request timeout in seconds (default: 300 = 5 minutes).
  This applies to individual HTTP calls made by the client, such as submitting a job or downloading outputs.

- `WAVESPEED_WAIT_RESULT_TIMEOUT`: Total timeout for waiting/polling results in seconds (default: 600 = 10 minutes).
  This limits the overall time spent polling for an asynchronous job result. When exceeded, polling stops with a timeout error.

Example:

```bash
export WAVESPEED_REQUEST_TIMEOUT=300          # per HTTP request
export WAVESPEED_WAIT_RESULT_TIMEOUT=900      # total wait for result (polling)
```

### Logging Configuration

By default, the MCP server logs to console. You can configure file logging by setting the `WAVESPEED_LOG_FILE` environment variable:

```bash
# Log to /tmp directory
export WAVESPEED_LOG_FILE=/tmp/wavespeed-mcp.log

# Log to system log directory
export WAVESPEED_LOG_FILE=/var/log/wavespeed-mcp.log

# Log to user home directory
export WAVESPEED_LOG_FILE=~/logs/wavespeed-mcp.log
```

The log file uses rotating file handler with:
- Maximum file size: 10MB
- Backup count: 5 files
- Log format: `%(asctime)s - wavespeed-mcp - %(levelname)s - %(message)s`

2. **Command-line Arguments**:

   - `--api-key`: Your WaveSpeed API key
   - `--api-host`: API host URL
   - `--config`: Path to configuration file

3. **Configuration File** (JSON format):
   See `wavespeed_mcp_config_demo.json` for an example.

## Architecture

WavespeedMCP follows a clean, modular architecture:

- `server.py`: Core MCP server implementation with tool definitions
- `client.py`: Optimized API client with intelligent polling
- `utils.py`: Comprehensive utility functions for resource handling
- `exceptions.py`: Specialized exception hierarchy for error handling
- `const.py`: Constants and default configuration values

## Development

### Requirements

- Python 3.11+
- Development dependencies: `pip install -e ".[dev]"`

### Testing

Run the test suite:

```bash
pytest
```

Or with coverage reporting:

```bash
pytest --cov=wavespeed_mcp
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support or feature requests, please contact the WaveSpeed AI team at support@wavespeed.ai.
