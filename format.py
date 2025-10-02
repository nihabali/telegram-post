#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TMDB Movie/Series Post Template Generator with Telegram Markdown Links
Usage: python3 tmdb_poster_maker.py
"""

import requests
import re
import sys
from datetime import datetime

# Direct API key inside code
API_KEY = "04a8552922af8bbfb9fce1e25b9213b1"

def parse_tmdb_link(link):
    m = re.search(r"/(movie|tv)/(\d+)", link)
    if m:
        return m.group(1), int(m.group(2))
    m2 = re.match(r"^\d+$", link.strip())
    if m2:
        return None, int(link.strip())
    return None, None

def human_duration(minutes):
    if minutes is None:
        return "-"
    hrs = minutes // 60
    mins = minutes % 60
    return f"{hrs}h {mins}m" if hrs > 0 else f"{mins}m"

def fetch_movie_details(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    params = {"api_key": API_KEY, "language": "en-US"}
    r = requests.get(url, params=params, timeout=10)
    r.raise_for_status()
    return r.json()

def fetch_tv_details(tv_id):
    url = f"https://api.themoviedb.org/3/tv/{tv_id}"
    params = {"api_key": API_KEY, "language": "en-US"}
    r = requests.get(url, params=params, timeout=10)
    r.raise_for_status()
    return r.json()

def fetch_season_details(tv_id, season_number):
    url = f"https://api.themoviedb.org/3/tv/{tv_id}/season/{season_number}"
    params = {"api_key": API_KEY, "language": "en-US"}
    r = requests.get(url, params=params, timeout=10)
    r.raise_for_status()
    return r.json()

def choose(prompt, options):
    print(prompt)
    for idx, opt in enumerate(options, start=1):
        print(f" {idx}. {opt}")
    while True:
        sel = input("Choice (number): ").strip()
        if sel.isdigit() and 1 <= int(sel) <= len(options):
            return int(sel)
        print("Enter a valid number between 1 and", len(options))

def format_genres(genres_list):
    try:
        names = [g['name'] for g in genres_list]
        return ", ".join(names[:2]) if names else "-"
    except:
        return "-"

def detect_status(tv_data, season_info):
    overall_status = tv_data.get("status", "").lower()
    season_air_date = season_info.get("air_date")
    last_episode = season_info.get("episodes", [])[-1] if season_info.get("episodes") else None

    today = datetime.today().date()

    if last_episode and last_episode.get("air_date"):
        try:
            air_dt = datetime.strptime(last_episode["air_date"], "%Y-%m-%d").date()
            if air_dt < today:
                return "Completed"
            elif air_dt > today:
                return "Upcoming"
            else:
                return "Releasing"
        except:
            pass

    if season_air_date:
        try:
            air_dt = datetime.strptime(season_air_date, "%Y-%m-%d").date()
            if air_dt > today:
                return "Upcoming"
        except:
            pass

    if "ended" in overall_status:
        return "Completed"
    if "returning" in overall_status:
        return "Releasing"
    if "in production" in overall_status:
        return "Releasing"
    if "planned" in overall_status:
        return "Upcoming"

    return "Releasing"

def main():
    print("=======================================")
    print(" TMDB-based Movie/Series Poster Maker")
    print("=======================================\n")

    kind_sel = choose("Select type:", ["Movie", "Series"])
    kind = "movie" if kind_sel == 1 else "tv"

    audio_sel = choose("Select Audio:", ["Hindi", "English"])
    audio_text = "Hindi" if audio_sel == 1 else "English"

    tmdb_link = input("Enter TMDB link or ID: ").strip()
    parsed_type, parsed_id = parse_tmdb_link(tmdb_link)
    if parsed_id is None:
        print("Invalid TMDB link or ID.")
        sys.exit(1)

    detected_type = parsed_type if parsed_type else kind
    if parsed_type and parsed_type != kind:
        print(f"Note: You selected {kind} but the link is {parsed_type}. Using link type instead.")
        kind = parsed_type

    try:
        if kind == "movie":
            data = fetch_movie_details(parsed_id)
            title = data.get("title") or "-"
            release_date = data.get("release_date") or "-"
            try:
                rd = datetime.strptime(release_date, "%Y-%m-%d")
                release_fmt = rd.strftime("%b %d, %Y")
            except:
                release_fmt = release_date
            rating = data.get("vote_average")
            rating_text = f"{rating}/10 (TMDB)" if rating else "TMDB"
            runtime = data.get("runtime")
            duration_text = human_duration(runtime)
            genres = format_genres(data.get("genres", []))
            qual_sel = choose("Select Quality:", ["SD", "HD", "FHD"])
            quality_text = ["SD","HD","FHD"][qual_sel-1]

            output = []
            output.append(f"🎬 Movie Title: {title}")
            output.append("╭──────────────────────")
            output.append(f"├ 📅 Release - {release_fmt}")
            output.append(f"├ ⭐ Ratings - {rating_text}")
            output.append(f"├ 📺 Duration - {duration_text}")
            output.append(f"├ 🎵 Audio - Dual | {audio_text} #Official")
            output.append(f"├ 📼 Quality - {quality_text}")
            output.append(f"├ 🎭 Genres - {genres}")
            output.append(f"├ 🧩 [AD Skip](https://telegra.ph/How-to-Skip-Ads-and-Download-Easily-04-04) | [Download Tutorial](https://telegra.ph/How-to-Download-from-GDFLIX-Fast--Direct-Links-04-04)")
            output.append("╰──────────────────────")
            output.append("╭──────────────────────")
            output.append("├ 📢 Backup Channel & Info Bot:")
            output.append("├ 📌 [Channel](https://t.me/+2jrpUqXgr-hmOWM1) | [Bot](http://t.me/othersottinfobot)")
            output.append("╰──────────────────────")
            print("\n\nFinal Template (copy manually):\n")
            print("\n".join(output))

        else:
            tv = fetch_tv_details(parsed_id)
            title = tv.get("name") or "-"
            seasons = tv.get("seasons", []) or []
            season_numbers = [s.get("season_number") for s in seasons if s.get("season_number") is not None]

            print(f"Total seasons found: {len(season_numbers)}")
            for sn in season_numbers:
                print(" -", sn)
            while True:
                season_choice_raw = input("Enter Season number: ").strip()
                if season_choice_raw.isdigit() and int(season_choice_raw) in season_numbers:
                    season_choice = int(season_choice_raw)
                    break
                print("Enter a valid season number.")

            season_info = fetch_season_details(parsed_id, season_choice)
            ep_count = len(season_info.get("episodes", [])) or "-"
            season_air_date = season_info.get("air_date") or "-"
            try:
                rd = datetime.strptime(season_air_date, "%Y-%m-%d")
                release_fmt = rd.strftime("%b %d, %Y")
            except:
                release_fmt = season_air_date

            rating = tv.get("vote_average")
            rating_text = f"{rating}/10 (TMDB)" if rating else "TMDB"
            genres = format_genres(tv.get("genres", []))
            qual_sel = choose("Select Quality:", ["SD", "HD", "FHD"])
            quality_text = ["SD","HD","FHD"][qual_sel-1]

            status_text = detect_status(tv, season_info)

            output = []
            output.append(f"🎬 Series Title: {title}")
            output.append("╭──────────────────────")
            output.append(f"├ 📝 Season - {season_choice}")
            output.append(f"├ 📅 Release - {release_fmt}")
            output.append(f"├ 🏷️ Status - {status_text}")
            output.append(f"├ ⭐ Ratings - {rating_text}")
            output.append(f"├ 📺 Episodes - {ep_count}")
            output.append(f"├ 🎵 Audio - Dual | {audio_text} #Official")
            output.append(f"├ 📼 Quality - {quality_text}")
            output.append(f"├ 🎭 Genres - {genres}")
            output.append(f"├ 🧩 [AD Skip](https://telegra.ph/How-to-Skip-Ads-and-Download-Easily-04-04) | [Download Tutorial](https://telegra.ph/How-to-Download-from-GDFLIX-Fast--Direct-Links-04-04)")
            output.append("╰──────────────────────")
            output.append("╭──────────────────────")
            output.append("├ 📢 Backup Channel & Info Bot:")
            output.append("├ 📌 [Channel](https://t.me/+2jrpUqXgr-hmOWM1) | [Bot](http://t.me/othersottinfobot)")
            output.append("╰──────────────────────")
            print("\n\nFinal Template (copy manually):\n")
            print("\n".join(output))

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
