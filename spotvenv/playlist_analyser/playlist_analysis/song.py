import requests
import dotenv
import os
import base64

class Song:

    def __init__(self, url):
        self.url = url
        
        # Get the song's ID, title, artist and album from the spotify api
        response = requests.get(f'https://api.spotify.com/v1/tracks/{self.get_song_id()}',
                                headers={
                                    'Authorization': f'Bearer {self.get_access_token()}'
                                })
        if response.status_code == 200:
            data = response.json()
            self.id = data['id']
            self.title = data['name']
            self.artist = data['artists'][0]['name']
            self.album = data['album']['name']
        else:
            raise Exception('Failed to get song information from Spotify API')

    def get_song_id(self):
        # Extract the song ID from the Spotify URL
        return self.url.split('/')[-1]

    def get_access_token(self):
        # Get the Client ID and Client Secret from the .env file
        dotenv.load_dotenv()

        client_id = os.getenv('CLIENT_ID')
        client_secret = os.getenv('CLIENT_SECRET')

        

       #puts the id and secret into the format asked for
        token = f"{client_id}:{client_secret}"
        tokenb64 = base64.b64encode(token.encode())

        #data field in request
        token_data = {
            "grant_type": "client_credentials"
        }

        #header field in request
        token_headers = {
            "Authorization": f"Basic {tokenb64.decode()}"
        }
        #gets bearer token
        response = requests.post("https://accounts.spotify.com/api/token", data=token_data, headers=token_headers)

        if response.status_code == 200:
            print("got access token")
            data = response.json()
            return data['access_token']
        else:
            raise Exception('Failed to get access token from Spotify API')
        
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def artist(self):
        return self._artist

    @artist.setter
    def artist(self, value):
        self._artist = value

    @property
    def album(self):
        return self._album

    @album.setter
    def album(self, value):
        self._album = value