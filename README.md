## How to run 
### 1. Clone the repository
```
git clone https://github.com/TvylorMvde/SpotifyAPI.git
```
### 2. Install requests
```
pip install requests
```
### 3. Edit **config.py**
```
TOKEN = "Your Token"
USER_ID = "Your Spotify ID"
ARTIST_ID = "Artist ID"
MARKET = "US"
PLAYLIST_INFO = {
    "name": "Your playlist name",
    "description": "Your playlist description",
    "public": False
}
```
### 4. Run the script
```
python spotify.py