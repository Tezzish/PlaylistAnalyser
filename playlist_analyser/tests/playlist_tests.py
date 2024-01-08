# from playlist_analysis.playlist_handler import PlaylistHandler
from playlist_analysis.playlist import Playlist
from playlist_analysis.song import Song
import pytest


@pytest.fixture
def playlist():
    song1 = Song(
        id=1,
        url="https://example.com/song1",
        title="Song 1",
        artist="Artist 1",
        album="Album 1",
        thumbnail="https://example.com/thumbnail.jpg",
        duration=180000,
        danceability=0.5,
        energy=0.8,
        loudness=-5.2,
        acousticness=0.5,
        valence=0.6,
        tempo=120,
    )

    song2 = Song(
        id=2,
        url="https://example.com/song2",
        title="Song 2",
        artist="Artist 1",
        album="Album 1",
        thumbnail="https://example.com/thumbnail.jpg",
        duration=180000,
        danceability=0.7,
        energy=1.0,
        loudness=-5.2,
        acousticness=0.3,
        valence=0.6,
        tempo=120,
    )

    playlist = Playlist(
        id=1,
        url="https://example.com/playlist",
        name="My Playlist",
        description="A sample playlist",
        author="John Doe",
        thumbnail="https://example.com/thumbnail.jpg",
        songs=[song1, song2],
    )
    yield playlist


# ------------------ Get_Avg_Of_Attribute Tests ------------------ #
def test_get_avg_attributes(playlist):
    avg_attributes = playlist.get_avg_attributes()

    assert avg_attributes['Energy'] == 90
    assert avg_attributes['Danceability'] == 60
    assert avg_attributes['Acousticness'] == 40
    assert avg_attributes['Valence'] == 60
    assert avg_attributes['Loudness'] == -5.2
    assert avg_attributes['Tempo'] == 120
    assert avg_attributes['Duration'] == 180


# ------------------ Get_Max_Of_Attribute Tests ------------------ #
def test_get_max_attributes(playlist):
    max_attributes = playlist.get_max_attributes()

    assert max_attributes['Energy'][0] == 100
    assert max_attributes['Danceability'][0] == 70
    assert max_attributes['Acousticness'][0] == 50
    assert max_attributes['Valence'][0] == 60
    assert max_attributes['Loudness'][0] == -5.2
    assert max_attributes['Tempo'][0] == 120
    assert max_attributes['Duration'][0] == 180


# ------------------ Constructor tests ------------------ #
# tests the constructor
def test_constructor():
    playlist = Playlist(
        id=1,
        url="https://example.com/playlist",
        name="My Playlist",
        description="A sample playlist",
        author="John Doe",
        thumbnail="https://example.com/thumbnail.jpg",
        songs=[],
    )

    assert playlist.id == 1
    assert playlist.url == "https://example.com/playlist"
    assert playlist.name == "My Playlist"
    assert playlist.description == "A sample playlist"
    assert playlist.author == "John Doe"
    assert playlist.thumbnail == "https://example.com/thumbnail.jpg"
    assert playlist.songs == []


# ------------------ to string tests ------------------ #
# tests the to string method
def test_to_string(playlist):
    playlist_string = playlist.__str__()
    assert playlist_string == (
        "Playlist(id=1, url=https://example.com/playlist, "
        "name=My Playlist, description=A sample playlist, "
        "author=John Doe, thumbnail=https://example.com/thumbnail.jpg, "
        "songs=['Song 1', 'Song 2']"
    )


# ------------------ Dict tests ------------------ #
# tests the to dict method
def test_dict(playlist):
    dict = playlist.__dict__()
    expected_keys = [
        'id', 'url', 'name', 'description', 'author', 'thumbnail', 'songs'
    ]
    assert list(dict.keys()) == expected_keys
    assert dict['id'] == 1
    assert dict['url'] == "https://example.com/playlist"
    assert dict['name'] == "My Playlist"
    assert dict['description'] == "A sample playlist"
    assert dict['author'] == "John Doe"
    assert dict['thumbnail'] == "https://example.com/thumbnail.jpg"

    songs = playlist.songs
    for song in dict['songs']:
        assert song in songs
