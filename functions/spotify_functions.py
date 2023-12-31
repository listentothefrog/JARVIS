import json
import os
from pprint import pprint
from dotenv import load_dotenv, find_dotenv
import spotipy
from spotipy import SpotifyOAuth
from AppOpener import open, close
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
    try: 
        
        results = sp.search(q=song, type="track")
        if len(results['tracks']['items']) > 0:
            first_track = results['tracks']['items'][0]
            artist = first_track['artists'][0]['name']
            track_uri = [first_track['uri']]
            device = sp.current_playback()
            device_name = device["device"]["name"]
            await user.send(f"Playing {first_track['name']} by {artist} on the device: {device_name}")
            await user.send(first_track['external_urls']['spotify'])
            sp.start_playback(uris=track_uri, position_ms=0, device_id=device_id)
            
        else:
            await user.send("No matching tracks found.")
    except ConnectionError: 
        await user.send("Couldn't connect with spotify")
        close("Spotify")
        open("Spotify")
        sp.start_playback(uris=track_uri, position_ms=0, device_id=device_id)    
    except NameError: 
        await user.send("Cannot find your device id")
        close("Spotify")
        open("Spotify")
        sp.start_playback(uris=track_uri, position_ms=0, device_id=device_id)

async def pause_song(user):
    await user.send("Pausing track...") 
    await sp.pause_playback(device_id=device_id)
    
async def resume_song(user):
    try:  
        await user.send("Resuming song...")
        sp.start_playback()
    except spotipy.exceptions.SpotifyException as e: 
        if e.http_status == 404 and e.code == -1: 
            await user.send("I encoutered an error while connecting with spotify")
            close("Spotify")
            open("Spotify")
            sp.start_playback(device_id=device_id)
    

async def find_playlist(playlist):
    await sp.start_playback(device_id=device_id, context_uri=playlist, position_ms=0)

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
        await user.send("No track is currently playing.")

async def previous_track(user):
    await user.send("Sure playing the previous track...") 
    sp.previous_track(device_id=device_id)
    
async def get_current_track(user): 
    current_track = sp.current_playback()
    track_name = current_track["item"]["name"]
    artist_data = current_track["item"]["artists"]
    artist_names = [artist['name'] for artist in artist_data]
    artist_names_formatted = ', '.join(artist_names)
    track_url = current_track["item"]["external_urls"]["spotify"]
    await user.send(f"You are currently's listening to {track_name} by {artist_names_formatted}")
    await user.send(track_url)