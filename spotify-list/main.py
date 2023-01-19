from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth


year = input(
    "Which year do you want to travel to? Type the date in the format YYYY-MM-DD:")
response = requests.get(f" https://www.billboard.com/charts/hot-100/{year}")
chart_page = response.text

soup = BeautifulSoup(chart_page, "html.parser")
songs = [x.get_text().strip()
         for x in soup.find_all("h3", attrs={'class': 'a-no-trucate'})]
clientid = "b3a11d94030647d5847fb140f7104db1"
secret = "a06ea6649aed47e9a81ee801ddde72c7"
uri = "http://example.com/callback/"


spotty = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com/callback/",
        client_id=clientid,
        client_secret=secret,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = spotty.current_user()["id"]
song_uri = []
for song in songs:
    result = spotty.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uri.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
