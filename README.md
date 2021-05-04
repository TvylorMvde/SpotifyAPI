## How to run 
### 1. Clone the repository
```
git clone https://github.com/TvylorMvde/SpotifyAPI.git
```
### 2. Install requests
```
pip install requests
```
### 3. Generate OAuth Token
- Go to [Spotify for Developers](https://developer.spotify.com/console/get-artist-top-tracks/)
- Fill in the mandatory fields (*artist* *id* and *market*)
- Click the **Get Token** button and check the boxes: 
    - *user-read-private*
    - *playlist-read-private*
    - *playlist-modify-private*
- Click the **Request Token** button.

### 4. Edit **config.py**
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
### 5. Run the script
```
python spotify.py