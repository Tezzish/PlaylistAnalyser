# Generated by Django 4.2.5 on 2023-09-30 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('artist', models.CharField(max_length=200)),
                ('album', models.CharField(max_length=200)),
                ('thumbnail', models.CharField(max_length=1000)),
                ('duration', models.IntegerField()),
                ('url', models.CharField(max_length=1000)),
                ('energy', models.FloatField()),
                ('danceability', models.FloatField()),
                ('valence', models.FloatField()),
                ('tempo', models.FloatField()),
                ('loudness', models.FloatField()),
                ('acousticness', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('url', models.CharField(max_length=1000)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1000)),
                ('thumbnail', models.CharField(max_length=1000)),
                ('author', models.CharField(max_length=200)),
                ('avg_energy', models.FloatField()),
                ('avg_danceability', models.FloatField()),
                ('avg_valence', models.FloatField()),
                ('avg_tempo', models.FloatField()),
                ('avg_loudness', models.FloatField()),
                ('avg_acousticness', models.FloatField()),
                ('avg_duration', models.FloatField()),
                ('songs', models.ManyToManyField(to='playlist_analysis.song')),
            ],
        ),
    ]