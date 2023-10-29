from django.test import TestCase
from .song import Song
from .playlist_handler import PlaylistHandler
import html

# Tests the playlist handler class
class PlaylistHandlerTestCase(TestCase):

    def setUp(self):
        self.handler = PlaylistHandler()

    #------------------ Get_Playlist_From_Url Tests ------------------#
    # simple test to get a playlist from a url
    # returns the json of the playlist
    def test_get_playlist_from_url(self):
        # gets a json of the playlist
        playlist_url = "https://open.spotify.com/playlist/6cUbe8r2kP140bL0Z2HHXV?si=89cbce6452b84b10"
        playlist = self.handler.get_playlist_from_url(playlist_url)
        self.assertIsNotNone(playlist)
        self.assertEqual(playlist['name'], "Fleece it out")
        self.assertEqual(html.unescape(playlist['description']), "I should've burned this place down when I had the chance")
        self.assertEqual(playlist['owner']['display_name'], "Ishan")
        self.assertEqual(playlist['images'][0]['url'], "https://mosaic.scdn.co/640/ab67616d0000b27337b16a48dec737a46b244ea2ab67616d0000b273586acdba3a0ddc93693a313eab67616d0000b273a6b996b1140c516deda4b9b0ab67616d0000b273cab7ae4868e9f9ce6bdfdf43")
        self.assertEqual(len(playlist['tracks']['items']), 19)

    # test for an invalid link
    def test_get_playlist_from_url_with_invalid_link(self):
        playlist_url = "https://open.spotify.com/playlist/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH"
        try:
            playlist = self.handler.get_playlist_from_url(playlist_url)
            self.assertIsNone(playlist)

        except Exception as e:
            if str(e) == "Playlist unavailable or private":
                self.passed = True
            self.passed = False

    #------------------ Get_Playlist_Id_From_Link Tests ------------------#
    # gets the id from a playlist url
    def test_get_playlist_id_from_link(self):
        playlist_id = self.handler.get_playlist_id_from_link("https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M")
        self.assertEqual(playlist_id, "37i9dQZF1DXcBWIGoYBM5M")
        with_q_mark = self.handler.get_playlist_id_from_link("https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M?si=3e2e2e2e2e2e2e2e")
        self.assertEqual(with_q_mark, "37i9dQZF1DXcBWIGoYBM5M")

    #------------------ Get_Playlist_From_Id Tests ------------------#
    # tests the get playlist method in the playlist handler
    def test_get_playlist(self):

        playlist_url = "https://open.spotify.com/playlist/6cUbe8r2kP140bL0Z2HHXV?si=89cbce6452b84b10"
        playlist = self.handler.get_playlist(playlist_url)

        self.assertIsNotNone(playlist)
        self.assertEqual(playlist.id, "6cUbe8r2kP140bL0Z2HHXV")
        self.assertEqual(playlist.url, "https://open.spotify.com/playlist/6cUbe8r2kP140bL0Z2HHXV")
        self.assertEqual(playlist.name, "Fleece it out")
        self.assertEqual(playlist.description, "I should've burned this place down when I had the chance")
        self.assertEqual(playlist.author, "Ishan")
        self.assertEqual(playlist.thumbnail, "https://mosaic.scdn.co/640/ab67616d0000b27337b16a48dec737a46b244ea2ab67616d0000b273586acdba3a0ddc93693a313eab67616d0000b273a6b996b1140c516deda4b9b0ab67616d0000b273cab7ae4868e9f9ce6bdfdf43")
        self.assertEqual(len(playlist.songs), 19)

    def test_save_playlist(self):
        playlist_url = "https://open.spotify.com/playlist/5LUOAa14SigWmSbqdR6dhJ?si=c82146374f584d3f"
        playlist = self.handler.get_playlist(playlist_url)
        self.assertIsNotNone(self.handler.get_playlist_from_db(playlist.id))

# Tests the playlist class
class PlaylistTestCase(TestCase):
    def setUp(self):
        self.handler = PlaylistHandler()
        self.playlist_url = "https://open.spotify.com/playlist/6cUbe8r2kP140bL0Z2HHXV?si=89cbce6452b84b10"
        self.playlist = self.handler.get_playlist(self.playlist_url)

    #------------------ Get_Avg_Of_Attribute Tests ------------------#
    def test_get_avg_attributes(self):
        playlist_url = "https://open.spotify.com/playlist/6cUbe8r2kP140bL0Z2HHXV?si=89cbce6452b84b10"
        playlist = self.handler.get_playlist(playlist_url)
        avg_attributes = playlist.get_avg_attributes()
        
        self.assertEqual(avg_attributes['Energy'], 77)
        self.assertEqual(avg_attributes['Danceability'], 46)
        self.assertEqual(avg_attributes['Acousticness'], 17)
        self.assertEqual(avg_attributes['Valence'], 39)
        self.assertAlmostEqual(avg_attributes['Loudness'], -5.86, 2)
        self.assertEqual(avg_attributes['Tempo'], 131)
        self.assertEqual(avg_attributes['Duration'], 222)

    #------------------ Get_Max_Of_Attribute Tests ------------------#
    def test_get_max_attributes(self):
        playlist_url = "https://open.spotify.com/playlist/6cUbe8r2kP140bL0Z2HHXV?si=89cbce6452b84b10"
        playlist = self.handler.get_playlist(playlist_url)
        max_attributes = playlist.get_max_attributes()

        self.assertEqual(max_attributes['Energy'][0], 98)
        self.assertEqual(max_attributes['Danceability'][0], 68)
        self.assertEqual(max_attributes['Acousticness'][0], 97)
        self.assertEqual(max_attributes['Valence'][0], 70)
        self.assertAlmostEqual(max_attributes['Loudness'][0], -2.58, 0)
        self.assertEqual(max_attributes['Tempo'][0], 180, 0)
        self.assertEqual(max_attributes['Duration'][0], 475, 0)

    