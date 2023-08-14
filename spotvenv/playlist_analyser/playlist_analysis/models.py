from django.db import models

# Create your models here.
class Playlist(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    thumbnail = models.CharField(max_length=1000)
    author = models.CharField(max_length=200)
    songs = models.ManyToManyField('Song')
    avg_energy = models.FloatField()
    avg_danceability = models.FloatField()
    avg_valence = models.FloatField()
    avg_tempo = models.FloatField()
    avg_loudness = models.FloatField()
    avg_acousticness = models.FloatField()
    avg_duration = models.FloatField()

class Song(models.Model):
    name = models.CharField(max_length=200)
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