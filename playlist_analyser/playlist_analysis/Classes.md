# Song 

## Attributes:
- id: str
- url: str
- title: str
- artist: str
- album: str
- thumbnail: str
- duration: int
- energy: float
- danceability: float
- valence: float
- tempo: float
- loudness: float
- acousticness: float

## Methods:
- get_id()
- get_url()
- get_title()
- get_artist()
- get_album()
- get_thumbnail()
- get_duration()
- get_energy()
- get_danceability()
- get_valence()

## Description:
This class represents a song. It contains all the information about a song that is needed for the analysis. The attributes are the song's id, url, title, artist, album, thumbnail, duration, energy, danceability, valence, tempo and loudness. The methods are getters for all the attributes. The song class is used in the playlist class.

## Example:
```python
song = Song(id, url, title, artist, album, thumbnail, duration, energy, danceability, valence, tempo, loudness, acousticness)
```
# Playlist

    <!-- def __init__(self, id, url, name, description, author, thumbnail, songs, avg_energy, avg_danceability, avg_acousticness, avg_valence, avg_loudness, avg_tempo, avg_duration):
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
        self._avg_duration = avg_duration -->

## Attributes:
- id: str
- url: str
- name: str
- description: str
- author: str
- thumbnail: str
- songs: list
- avg_energy: float
- avg_danceability: float
- avg_acousticness: float
- avg_valence: float
- avg_loudness: float
- avg_tempo: float
- avg_duration: float

## Methods:
- get_id()
- get_url()
- get_name()
- get_description()
- get_author()
- get_thumbnail()
- get_songs()
- get_avg_energy()
- get_avg_danceability()
- get_avg_acousticness()
- get_avg_valence()
- get_avg_loudness()
- get_avg_tempo()
- get_avg_duration()
- get_avg_attributes()

## Description:
This class represents a playlist. It contains all the information about a playlist that is needed for the analysis. The attributes are the playlist's id, url, name, description, author, thumbnail, songs, avg_energy, avg_danceability, avg_acousticness, avg_valence, avg_loudness, avg_tempo and avg_duration. The methods are getters for all the attributes. The playlist class is used in the playlist_handler class.

## Example:
```python
playlist = Playlist(id, url, name, description, author, thumbnail, songs, avg_energy, avg_danceability, avg_acousticness, avg_valence, avg_loudness, avg_tempo, avg_duration)
```

