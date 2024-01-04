class Song:

    def __init__(
            self,
            id,
            url,
            title,
            artist,
            album,
            thumbnail,
            duration,
            energy,
            danceability,
            valence,
            tempo,
            loudness,
            acousticness
            ):
        self._id = id
        self._url = url
        self._title = title
        self._artist = artist
        self._album = album
        self._thumbnail = thumbnail
        self._duration = duration
        self._energy = energy
        self._danceability = danceability
        self._valence = valence
        self._tempo = tempo
        self._loudness = loudness
        self._acousticness = acousticness

    def __str__(self):
        return (
            f"Song ID: {self._id}\n"
            f"URL: {self._url}\n"
            f"Title: {self._title}\n"
            f"Artist: {self._artist}\n"
            f"Album: {self._album}\n"
            f"Energy: {self._energy}\n"
            f"Danceability: {self._danceability}\n"
            f"Acousticness: {self._acousticness}\n"
            f"Tempo: {self._tempo}"
        )

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
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def artist(self):
        return self._artist

    @artist.setter
    def artist(self, value):
        self._artist = value

    @property
    def album(self):
        return self._album

    @album.setter
    def album(self, value):
        self._album = value

    @property
    def thumbnail(self):
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, value):
        self._thumbnail = value

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        self._duration = value

    @property
    def energy(self):
        return self._energy

    @energy.setter
    def energy(self, value):
        self._energy = value

    @property
    def danceability(self):
        return self._danceability

    @danceability.setter
    def danceability(self, value):
        self._danceability = value

    @property
    def valence(self):
        return self._valence

    @valence.setter
    def valence(self, value):
        self._valence = value

    @property
    def tempo(self):
        return self._tempo

    @tempo.setter
    def tempo(self, value):
        self._tempo = value

    @property
    def loudness(self):
        return self._loudness

    @loudness.setter
    def loudness(self, value):
        self._loudness = value

    @property
    def acousticness(self):
        return self._acousticness

    @acousticness.setter
    def acousticness(self, value):
        self._acousticness = value
