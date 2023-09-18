import os
import pprint
from dotenv import load_dotenv, find_dotenv
import spotipy
from spotipy import SpotifyOAuth
from AppOpener import open

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
CLIENT_ID = os.getenv('SPOTIFY_CLIENT')
CLIENT_SECRET = os.getenv('SPOTIFY_SECRET')
REDIRECT_URI = os.getenv('REDIRECT_URI')

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope='user-library-read, user-read-playback-state, user-modify-playback-state, user-read-currently-playing, app-remote-control, streaming'))

try: 
    devices = sp.devices()
    device_id = devices['devices'][0]['id']
except IndexError: 
    open("Spotify")

async def play_song(song, user): 
    results = sp.search(q=song, type="track")
    if len(results['tracks']['items']) > 0:
        first_track = results['tracks']['items'][0]
        track_uri = [first_track['uri']]
        await user.send(f"Playing {first_track['name']}")
        await user.send(first_track['external_urls']['spotify'])
        sp.start_playback(uris=track_uri, position_ms=0, device_id=device_id)
    else:
        await user.send("No matching tracks found.")
        
async def pause_song(): 
    await sp.pause_playback(device_id=device_id)
