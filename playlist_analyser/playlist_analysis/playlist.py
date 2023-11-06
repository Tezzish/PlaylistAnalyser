import datetime

class Playlist:

    def __init__(self, id, url, name, description, author, thumbnail, songs):
        self._id = id
        self._url = url
        self._name = name
        self._description = description
        self._author = author
        self._thumbnail = thumbnail
        self._songs = songs

    def __str__(self):
        #return all attributes
        return f"Playlist(id={self._id}, url={self._url}, name={self._name}, description={self._description}, author={self._author}, thumbnail={self._thumbnail}, songs={self._songs}, avg_energy={self._avg_energy}, avg_danceability={self._avg_danceability}, avg_acousticness={self._avg_acousticness}, avg_valence={self._avg_valence}, avg_loudness={self._avg_loudness}, avg_tempo={self._avg_tempo}, avg_duration={self._avg_duration})"
    
    def __dict__(self):
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
        # get the average of the attribute for all songs in the playlist using functional programming
        return sum(map(lambda song: getattr(song, attribute), self._songs)) / len(self._songs)
    
    def get_max_of_attribute(self, attribute):
        # get the max of the attribute for all songs in the playlist using functional programming
        # return a tuple of the value and the song object
        return max(map(lambda song: (getattr(song, attribute), song), self._songs))

    def get_avg_attributes(self):
        print(round(self.get_avg_of_attribute('duration'), 2))
        return {
            'Energy' : round(self.get_avg_of_attribute('energy') * 100),
            'Danceability' : round(self.get_avg_of_attribute('danceability') * 100),
            'Acousticness' : round(self.get_avg_of_attribute('acousticness') * 100),
            'Valence' : round(self.get_avg_of_attribute('valence') * 100),
            'Loudness' : round(self.get_avg_of_attribute('loudness'), 2),
            'Tempo' : round(self.get_avg_of_attribute('tempo')),
            'Duration' : round(self.get_avg_of_attribute('duration') / 1000),
        }
    
    def get_max_attributes(self):
        # we save the values because we need to also return the song url
        # so one call instead of two
        energy = self.get_max_of_attribute('energy')
        danceability = self.get_max_of_attribute('danceability')
        acousticness = self.get_max_of_attribute('acousticness')
        valence = self.get_max_of_attribute('valence')
        loudness = self.get_max_of_attribute('loudness')
        tempo = self.get_max_of_attribute('tempo')
        duration = self.get_max_of_attribute('duration')
        return {
            'Energy' : (round(energy[0] * 100), energy[1].url),
            'Danceability' : (round(danceability[0] * 100), danceability[1].url),
            'Acousticness' : (round(acousticness[0] * 100), acousticness[1].url),
            'Valence' : (round(valence[0] * 100), valence[1].url),
            'Loudness' : (round(loudness[0], 2), loudness[1].url),
            'Tempo' : (round(tempo[0]), tempo[1].url),
            'Duration' : (round(duration[0] / 1000), duration[1].url),
        }
