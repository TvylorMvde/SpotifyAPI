
import requests
import json
import time
from config import (
    TOKEN,
    USER_ID,
    ARTIST_ID,
    MARKET,
    PLAYLIST_INFO)

# ENDPOINTS:
# Playlist endpoint
playlist_url = f"https://api.spotify.com/v1/users/{USER_ID}/playlists"

# Artist endpoint
artist_url = f"https://api.spotify.com/v1/artists/{ARTIST_ID}"

# Top tracks endpoint
toptracks_url = f"https://api.spotify.com/v1/artists/{ARTIST_ID}/top-tracks?market={MARKET}"

# Authorization headers
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": f"Bearer {TOKEN}"}


def get_playlist(url, headers):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(e)
    return response.json()


def get_artist(url, headers):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(e)
    return response.json()


def get_artist_name(url, headers):
    data = get_artist(url, headers)
    return data['name']


def get_top_tracks(url, headers):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(e)
    return response.json()['tracks']


def get_top_tracks_uris(url, headers):
    uris = []
    tracks = get_top_tracks(url, headers)
    for track in tracks:
        uris.append(track['uri'])
    return uris


def create_playlist(url, headers, playlist_info):
    playlist_data = json.dumps(playlist_info)
    try:
        response = requests.post(url, data=playlist_data, headers=headers)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(e)
    return response.json()['id']


def add_tracks_to_playlist(playlist_id, toptracks_url, headers):
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
    tracks = json.dumps({
        "uris": get_top_tracks_uris(toptracks_url, headers)
    })
    try:
        response = requests.post(url, data=tracks, headers=headers)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(e)
    return None


if __name__ == "__main__":
    artist_name = get_artist_name(artist_url, headers)
    print(f"Creating playlist with {artist_name}'s top tracks...")
    time.sleep(1)
    playlist_id = create_playlist(playlist_url, headers, PLAYLIST_INFO)
    print("Playlist created successfully.")
    time.sleep(1)
    print(f"Adding songs to playlist...")
    time.sleep(2)
    add_tracks_to_playlist(playlist_id, toptracks_url, headers)
    print("Done.")

