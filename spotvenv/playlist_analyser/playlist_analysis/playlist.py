import requests
import dotenv
import os

class Playlist:

    def __init__(self, id, url, name, description, author, thumbnail, songs, avg_energy, avg_danceability, avg_acousticness, avg_valence, avg_loudness, avg_tempo, avg_duration):
        self._id = id
        self._url = url
        self._name = name
        self._description = description
        self._author = author
        self._thumbnail = thumbnail
        self._songs = songs
        self._avg_energy = avg_energy
        self._avg_danceability = avg_danceability
        self._avg_acousticness = avg_acousticness
        self._avg_valence = avg_valence
        self._avg_loudness = avg_loudness
        self._avg_tempo = avg_tempo
        self._avg_duration = avg_duration

    def __str__(self):
        #return all attributes
        return f"Playlist(id={self._id}, url={self._url}, name={self._name}, description={self._description}, author={self._author}, thumbnail={self._thumbnail}, songs={self._songs}, avg_energy={self._avg_energy}, avg_danceability={self._avg_danceability}, avg_acousticness={self._avg_acousticness}, avg_valence={self._avg_valence}, avg_loudness={self._avg_loudness}, avg_tempo={self._avg_tempo}, avg_duration={self._avg_duration})"
    
    def __dict__(self):
        return {
            'id': self._id,
            'url': self._url,
            'name': self._name,
            'description': self._description,
            'author': self._author,
            'thumbnail': self._thumbnail,
            'songs': self._songs,
            'avg_energy': self._avg_energy,
            'avg_danceability': self._avg_danceability,
            'avg_acousticness': self._avg_acousticness,
            'avg_valence': self._avg_valence,
            'avg_loudness': self._avg_loudness,
            'avg_tempo': self._avg_tempo,
            'avg_duration': self._avg_duration
        }

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
    def avg_acousticness(self):
        return self._avg_acousticness
    
    @avg_acousticness.setter
    def avg_acousticness(self, value):
        self._avg_acousticness = value

    @property
    def avg_valence(self):
        return self._avg_valence
    
    @avg_valence.setter
    def avg_valence(self, value):
        self._avg_valence = value
    
    @property
    def avg_loudness(self):
        return self._avg_loudness
    
    @avg_loudness.setter
    def avg_loudness(self, value):
        self._avg_loudness = value

    @property
    def avg_tempo(self):
        return self._avg_tempo
    
    @avg_tempo.setter
    def avg_tempo(self, value):
        self._avg_tempo = value

    @property
    def avg_duration(self):
        return self._avg_duration
    
    @avg_duration.setter
    def avg_duration(self, value):
        self._avg_duration = value

    def get_avg_attributes(self):
        return {
            'Energy': round(self._avg_energy * 100, 2),
            'Danceability': round(self._avg_danceability * 100, 2),
            'Acousticness': round(self._avg_acousticness * 100, 2),
            'Valence': round(self._avg_valence * 100, 2),
            'Loudness': round(self._avg_loudness, 2),
            'Tempo': round(self._avg_tempo, 2),
            'Duration': round(self._avg_duration / 1000, 2)
        }