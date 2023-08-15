from django.test import TestCase
from .song import Song

# Create your tests here.
class SongTestCase(TestCase):

    def setUp(self):
        self.song = Song("https://open.spotify.com/track/7wBJfHzpfI3032CSD7CE2m?si=2c92617d97284914")

    def test_song_attributes(self):
        self.assertEqual(self.song.title, "STARGAZING")
        self.assertEqual(self.song.artist, "Travis Scott")
        self.assertEqual(self.song.album, "ASTROWORLD")
        self.assertEqual(self.song.id, "7wBJfHzpfI3032CSD7CE2m")