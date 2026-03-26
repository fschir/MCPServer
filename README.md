# Deutscher Wetterdienst FastMCP Server

A Model Context Protocol (MCP) server that provides access to weather data from the Deutscher Wetterdienst (German Weather Service) through standardized MCP tools.

## Features

- **Weather Alerts**: Get current weather warnings and alerts in English
- **Station Data**: Retrieve weather data from specific weather stations by ID
- **Crowd-sourced Reports**: Access community weather observations
- **HTTP Transport**: Runs as an HTTP server for MCP client connections
- **Configurable Logging**: Output to both console and file with adjustable log levels
- **Docker Support**: Containerized deployment with Docker Compose

## Available Tools

### `get_weather_alerts`
Retrieves current weather alerts and warnings from the Deutscher Wetterdienst API.

### `get_weather_from_station`
Fetches current weather data from specific weather stations using their station IDs.

**Parameters:**
- `ids`: List of station IDs to query

### `get_crowd_weather_data`
Gets current crowd-sourced weather reports from the Deutscher Wetterdienst.

### `fetch_ftp_files`
Downloads all files from a specific directory on the DWD FTP server.

**Parameters:**
- `remote_dir`: Remote directory path to fetch files from (optional, defaults to root)

### `list_ftp_directory`
Lists all files in a specific directory on the DWD FTP server.

**Parameters:**
- `remote_dir`: Remote directory path to list files from (optional, defaults to root)

## Quick Start

### Using Docker (Recommended)

1. Clone the repository:
```bash
git clone <repository-url>
cd MCPServer
```

2. Build and run with Docker Compose:
```bash
docker-compose up --build
```

The server will be available on `http://localhost:8823`

### Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the server:
```bash
python main.py
```

## Configuration

The server supports several command-line arguments:

- `--host`: Host IP to bind the server (default: `0.0.0.0`)
- `--port`: Port number for the server (default: `8823`)
- `--log-level`: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL) (default: `INFO`)
- `--log-file`: Path to log file (default: `mcp_server.log`)

### Examples

```bash
# Run on a specific port
python main.py --port 9000

# Enable debug logging
python main.py --log-level DEBUG

# Custom log file
python main.py --log-file custom.log

# Bind to localhost only
python main.py --host 127.0.0.1
```

## API Integration

The server integrates with Deutscher Wetterdienst's public APIs:

- **Static API v16**: `https://s3.eu-central-1.amazonaws.com/app-prod-static.warnwetter.de/v16/`
- **API v30**: `https://dwd.api.proxy.bund.dev/v30/`
- **FTP Server**: `opendata.dwd.de` (anonymous access)

All requests include appropriate User-Agent headers and handle HTTP/FTP errors gracefully.

## Dependencies

- `fastmcp`: MCP server framework
- `httpx`: Asynchronous HTTP client
- `pandas`: Data manipulation and analysis
- `numpy`: Numerical computing

## Development

### Project Structure

```
MCPServer/
├── server.py            # Server implementation alternative entrypoint
├── src/                 # Reusable helpers and FTP client utilities
│   ├── __init__.py
│   └── utils.py
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker container configuration
├── docker-compose.yml   # Docker Compose setup
└── README.md            # This file
```

### Python Import / Package Usage

You can import FTP utilities directly after setting up `src/__init__.py`:

```python
from src import FTPConfig, fetch_all_ftp_files

ftp_config = FTPConfig()
results = fetch_all_ftp_files(ftp_config, remote_dir="poi")
print(results)
```

### Building

```bash
# Build Docker image
docker build -t mcpserver .

# Run container
docker run -p 8823:8823 mcpserver
```

## License

GNU General Public License v3.0


## Support

For issues and questions, please [create an issue](https://github.com/your-repo/issues) in this repository.