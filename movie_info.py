import requests
import re
import sys
import os

# TMDB API Key
API_KEY = "YOUR_API_KEY"

# Function to extract movie ID from TMDB link
def extract_movie_id(url):
    match = re.search(r'/movie/(\d+)', url)
    if match:
        return match.group(1)
    else:
        return None

# Function to fetch movie details from TMDB API
def fetch_movie_details(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Function to format runtime from minutes to h m
def format_runtime(minutes):
    if minutes is None or minutes == 0:
        return "N/A"
    hours = minutes // 60
    mins = minutes % 60
    return f"{hours}h {mins}m" if mins > 0 else f"{hours}h"

# Main function
def main():
    # Ask for TMDB link
    tmdb_link = input("Enter the TMDB movie link: ").strip()
    
    # Extract movie ID
    movie_id = extract_movie_id(tmdb_link)
    if not movie_id:
        print("Invalid TMDB link. It should be like https://www.themoviedb.org/movie/12345-movie-name")
        sys.exit(1)
    
    # Fetch details
    details = fetch_movie_details(movie_id)
    if not details:
        print("Failed to fetch movie details. Check the link or API key.")
        sys.exit(1)
    
    # Extract required info
    title = details.get('title', 'N/A')
    release_date = details.get('release_date', '')
    year = release_date.split('-')[0] if release_date else 'N/A'
    runtime_min = details.get('runtime')
    runtime = format_runtime(runtime_min)
    genres_list = [g['name'] for g in details.get('genres', [])]
    genre = ', '.join(genres_list[:2]) if genres_list else 'N/A'
    rating = details.get('vote_average', 'N/A')
    if rating != 'N/A':
        rating = f"{rating}/10 (TMDB)"
    
    # Ask for format
    print("\nSelect format:")
    print("1. MP4")
    print("2. MKV")
    print("3. AVI")
    print("4. MOV")
    print("5. WMV")
    format_choice = input("Enter number (1-5): ").strip()
    formats = {
        '1': "MP4",
        '2': "MKV",
        '3': "AVI",
        '4': "MOV",
        '5': "WMV"
    }
    format_ = formats.get(format_choice, "MKV")  # Default to MKV if invalid
    
    # Ask for quality
    print("\nSelect quality:")
    print("1. 480P SD")
    print("2. 720P HD")
    print("3. 1080P FHD")
    quality_choice = input("Enter number (1-3): ").strip()
    qualities = {
        '1': "480P SD",
        '2': "720P HD",
        '3': "1080P FHD"
    }
    quality = qualities.get(quality_choice, "1080P FHD")  # Default to 1080P FHD if invalid
    
    # Build the formatted text
    formatted_text = f"""╭─────────────────────
│ 🎬  Title     : {title}
│ 📅  Year      : {year}
│ 📺  Quality   : {quality}
│ 💽  Format    : {format_}
│ ⏱️  Runtime   : {runtime}
│ 🎭  Genre     : {genre}
│ ⭐ Rating    : {rating}
╰─────────────────────"""
    
    # Print the formatted text
    print("\nGenerated Format:\n")
    print(formatted_text)
    print("\nYou can manually copy the above text.")

if __name__ == "__main__":
    main()
