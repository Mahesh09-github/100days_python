import requests
import spotipy
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth
spotify_URL = "https://api.spotify.com/v1/me/playlists"
time_period = input("Which year do you want to travel to? Type in this format YYYY")
URL = f"https://takemeback.to/songs/date/{time_period}/usa"
head = {
    "headers":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0"
}
client_id="12850484177e426fb22313d2dfd0a722"
client_secret="496677cd3900406084d2cef576d2a835"
# playlist = {
#     "name": "New Playlist",
#     "description": "New playlist description",
#     "public": False
# }
scope = "user-library-read"

response = requests.get(url=URL)
data = response.text


soup = BeautifulSoup(data,"html.parser")
songs = soup.find_all(name="span", itemprop="name")
links = soup.find_all("a",href=True)

song_list = []
link_list = []
for link in links:  # ensure href exists
    href = link["href"]
    if "youtube.com" in href or "youtu.be" in href:
        link_list.append(href)

for song in songs:
    text = song.getText()
    song_list.append(text)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri="https://example.org/callback",
    scope=scope
))
user_id = sp.current_user()["id"]
song_uris = []
for i in song_list:
    track_name = i
    query = f"track:{track_name} year:{time_period}"
    results = sp.search(q=query, type="track", limit=1)
    print(results)
    # for item in results["tracks"]["items"]:
    #     print(item["name"], "-", item["external_urls"]["spotify"])
    try:
        uri = results["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{i} doesn't exist in Spotify. Skipped.")
playlist = sp.user_playlist_create(user=user_id,name=f"{time_period}'s Top 10 Songs",public=False)
print(playlist)


sp.playlist_add_items(playlist_id=playlist["id"],items=song_uris)



