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

## Attributes:
- id: str
- url: str
- title: str
- description: str
- thumbnail: str
- songs: list

## Methods:
- get_id()
- get_url()
- get_title()
- get_description()
- get_thumbnail()
- get_songs()

## Description:
This class represents a playlist. It contains all the information about a playlist that is needed for the analysis. The attributes are the playlist's id, url, title, description, thumbnail and songs. The methods are getters for all the attributes. The playlist class is used in the playlist_analyser class.

## Example:
```python
playlist = Playlist(id, url, title, description, thumbnail, songs)
```