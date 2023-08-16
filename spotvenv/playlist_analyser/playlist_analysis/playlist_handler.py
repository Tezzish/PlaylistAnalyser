from .playlist import Playlist
import base64
import dotenv
import os
import requests

class PlaylistHandler:

    def get_playlist_id_from_link(self, playlist_link):
        # https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M?si=1f3c8c5b0e7f4d4c
        # https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M
        # 37i9dQZF1DXcBWIGoYBM5M
        # 0th index is the playlist id
        return playlist_link.split('/')[-1].split('?')[0]

    def get_playlist(self, playlist_link):
        access_token = self.get_access_token()
        headers = {
            "Authorization": f"Bearer {access_token}"
        }

        # Make the request to the Spotify API
        response = requests.get(f"https://api.spotify.com/v1/playlists/{self.get_playlist_id_from_link(playlist_link)}", 
                                headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
            #return the tracks of the playlist
            return Playlist(response.json()['id'], response.json()['external_urls']['spotify'], response.json()['name'], response.json()['description'], response.json()['owner']['display_name'], response.json()['images'][0]['url'], response.json()['tracks']['items'])
        else:
            print(f"Error: {response.status_code} - {response.text}")

    
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
            data = response.json()
            return data['access_token']
        else:
            raise Exception('Failed to get access token from Spotify API')
        
