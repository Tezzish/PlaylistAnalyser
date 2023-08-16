import requests
import dotenv
import os

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
        return f"Playlist: {self.name} by {self.author} ({len(self.songs)} songs)"

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