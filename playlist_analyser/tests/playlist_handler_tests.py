from playlist_analysis.playlist_handler import PlaylistHandler
import html
import pytest


# Tests the playlist handler class
@pytest.fixture
def handler():

    handler = PlaylistHandler()

    yield handler


# ------------------ get_playlist_from_spotify Tests ------------------ #
# simple test to get a playlist from a url
# returns the json of the playlist
def test_get_playlist_from_spotify(handler):
    # gets a json of the playlist
    playlist_url = (
        "6cUbe8r2kP140bL0Z2HHXV"
    )
    playlist = handler.get_playlist_from_spotify(playlist_url)
    assert playlist is not None
    assert playlist['name'] == "Fleece it out"
    assert html.unescape(playlist['description']) == (
        "I should've burned this place down when I had the chance"
    )
    assert playlist['owner']['display_name'] == "Ishan"
    assert playlist['images'][0]['url'] == (
        "https://mosaic.scdn.co/640/"
        "ab67616d0000b27337b16a48dec737a46b244ea2ab67616d0000b2735"
        "86acdba3a0ddc93693a313eab67616d0000b273a6b996b1140c51"
        "6deda4b9b0ab67616d0000b273cab7ae4868e9f9ce6bdfdf43"
    )
    assert len(playlist['tracks']['items']) == 19


# test for an invalid link
def test_get_playlist_from_spotify_with_invalid_spotify_link(handler):
    playlist_url = (
        "https://open.spotify.com/playlist/"
        "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
        "HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH"
    )
    try:
        playlist = handler.get_playlist_from_spotify(playlist_url)
        assert playlist is None

    except Exception as e:
        print(str(e))
        assert str(e) == "Playlist unavailable or private"


# ------------------ Get_Playlist_Id_From_Link Tests ------------------ #
# gets the id from a playlist url
def test_get_playlist_id_from_link(handler):
    playlist_id = handler.get_playlist_id_from_link(
        "https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M"
        )
    assert playlist_id == "37i9dQZF1DXcBWIGoYBM5M"
    with_q_mark = handler.get_playlist_id_from_link(
        "https://open.spotify.com/playlist/"
        "37i9dQZF1DXcBWIGoYBM5M?si=3e2e2e2e2e2e2e2e"
        )
    assert with_q_mark == "37i9dQZF1DXcBWIGoYBM5M"


# ------------------ Get_Playlist_From_Id Tests ------------------ #
# tests the get playlist method in the playlist handler
@pytest.mark.django_db
def test_get_playlist(handler):
    playlist_url = (
        "https://open.spotify.com/playlist/"
        "6cUbe8r2kP140bL0Z2HHXV?si=89cbce6452b84b10"
        )
    playlist = handler.get_playlist(playlist_url)

    assert playlist is not None
    assert playlist.id == "6cUbe8r2kP140bL0Z2HHXV"
    assert playlist.url == (
        "https://open.spotify.com/playlist/6cUbe8r2kP140bL0Z2HHXV"
    )
    assert playlist.name == "Fleece it out"
    assert playlist.description == (
        "I should've burned this place down "
        "when I had the chance")
    assert playlist.author == "Ishan"
    assert playlist.thumbnail == (
        "https://mosaic.scdn.co/640/"
        "ab67616d0000b27337b16a48dec737a46b244ea2ab67616d0000b"
        "273586acdba3a0ddc93693a313eab67616d0000b273a6b996b1140"
        "c516deda4b9b0ab67616d0000b273cab7ae4868e9f9ce6bdfdf43"
    )
    assert len(playlist.songs) == 19


# tests the get playlist method in the playlist handler
@pytest.mark.django_db
def test_get_saved_playlist(handler):
    playlist_url = (
        "https://open.spotify.com/playlist/"
        "6cUbe8r2kP140bL0Z2HHXV?si=89cbce6452b84b10"
        )
    handler.get_playlist(playlist_url)
    playlist2 = handler.get_playlist(playlist_url)

    assert playlist2 is not None
    assert playlist2.id == "6cUbe8r2kP140bL0Z2HHXV"
    assert playlist2.url == (
        "https://open.spotify.com/playlist/6cUbe8r2kP140bL0Z2HHXV"
    )
    assert playlist2.name == "Fleece it out"
    assert len(playlist2.songs) == 19


def test_get_playlist_from_id_with_invalid_link(handler):
    playlist_url = (
        "AAAAAAAAAAAAAAAAAAAA"
        "HHHHHHHHHHHHHHHHHHHH"
    )
    with pytest.raises(Exception) as context:
        playlist = handler.get_playlist_id_from_link(playlist_url)
        assert playlist is None
    assert str(context.value) == "Invalid playlist link"


# ------------------ Save_Playlist Tests ------------------ #
@pytest.mark.django_db
def test_save_playlist(handler):
    playlist_url = (
        "https://open.spotify.com/playlist/"
        "5LUOAa14SigWmSbqdR6dhJ?si=c82146374f584d3f"
    )
    playlist = handler.get_playlist(playlist_url)
    assert handler.get_playlist_from_db(playlist.id) is not None


# ------------------ Get_Playlist_From_Db Tests ------------------ #
# tests the get playlist from db method
@pytest.mark.django_db
def test_get_playlist_from_db(handler):
    playlist_url = (
        "https://open.spotify.com/playlist/"
        "6cUbe8r2kP140bL0Z2HHXV?si=89cbce6452b84b10"
        )
    playlist = handler.get_playlist(playlist_url)
    playlist2 = handler.get_playlist_from_db(playlist.id)

    assert playlist2 is not None
    assert playlist2.id == "6cUbe8r2kP140bL0Z2HHXV"
    assert playlist2.url == (
        "https://open.spotify.com/playlist/6cUbe8r2kP140bL0Z2HHXV"
    )
    assert playlist2.name == "Fleece it out"
    assert len(playlist2.songs) == 19


@pytest.mark.django_db
def test_get_unseen_playlist_from_db(handler):
    with pytest.raises(Exception) as context:
        playlist2 = handler.get_playlist_from_db('AAAAAAAAAAAH')
        assert playlist2 is None
    assert str(context.value) == "Playlist not found in database"
