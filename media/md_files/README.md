# caching-proxy

CLI tool for caching HTTP requests  
Project from [roadmap.sh](https://roadmap.sh/projects/caching-server)

## Implementation

- While the proxy server is running, the cache is stored in memory, which makes it fast but can use a lot of RAM. For this learning project, this simple approach is enough.  
- Before starting, the `main.py` script reads a `*.json` file to load the saved cache. When the server stops, the cache is saved back to the file.  
- For a real-use version, the cache should be stored in **Redis**, and error handling should be improved.

## Technologies

- `python3.14`  
- `fastapi` — backend framework  
- `httpx` — HTTP client for external requests  
- `uvicorn` — server  
- `argparse` — command-line argument parser  

## Issues / TODO

- Improve in-memory cache (cachetools, Redis)  
- Improve logging  
- Add testing  
- Add docstrings  
- Code formatting  

## Installation and Usage

The development version is managed with the `uv` tool. I recommend [installing it](https://docs.astral.sh/uv/getting-started/installation/).

1. Clone the repository and move into it:
```bash
git clone https://github.com/dayanik/cashing-proxy
cd cashing-proxy
```

2. Install dependencies:
```bash
uv sync
```

3. Run the server. Run it from the project directory so the cache file is not lost:
```bash
uv run main.py --port 3030 --origin https://roadmap.sh
```

4. To stop the server, press `Ctrl + C`. The cache will be saved automatically.

5. Clear the cache:
```bash
uv run main.py --clear_cache
```

6. Get help for commands:
```bash
uv run main.py --help
```