import json
import os
import pprint
from dotenv import load_dotenv, find_dotenv
import spotipy
from spotipy import SpotifyOAuth
from AppOpener import open
import time

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
    
async def resume_song(): 
    sp.start_playback()

async def find_playlist(playlist):
    sp.start_playback(device_id=device_id, context_uri=playlist, position_ms=0)

async def skip_track(user): 
    sp.next_track(device_id=device_id)

    time.sleep(1)
    
    current_song = sp.current_playback()

    if current_song is not None and "item" in current_song:
        track_name = current_song["item"]["name"]
        track_url = current_song["item"]["external_urls"]["spotify"]
        album_name = current_song["item"]["album"]["name"]
        await user.send(f"Now playing: {track_name} on {album_name}")
        await user.send(track_url)
    else:
        print("No track is currently playing.")
    