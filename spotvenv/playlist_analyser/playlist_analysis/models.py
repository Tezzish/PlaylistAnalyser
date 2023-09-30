from django.db import models

# Create your models here.
class Playlist(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    url = models.CharField(max_length=1000)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    thumbnail = models.CharField(max_length=1000)
    author = models.CharField(max_length=200)
    songs = models.ManyToManyField('Song')

class Song(models.Model):
    name = models.CharField(max_length=200)
    id = models.CharField(max_length=200, primary_key=True)
    artist = models.CharField(max_length=200)
    album = models.CharField(max_length=200)
    thumbnail = models.CharField(max_length=1000)
    duration = models.IntegerField()
    url = models.CharField(max_length=1000)
    energy = models.FloatField()
    danceability = models.FloatField()
    valence = models.FloatField()
    tempo = models.FloatField()
    loudness = models.FloatField()
    acousticness = models.FloatField()