import requests
from bs4 import BeautifulSoup
import spotify
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth

ACCESS={"access_token": "BQDfknVwYz3ij_Np7OiXEzrWhwGOFpjkCg6VZ-4aMPrSnqLZBzjM7Chks-D-ign4sCKF-aYmhJnbuurOrrB2eH0b1wKV3LGT6Z-q8FUB0pY_Kc1GcSJE-xQUQfz762hgH-wfDPuJVpIF2EI34k0LxsMIxACvYhrFZty5S09zlJ5x7myey1Mb1yXs7V7vDX_ibnt5wexSchv8q0P5y6OgKRrGeiRF7ZR2XzvO2gXHFhKE59AfKlOQE4f0M8rCy6P4ySJ6LoZo1kcPHg", "token_type": "Bearer", "expires_in": 3600, "refresh_token": "AQBgTUeOMuY_NvcCm-bWYmeiznsdMKx220IdK7kp5CGpqa1la5Va8g_f084Ja7OQdQuVbvtZjiRZZb7sjh6HWx2p-gv20Tcpl_2NwQOquSr11Zm5D8jEAIQHHZKC-AJ5tEE", "scope": "playlist-modify-private", "expires_at": 1755365546}
ACCESS_TOKEN2=ACCESS.get('access_token')
print(ACCESS_TOKEN2)

CLIENT_ID='14ae1833f93343c98963fa2472f9e254'
CLIENT_SECRET='3aa59e38458a438394fd398b918f39dc'
ACCESS_TOKEN=''



create_playlist_url=f'https://api.spotify.com/v1/users/{CLIENT_ID}/playlists'

ARTIST_ID='3m49WVMU4zCkaVEKb8kFW7?si=wdj5ig80RSW9Y8Pil8q8Cw'
ARTIST_URL=f'https://api.spotify.com/v1/artists/{ARTIST_ID}'
SPOTIFY_URL="https://accounts.spotify.com/api/token"
headers_token={"Content-Type": "application/x-www-form-urlencoded"}
body={"grant_type":"client_credentials",
     "client_id":CLIENT_ID,
    "client_secret":CLIENT_SECRET}


# input_date='2025-08-09'
# # input_date=input('what year you would like to travel to in YYYY-MM-DD format...?')
# songs_url=f'https://www.billboard.com/charts/hot-100/{input_date}/'
# response=requests.get(songs_url)
# data=response.text
# # print(data)
# soup=BeautifulSoup(data,'html.parser')
# divs=soup.select('.chart-results-list .o-chart-results-list-row-container')
# song_titles_list=[div.select('.c-title')[0].get_text() for div in divs]
# song_titles=[item.strip() for item in song_titles_list]
#
# print(song_titles)


def get_access_token():
    global ACCESS_TOKEN
    response_access=requests.post(SPOTIFY_URL,headers=headers_token,data=body)
    ACCESS_TOKEN=response_access.json().get('access_token')
    print('Access token fetched')

get_access_token()

# GET ARTIST DATA
header_artist={"Authorization": f"Bearer {ACCESS_TOKEN}"}
# response_artist=requests.get(ARTIST_URL,headers=header_artist)
# print(response_artist.json())

# # CREATE A PLAYLIST
sp = Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri='https://example.com/callbacks',
    scope="playlist-modify-private"
))

# Example: Get current user’s saved tracks
results = sp.current_user_saved_tracks(limit=10)
for idx, item in enumerate(results['items']):
    track = item['track']
    print(f"{idx+1}: {track['artists'][0]['name']} - {track['name']}")


# GET USER ID

# Normally you'd get this token from Spotify's OAuth flow

url = "https://api.spotify.com/v1/me"
headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN2}"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    user_data = response.json()
    MY_TOKEN=user_data.get('id')
    print(user_data)  # contains display_name, email, id, country, product, etc.
else:
    print("Error:", response.status_code, response.text)

# GET SINGLE SONG
user_id = sp.current_user()["id"]
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
song_names = ["The list of song", "titles from your", "web scrape"]

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")