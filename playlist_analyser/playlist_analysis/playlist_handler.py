import base64
import html
import json
import os

import dotenv
import requests

from .models import Playlist as PlaylistModel
from .models import Song as SongModel
from .playlist import Playlist
from .song import Song


class PlaylistHandler:
    """
    A class that handles the analysis of Spotify playlists.

    Attributes:
    None

    Methods:
    get_playlist_id_from_link(playlist_link): Returns the playlist ID from the given playlist link.
    get_playlist_from_url(playlist_link): Returns the playlist JSON object from the Spotify API for the given playlist link.
    get_access_token(): Returns the access token required to make requests to the Spotify API.
    get_audio_features(song_id): Returns the audio features JSON object for the given song ID.
    save_song_to_db(song): Saves the given song object to the database.
    get_playlist(playlist_link): Returns the playlist object for the given playlist link.
    """
    
    def get_playlist_id_from_link(self, playlist_link):
        """
        Returns the playlist ID from the given playlist link.

        Parameters:
        playlist_link (str): The Spotify playlist link.

        Returns:
        str: The playlist ID.
        """
        return playlist_link.split('/')[-1].split('?')[0]
    
    def get_playlist_from_url(self, playlist_link):
        """
        Returns the playlist JSON object from the Spotify API for the given playlist link.

        Parameters:
        playlist_link (str): The Spotify playlist link.

        Returns:
        dict: The playlist JSON object.
        """
        access_token = self.get_access_token()
        headers = {
            "Authorization": f"Bearer {access_token}"
        }

        # Make the request to the Spotify API
        response = requests.get(f"https://api.spotify.com/v1/playlists/{self.get_playlist_id_from_link(playlist_link)}", 
                                headers=headers)
        
        
        
        # if playlist is private or 404, throw an error
        if response.status_code == 404 or json.loads(response.text)['public'] == 'false':
            raise Exception('Playlist unavailable or private')
        
        # Check if the request was successful
        elif response.status_code == 200:
            # html escape the response
            response_text = html.unescape(response.text)
            # convert the response to a JSON object
            response_json = json.loads(response_text)
            return response_json
        
        else:
            raise Exception('Failed to get playlist from Spotify API')

    def get_access_token(self):
        """
        Returns the access token required to make requests to the Spotify API.

        Returns:
        str: The access token.
        """
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
            print(f"Error: {response.status_code} - {response.text}")
            raise Exception('Failed to get access token from Spotify API')
        
    def get_audio_features(self, song_ids):
        """
        Returns the audio features JSON object for the given song ID.

        Parameters:
        song_id (str): The Spotify song ID.

        Returns:
        dict: The audio features JSON object.
        """
        #get the audio features of the song
        access_token = self.get_access_token()
        headers = {
            "Authorization": f"Bearer {access_token}"
        }

        # Make the request to the Spotify API using comma separated song ids
        response = requests.get(f"https://api.spotify.com/v1/audio-features?ids={','.join(song_ids)}",
                                headers=headers)
        
        # Check if the request was successful
        if response.status_code == 200:
            #return a dictionary of the song ids and the corresponding audio features
            features = {}
            for item in response.json()['audio_features']:
                if item == None:
                    continue
                features[item['id']] = item
            return features     
        else:
            print(f"Error: {response.status_code} - {response.text}")
            raise Exception('Failed to get audio features from Spotify API')
        
    def get_playlist(self, playlist_link):
        """
        Returns the playlist object for the given playlist link.

        Parameters:
        playlist_link (str): The Spotify playlist link.

        Returns:
        Playlist: The Playlist object.
        """
        playlist_json = self.get_playlist_from_url(playlist_link)
        # if the playlist is in the database and the playlist has the same songs as the one in the database, return the playlist from the database
        playlist_model = PlaylistModel.objects.filter(id=self.get_playlist_id_from_link(playlist_link))
        if playlist_model.exists():
            # for each track id in playlist_json, check if it exists in the playlist_model
            # if all of the songs are the same in the playlist_model, return the playlist_model, else continue
            playlist_model_songs = playlist_model[0].songs.values_list('id', flat=True)
            playlist_json_songs = [track['track']['id'] for track in playlist_json['tracks']['items']]

            if sorted(playlist_model_songs) == sorted(playlist_json_songs):
                return self.get_playlist_from_db(playlist_model[0].id)
            else:
                playlist_model.delete()

        #get the playlist from the api
        
        #maps the songs to song objects
        mapped_songs, song_models = self.map_songs_to_song_objects(list(playlist_json['tracks']['items']))

        #create playlist object
        playlist_obj = Playlist(
            playlist_json['id'],
            playlist_json['external_urls']['spotify'],
            playlist_json['name'],
            playlist_json['description'],
            playlist_json['owner']['display_name'],
            playlist_json['images'][0]['url'],
            mapped_songs,
        )

        self.save_playlist_to_db(playlist_obj, song_models)

        return playlist_obj
    
    def map_songs_to_song_objects(self, songs):
        """
        Maps the given list of songs to Song objects and saves them to the database.

        Parameters:
        songs (list): The list of songs to be mapped.

        Returns:
        tuple: A tuple containing the list of Song objects and the list of SongModel objects that were saved to the database.
        """

        song_models = []
        mapped_songs = []

        # get a set of the songs that don't exist in the database
        song_ids = list(map(lambda song: song['track']['id'], songs))
        song_ids_in_db = set(map(lambda song: song.id, SongModel.objects.filter(id__in=song_ids)))
        song_ids_not_in_db = set(song_ids) - song_ids_in_db

        # get the audio features for the songs not in the database using their ids
        audio_features = self.get_audio_features(song_ids_not_in_db)    

        for song in songs:
            if song['track']['id'] in song_ids_in_db:
                # get the song model from the database, and add it to the list
                song_model = SongModel.objects.get(id=song['track']['id'])
                song_models.append(song_model)
                # get the song object from the song model
                song_obj = Song(
                    song_model.id,
                    song_model.url,
                    song_model.name,
                    song_model.artist,
                    song_model.album,
                    song_model.thumbnail,
                    song_model.duration,
                    song_model.energy,
                    song_model.danceability,
                    song_model.valence,
                    song_model.tempo,
                    song_model.loudness,
                    song_model.acousticness
                )
                # add the song object to the list
                mapped_songs.append(song_obj)        
                continue
            else:
                if (song['track']['id'] not in audio_features):
                    continue
                song_obj = Song(
                    song['track']['id'],
                    song['track']['external_urls']['spotify'],
                    song['track']['name'],
                    song['track']['artists'][0]['name'],
                    song['track']['album']['name'],
                    song['track']['album']['images'][0]['url'],
                    song['track']['duration_ms'],
                    audio_features[song['track']['id']]['energy'],
                    audio_features[song['track']['id']]['danceability'],
                    audio_features[song['track']['id']]['valence'],
                    audio_features[song['track']['id']]['tempo'],
                    audio_features[song['track']['id']]['loudness'],
                    audio_features[song['track']['id']]['acousticness']
                )
                #save the song to the database
                song_model = self.save_song_to_db(song_obj)
                #add the song model to the list
                song_models.append(song_model)
            mapped_songs.append(song_obj)
        return mapped_songs, song_models
    
    def get_playlist_from_db(self, playlist_id):
        """
        Returns the playlist object for the given playlist id.

        Parameters:
        playlist_id (str): The Spotify playlist id.

        Returns:
        Playlist: The Playlist object.
        """
        playlist_model = PlaylistModel.objects.get(id=playlist_id)
        songs = playlist_model.songs.all()

        playlist_obj = Playlist(
            playlist_model.id,
            playlist_model.url,
            playlist_model.name,
            playlist_model.description,
            playlist_model.author,
            playlist_model.thumbnail,
            songs
        )

        return playlist_obj
    
    def save_playlist_to_db(self, playlist_obj, song_models):
        
        #save as playlist model
        playlist_model = PlaylistModel(
            id = playlist_obj.id,
            url = playlist_obj.url,
            name = playlist_obj.name,
            description = playlist_obj.description,
            author = playlist_obj.author,
            thumbnail = playlist_obj.thumbnail,
        )

        playlist_model.save()
        playlist_model.songs.set(song_models)

    def save_song_to_db(self, song):
        """
        Saves the given song object to the database.

        Parameters:
        song (Song): The Song object to be saved.

        Returns:
        SongModel: The SongModel object that was saved to the database.
        """
        song_model = SongModel(
            id=song.id,
            url=song.url,
            name=song.title,
            artist=song.artist,
            album=song.album,
            thumbnail=song.thumbnail,
            duration=song.duration,
            energy=song.energy,
            danceability=song.danceability,
            valence=song.valence,
            tempo=song.tempo,
            loudness=song.loudness,
            acousticness=song.acousticness
        )
        song_model.save()

        return song_model
        