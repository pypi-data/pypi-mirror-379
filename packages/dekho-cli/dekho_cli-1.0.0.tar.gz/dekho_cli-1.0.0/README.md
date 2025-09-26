# sports-cli

A CLI tool to fetch and play sports IPTV channels via mpv.

## Installation

1. Install Python (>=3.7) from https://python.org
2. Install mpv:
   - Windows: Download from https://mpv.io/installation/ and add to PATH
   - Linux: `sudo apt install mpv`
   - Mac: `brew install mpv`
3. Install the package:
   ```powershell
   pip install .
   ```

## Usage

Run from command line:
```powershell
dekho-cli
```

## Notes
- The tool fetches the latest playlist every hour.
- Select a channel to play; it will launch mpv with the stream URL.
