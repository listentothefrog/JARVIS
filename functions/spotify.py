import os
from dotenv import find_dotenv, load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
SPOTIFY_CLIENT = os.getenv('SPOTIFY_CLIENT')
SPOTIFY_SECRET = os.getenv('SPOTIFY_SECRET')

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=SPOTIFY_CLIENT,
                                                           client_secret=SPOTIFY_SECRET))

results = sp.search(q='playboi carti', limit=20)
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'])
    
    