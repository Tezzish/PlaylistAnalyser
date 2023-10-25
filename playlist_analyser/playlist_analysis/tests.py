from django.test import TestCase
from .song import Song
from .playlist_handler import PlaylistHandler
import html

class PlaylistHandlerTestCase(TestCase):

    def setUp(self):
        self.handler = PlaylistHandler()

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
        print(playlist)
        

    def test_get_playlist_id_from_link(self):
        playlist_id = self.handler.get_playlist_id_from_link("https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M")
        self.assertEqual(playlist_id, "37i9dQZF1DXcBWIGoYBM5M")
        with_q_mark = self.handler.get_playlist_id_from_link("https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M?si=3e2e2e2e2e2e2e2e")
        self.assertEqual(with_q_mark, "37i9dQZF1DXcBWIGoYBM5M")

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
        avg_attributes = playlist.get_avg_attributes()
        
        self.assertAlmostEqual(avg_attributes['energy'], 0.7694210526315789, 3)
        self.assertAlmostEqual(avg_attributes['danceability'], 0.46215789473684216, 3)
        self.assertAlmostEqual(avg_attributes['acousticness'], 0.17108994210526318, 3)
        self.assertAlmostEqual(avg_attributes['valence'], 0.3945789473684211, 3)
        self.assertAlmostEqual(avg_attributes['loudness'], -5.85521052631579, 3)
        self.assertAlmostEqual(avg_attributes['tempo'], 130.84536842105263, 3)
        self.assertAlmostEqual(avg_attributes['duration'], 221971.63157894736, 3)

    def test_save_playlist(self):
        playlist_url = "https://open.spotify.com/playlist/5LUOAa14SigWmSbqdR6dhJ?si=c82146374f584d3f"
        playlist = self.handler.get_playlist(playlist_url)
        self.assertIsNotNone(self.handler.get_playlist_from_db(playlist.id))

    def test_get_all_playlists(self):
        self.handler.get_playlist("https://open.spotify.com/playlist/5LUOAa14SigWmSbqdR6dhJ?si=c82146374f584d3f")
        self.handler.get_playlist("https://open.spotify.com/playlist/7owATjdpPTEGls8YJHjctt?si=9cb5710bd9684b69")
        self.handler.get_playlist("https://open.spotify.com/playlist/5LUOAa14SigWmSbqdR6dhJ?si=c82146374f584d3f")

        self.assertIsNotNone(self.handler.get_all_playlists())
        self.assertEqual(len(self.handler.get_all_playlists()), 2)