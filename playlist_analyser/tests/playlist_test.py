from playlist_analysis.playlist_handler import PlaylistHandler
import pytest


@pytest.fixture
def handler():
    yield PlaylistHandler()


# ------------------ Get_Avg_Of_Attribute Tests ------------------ #
@pytest.mark.django_db
def test_get_avg_attributes(handler):
    playlist_url = (
        "https://open.spotify.com/playlist/"
        "6cUbe8r2kP140bL0Z2HHXV?si=89cbce6452b84b10"
    )
    playlist = handler.get_playlist(playlist_url)
    avg_attributes = playlist.get_avg_attributes()

    assert avg_attributes['Energy'] == 77
    assert avg_attributes['Danceability'] == 46
    assert avg_attributes['Acousticness'] == 17
    assert avg_attributes['Valence'] == 39
    assert avg_attributes['Loudness'] == -5.86
    assert avg_attributes['Tempo'] == 131
    assert avg_attributes['Duration'] == 222


# ------------------ Get_Max_Of_Attribute Tests ------------------ #
@pytest.mark.django_db
def test_get_max_attributes(handler):
    playlist_url = (
        "https://open.spotify.com/playlist/"
        "6cUbe8r2kP140bL0Z2HHXV?si=89cbce6452b84b10"
    )
    playlist = handler.get_playlist(playlist_url)
    max_attributes = playlist.get_max_attributes()

    assert max_attributes['Energy'][0] == 98
    assert max_attributes['Danceability'][0] == 68
    assert max_attributes['Acousticness'][0] == 97
    assert max_attributes['Valence'][0] == 70
    assert max_attributes['Loudness'][0] == -2.58
    assert max_attributes['Tempo'][0] == 180
    assert max_attributes['Duration'][0] == 475
