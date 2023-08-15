import requests
import dotenv
import os

class Playlist:

    def __init__(self, url):

        # Load environment variables
        dotenv.load_dotenv()

        # Get client ID and secret
        self._client_id = os.getenv("CLIENT_ID")
        self._client_secret = os.getenv("CLIENT_SECRET")

        # Send a request to the API to get the authorization token
        self._token = self.get_token()

        # Get the information from the API
        self._url = url
        self.get_info()

    def get_info(self):
            
        # Get the playlist ID from the URL
        self._id = self.url.split("/")[-1]

        # Send a request to the API to get the playlist information
        response = requests.get(
            f"https://api.spotify.com/v1/playlists/{self.id}",
            headers = {
                "Authorization": f"Bearer {self._token}"
            }
        )

        # Get the playlist information
        self._name = response.json()["name"]
        self._description = response.json()["description"]
        self._author = response.json()["owner"]["display_name"]
        self._thumbnail = response.json()["images"][0]["url"]
        self._songs = response.json()["tracks"]["items"]

    def get_token(self):
            
        # Send a request to the API to get the authorization token
        response = requests.post(
            "https://accounts.spotify.com/api/token",
            data = {
                "grant_type": "client_credentials"
            },
            auth = (
                self._client_id,
                self._client_secret
            )
        )

        # Return the token
        return response.json()["access_token"]

    


    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._author = value

    @property
    def thumbnail(self):
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, value):
        self._thumbnail = value

    @property
    def songs(self):
        return self._songs

    @songs.setter
    def songs(self, value):
        self._songs = value

    @property
    def avg_energy(self):
        return self._avg_energy

    @avg_energy.setter
    def avg_energy(self, value):
        self._avg_energy = value

    @property
    def avg_danceability(self):
        return self._avg_danceability

    @avg_danceability.setter
    def avg_danceability(self, value):
        self._avg_danceability = value

    @property
    def avg_valence(self):
        return self._avg_valence

    @avg_valence.setter
    def avg_valence(self, value):
        self._avg_valence = value

    @property
    def avg_tempo(self):
        return self._avg_tempo

    @avg_tempo.setter
    def avg_tempo(self, value):
        self._avg_tempo = value

    @property
    def avg_loudness(self):
        return self._avg_loudness

    @avg_loudness.setter
    def avg_loudness(self, value):
        self._avg_loudness = value

    @property
    def avg_speechiness(self):
        return self._avg_speechiness

    @avg_speechiness.setter
    def avg_speechiness(self, value):
        self._avg_speechiness = value

    @property
    def avg_acousticness(self):
        return self._avg_acousticness

    @avg_acousticness.setter
    def avg_acousticness(self, value):
        self._avg_acousticness = value

    @property
    def avg_duration_ms(self):
        return self._avg_duration_ms

    @avg_duration_ms.setter
    def avg_duration_ms(self, value):
        self._avg_duration_ms = value

    