from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import PrettyPrinter
import spotipy.util as util
import sys
from datetime import datetime

pp = PrettyPrinter(indent=4)

date = input("Which year do you want to go to? The data should be formatted YYYY-MM-DD: ")

response = requests.get("https://www.billboard.com/charts/hot-100/" + date)

soup = BeautifulSoup(response.text, 'html.parser')
song_titles = soup.find_all(name='h3', class_='c-title')


first_songs = []
for song in song_titles:
    first_songs.append(song.getText().strip())

songs2 = []
for num in range(7, len(first_songs), 4):
    songs2.append(first_songs[num])

songs = [songs2[num] for num in range(0, 100)]
# pp.pprint(songs)



CLIENT_ID = 'ce617713aea7424abbbbfc76b7f7dc0b'
CLIENT_SECRET = '58ac61ba030f4afa89f2d7f77627b55b'



sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri="https://example.com",
    scope="playlist-modify-private",
    show_dialog=True,
    cache_path="token.txt",
    )
)

user = sp.current_user()["id"]
print(user)

songs_in_spotify = 0
songs_not_in_spotify = 0

spotify_song_names = []
spotify_song_uris = []
year = date.split('-')[0]
for song in songs:
    result = sp.search(q=f'track: {song} year: {year}', type='track')
    # print(result)
    
    try:
        spotify_song_names.append(result['tracks']['items'][0]['name'])
        spotify_song_uris.append(result['tracks']['items'][0]['uri'].split(':')[-1])
        songs_in_spotify += 1
    except:
        # print('Not in Spotify')
        songs_not_in_spotify += 1

# pp.pprint(spotify_song_names)
# pp.pprint(spotify_song_uris)
print(songs_in_spotify)
print(songs_not_in_spotify)

# with open('billboard.txt', mode='w') as d:
#     for song in songs:
#         d.write('%s\n' % song)

# with open('spotify.txt', mode='w') as d:
#     for song in spotify_song_names:
#         d.write('%s\n' % song)

# token = util.prompt_for_user_token(user, scope="user-library-read <etc>")

now = datetime.now().strftime("%Y-%m-%d")
if date == '':
    date = now

#Creating a new private playlist in Spotify
p = sp.user_playlist_create(user=user, name=f"{date} Billboard 100", public=False,collaborative=False, description="Test")

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id= p['id'], items=spotify_song_uris)