from rest_framework import serializers


class SongSerializer(serializers.Serializer):
    id = serializers.CharField()
    title = serializers.CharField()
    artist = serializers.CharField()
    album = serializers.CharField()
    duration = serializers.IntegerField()
    thumbnail = serializers.URLField()
    url = serializers.URLField()


class PlaylistSerializer(serializers.Serializer):
    id = serializers.CharField()
    url = serializers.URLField()
    name = serializers.CharField()
    description = serializers.CharField()
    author = serializers.CharField()
    thumbnail = serializers.URLField()
    songs = SongSerializer(many=True)

    class Meta:
        fields = '__all__'
