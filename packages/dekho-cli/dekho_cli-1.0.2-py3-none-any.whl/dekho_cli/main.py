import requests
import time
import threading
import os

GITHUB_M3U_URL = "https://raw.githubusercontent.com/abusaeeidx/IPTV-Scraper-Zilla/main/CricHD.m3u"
FETCH_INTERVAL = 3600  # seconds (1 hour)

channels = []

def fetch_m3u8():
    global channels
    try:
        resp = requests.get(GITHUB_M3U_URL)
        resp.raise_for_status()
        lines = resp.text.splitlines()
        channels = []
        name = None
        for line in lines:
            line = line.strip()
            if line.startswith("#EXTINF:"):
                # Extract the name after the last comma
                parts = line.split(",", 1)
                name = parts[-1].strip() if len(parts) > 1 else "Unnamed Channel"
            elif line.startswith("http") and name:
                channels.append((name, line))
                name = None
    except Exception as e:
        print(f"Error fetching playlist: {e}")

def periodic_fetch():
    while True:
        fetch_m3u8()
        time.sleep(FETCH_INTERVAL)

def select_channel():
    if not channels:
        print("No channels available. Try again later.")
        return None
    while True:
        search = input("Search channel (or press Enter to list all): ").strip().lower()
        # Filter channels by search
        filtered = [(name, url) for name, url in channels if search in name.lower()] if search else channels[:]
        if not filtered:
            print("No channels match your search.")
            continue
        # Display channels
        print("Available channels:")
        for idx, (name, _) in enumerate(filtered, 1):
            print(f"{idx}. {name}")
        try:
            choice = int(input("Select channel number: "))
            if 1 <= choice <= len(filtered):
                return filtered[choice - 1]
            print("Invalid choice.")
        except Exception:
            print("Invalid input.")

def play_channel(channel_name, m3u8_url):
    from shutil import which
    if which("mpv") is None:
        print("mpv is not installed!")
        if os.name == "nt":
            print("To install mpv on Windows, run: scoop install mpv")
        else:
            print("Please install mpv using your system's package manager.")
        return
    print(f'Playing "{channel_name}"...')
    # Suppress mpv output
    if os.name == "nt":
        os.system(f'mpv "{m3u8_url}" --really-quiet >nul 2>&1')
    else:
        os.system(f'mpv "{m3u8_url}" --really-quiet >/dev/null 2>&1')

def main():
    print(r"""
          __      _
       o'')}____//
        `_/      )
        (_(_/-(_/
        
       ⚡ dekho-cli 1.0.0 ⚡
          made by abhilash
""")
    print("Fetching playlist...")
    fetch_m3u8()
    threading.Thread(target=periodic_fetch, daemon=True).start()

    while True:
        result = select_channel()
        if result:
            channel_name, m3u8_url = result
            play_channel(channel_name, m3u8_url)
        again = input("Play another channel? (y/n): ").lower()
        if again != 'y':
            break

if __name__ == "__main__":
    main()
