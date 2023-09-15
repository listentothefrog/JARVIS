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

def play_song(song): 
    results = sp.search(q=song, type="track")
    print(results)