from .playlist import Playlist

class PlaylistHandler:
    def get_playlist(self, playlist_url):
        playlist = Playlist(playlist_url)
        return playlist