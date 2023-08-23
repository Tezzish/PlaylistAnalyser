import base64
import html
import json
import os

import dotenv
import pandas as pd
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

        # Check if the request was successful
        if response.status_code == 200:
            # html escape the response
            response_text = html.unescape(response.text)
            # convert the response to a JSON object
            response_json = json.loads(response_text)
            return response_json
        
        else:
            print(f"Error: {response.status_code} - {response.text}")

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
                features[item['id']] = item
            return features     
        else:
            print(f"Error: {response.status_code} - {response.text}")
    
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
        
    def get_playlist(self, playlist_link):
        """
        Returns the playlist object for the given playlist link.

        Parameters:
        playlist_link (str): The Spotify playlist link.

        Returns:
        Playlist: The Playlist object.
        """
        # if the playlist is in the database, return that
        playlist_model = PlaylistModel.objects.filter(id=self.get_playlist_id_from_link(playlist_link))
        if playlist_model.exists():
            return self.get_playlist_from_db(self.get_playlist_id_from_link(playlist_link))
        
        #get the playlist from the api
        playlist_json = self.get_playlist_from_url(playlist_link)
        
        #maps the songs to song objects
        mapped_songs, song_models = self.map_songs_to_song_objects(list(playlist_json['tracks']['items']))

        #get avg attributes of the playlist
        avg_attributes = self.get_avg_attributes(mapped_songs)

        #create playlist object
        playlist_obj = Playlist(
            playlist_json['id'],
            playlist_json['external_urls']['spotify'],
            playlist_json['name'],
            playlist_json['description'],
            playlist_json['owner']['display_name'],
            playlist_json['images'][0]['url'],
            mapped_songs,
            avg_attributes['avg_energy'],
            avg_attributes['avg_danceability'],
            avg_attributes['avg_acousticness'],
            avg_attributes['avg_valence'],
            avg_attributes['avg_loudness'],
            avg_attributes['avg_tempo'],
            avg_attributes['avg_duration']
        )

        self.save_playlist_to_db(playlist_obj, avg_attributes, song_models)

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
    
    def get_avg_attributes(self, songs):
        """
        Returns a dictionary containing the average audio features of the given list of songs.

        Parameters:
        songs (list): The list of songs to be analyzed.

        Returns:
        dict: A dictionary containing the average audio features.
        """
        #make pandas df from dictionary
        df = pd.DataFrame([song.__dict__ for song in songs])

        #remove the underscores from the column names
        df.columns = df.columns.str.replace('_', '')

        avg_energy = df['energy'].mean()
        avg_danceability = df['danceability'].mean()
        avg_acousticness = df['acousticness'].mean()
        avg_valence = df['valence'].mean()
        avg_loudness = df['loudness'].mean()
        avg_tempo = df['tempo'].mean()
        avg_duration = df['duration'].mean()

        return {
            'avg_energy': avg_energy,
            'avg_danceability': avg_danceability,
            'avg_acousticness': avg_acousticness,
            'avg_valence': avg_valence,
            'avg_loudness': avg_loudness,
            'avg_tempo': avg_tempo,
            'avg_duration': avg_duration
        }
    
    def get_all_playlists(self):
        return PlaylistModel.objects.all()
    
    def get_playlist_from_db(self, playlist_id):
        playlist_model = PlaylistModel.objects.get(id=playlist_id)
        songs = playlist_model.songs.all()

        playlist_obj = Playlist(
            playlist_model.id,
            playlist_model.url,
            playlist_model.name,
            playlist_model.description,
            playlist_model.author,
            playlist_model.thumbnail,
            songs,
            playlist_model.avg_energy,
            playlist_model.avg_danceability,
            playlist_model.avg_acousticness,
            playlist_model.avg_valence,
            playlist_model.avg_loudness,
            playlist_model.avg_tempo,
            playlist_model.avg_duration
        )

        return playlist_obj
    
    def save_playlist_to_db(self, playlist_obj, avg_attributes, song_models):
        
        #save as playlist model
        playlist_model = PlaylistModel(
            id = playlist_obj.id,
            url = playlist_obj.url,
            name = playlist_obj.name,
            description = playlist_obj.description,
            author = playlist_obj.author,
            thumbnail = playlist_obj.thumbnail,
            avg_energy = avg_attributes['avg_energy'],
            avg_danceability = avg_attributes['avg_danceability'],
            avg_acousticness = avg_attributes['avg_acousticness'],
            avg_valence = avg_attributes['avg_valence'],
            avg_loudness = avg_attributes['avg_loudness'],
            avg_tempo = avg_attributes['avg_tempo'],
            avg_duration = avg_attributes['avg_duration']
        )

        playlist_model.save()
        playlist_model.songs.set(song_models)
        print("saved")