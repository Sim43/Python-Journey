import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

my_date = input("Which year do you want to travel to? Type the date in the format YYYY-MM-DD: ")
year = my_date[:4]

url = f"https://www.billboard.com/charts/hot-100/{my_date}/"
response = requests.get(url=url)
billboard_page = response.text
soup = BeautifulSoup(billboard_page, "html.parser")
songs = [{song.getText().strip()} for song in soup.select(".o-chart-results-list__item h3")]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-public",
        redirect_uri="http://example.com",
        client_id="087878a572d74dd7b731754430d0905c",
        client_secret="4dc4848cac6d4b5da9828774373efd87",
        show_dialog=True,
        cache_path="token.txt",
        username="Fury", 
        )
    )
user_id = sp.current_user()["id"]
playlist_name = f'{my_date} Billboard 100'  
playlist = sp.user_playlist_create(user_id, name=playlist_name)
playlist_id = playlist["id"]

song_uris = []
for song in songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
        
sp.playlist_add_items(playlist_id=playlist_id, items=song_uris)