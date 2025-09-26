import requests
import time
import threading
import os
import sys

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
            if line.startswith("#EXTINF:"):
                name = line.split(",", 1)[-1].strip()
            elif line.startswith("http") and name:
                channels.append((name, line.strip()))
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
        filtered = [(i, name, url) for i, (name, url) in enumerate(channels) if search in name.lower()] if search else [(i, name, url) for i, (name, url) in enumerate(channels)]
        if not filtered:
            print("No channels match your search.")
            continue
        print("Available channels:")
        for idx, name, _ in filtered:
            print(f"{idx+1}. {name}")
        try:
            choice = int(input("Select channel number: "))
            for idx, name, url in filtered:
                if choice == idx+1:
                    return name, url
            print("Invalid choice.")
        except Exception:
            print("Invalid input.")
        # Loop again if invalid

def play_channel(channel_name, m3u8_url):
    def is_mpv_installed():
        if os.name == "nt":
            from shutil import which
            return which("mpv") is not None
        else:
            from shutil import which
            return which("mpv") is not None

    if not is_mpv_installed():
        print("mpv is not installed!")
        if os.name == "nt":
            print("To install mpv on Windows, run:")
            print("scoop install mpv")
        else:
            print("Please install mpv using your system's package manager.")
        return
    print(f'Playing "{channel_name}"')
    # Suppress mpv output
    if os.name == "nt":
        os.system(f"mpv \"{m3u8_url}\" --really-quiet >nul 2>&1")
    else:
        os.system(f"mpv \"{m3u8_url}\" --really-quiet >/dev/null 2>&1")

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
