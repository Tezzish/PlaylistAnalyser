class Playlist:
    """
    Represents a playlist with various attributes and methods for analysis.
    """

    def __init__(self, id, url, name, description, author, thumbnail, songs):
        self._id = id
        self._url = url
        self._name = name
        self._description = description
        self._author = author
        self._thumbnail = thumbnail
        self._songs = songs

    def __str__(self):
        # map songs to song names
        songs = list(map(lambda song: song.title, self._songs))
        # return all attributes
        return (
            f"Playlist(id={self._id}, url={self._url}, name={self._name}, "
            f"description={self._description}, author={self._author}, "
            f"thumbnail={self._thumbnail}, songs={songs}"
            )

    def __dict__(self):
        """
        Returns a dictionary representation of the playlist object.

        Returns:
            dict: A dictionary with attribute names as keys
                and their corresponding values.
        """
        return {
            'id': self._id,
            'url': self._url,
            'name': self._name,
            'description': self._description,
            'author': self._author,
            'thumbnail': self._thumbnail,
            'songs': self._songs,
        }

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
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._author = value

    @property
    def thumbnail(self):
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, value):
        self._thumbnail = value

    @property
    def songs(self):
        return self._songs

    @songs.setter
    def songs(self, value):
        self._songs = value

    def get_avg_of_attribute(self, attribute):
        """
        Calculates the average value of a given attribute
            for all songs in the playlist.

        Args:
            attribute (str): The name of the attribute.

        Returns:
            float: The average value of the attribute.
        """
        # get the average of the attribute for all songs in the playlist
        return (
            sum(map(lambda song: getattr(song, attribute), self._songs)) /
            len(self._songs)
        )

    def get_max_of_attribute(self, attribute):
        """
        Finds the maximum value of a given attribute
            for all songs in the playlist.

        Args:
            attribute (str): The name of the attribute.

        Returns:
            tuple: A tuple containing the maximum value
                and the corresponding song object.
        """
        # get the max of the attribute for all songs in the playlist
        # return a tuple of the value and the song object
        return (
            max(
                map(
                    lambda song: (getattr(song, attribute), song), self._songs
                ),
                key=lambda song: song[0]))

    def get_avg_attributes(self):
        """
        Calculates the average values of various attributes
            for all songs in the playlist.

        Returns:
            dict: A dictionary with attribute names as keys
                and their corresponding average values.
        """
        return {
            'Energy': round(self.get_avg_of_attribute('energy') * 100),
            'Danceability':
                round(self.get_avg_of_attribute('danceability') * 100),
            'Acousticness':
                round(self.get_avg_of_attribute('acousticness') * 100),
            'Valence': round(self.get_avg_of_attribute('valence') * 100),
            'Loudness': round(self.get_avg_of_attribute('loudness'), 2),
            'Tempo': round(self.get_avg_of_attribute('tempo')),
            'Duration': round(self.get_avg_of_attribute('duration') / 1000),
        }

    def get_max_attributes(self):
        """
        Finds the maximum values of various attributes

        Returns:
            dict: A dictionary with attribute names as keys and tuples
            of rounded attribute values and song URLs as values.
        """
        ''' We save the values because we need to also return the song url
            so it's one call instead of two'''
        energy = self.get_max_of_attribute('energy')
        danceability = self.get_max_of_attribute('danceability')
        acousticness = self.get_max_of_attribute('acousticness')
        valence = self.get_max_of_attribute('valence')
        loudness = self.get_max_of_attribute('loudness')
        tempo = self.get_max_of_attribute('tempo')
        duration = self.get_max_of_attribute('duration')
        return {
            'Energy': (round(energy[0] * 100), energy[1].url),
            'Danceability':
                (round(danceability[0] * 100), danceability[1].url),
            'Acousticness':
                (round(acousticness[0] * 100), acousticness[1].url),
            'Valence': (round(valence[0] * 100), valence[1].url),
            'Loudness': (round(loudness[0], 2), loudness[1].url),
            'Tempo': (round(tempo[0]), tempo[1].url),
            'Duration': (round(duration[0] / 1000), duration[1].url),
        }
