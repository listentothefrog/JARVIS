import os
from dotenv import find_dotenv, load_dotenv
import spotipy
import webbrowser

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
SPOTIFY_CLIENT = os.getenv('SPOTIFY_CLIENT')
SPOTIFY_SECRET = os.getenv('SPOTIFY_SECRET')
SPOTIFY_REDIRECT_URI = os.getenv('REDIRECT_URI')

  
oauth_object = spotipy.SpotifyOAuth(SPOTIFY_CLIENT, SPOTIFY_SECRET, SPOTIFY_REDIRECT_URI)
token_dict = oauth_object.get_access_token()
token = token_dict['access_token']
spotifyObject = spotipy.Spotify(auth=token)
user_name = spotifyObject.current_user()
  

  
while True:
    print("Welcome to the project, " + user_name['display_name'])
    print("0 - Exit the console")
    print("1 - Search for a Song")
    user_input = int(input("Enter Your Choice: "))
    if user_input == 1:
        search_song = input("Enter the song name: ")
        results = spotifyObject.search(search_song, 1, 0, "track")
        songs_dict = results['tracks']
        song_items = songs_dict['items']
        song = song_items[0]['external_urls']['spotify']
        webbrowser.open(song)
        print('Song has opened in your browser.')
    elif user_input == 0:
        print("Good Bye, Have a great day!")
        break
    else:
        print("Please enter valid user-input.")