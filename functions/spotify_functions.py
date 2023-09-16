import os
from dotenv import load_dotenv, find_dotenv
import spotipy
from spotipy import SpotifyOAuth

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
CLIENT_ID = os.getenv('SPOTIFY_CLIENT')
CLIENT_SECRET = os.getenv('SPOTIFY_SECRET')
REDIRECT_URI = os.getenv('REDIRECT_URI')

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope='user-library-read'))

async def play_song(song, user): 
    results = sp.search(q=song, type="track")
    if len(results['tracks']['items']) > 0:
        first_track = results['tracks']['items'][0]
        await user.send(f"Playing {first_track['name']}..., by ".join(artist['name'] for artist in first_track['artists']))
        await user.send(first_track['external_urls']['spotify'])
    else:
        await user.send("No matching tracks found.")