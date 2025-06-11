from rest_framework import serializers
from .models import Song, Album, Author


class SongSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.name', read_only=True)
    album_name = serializers.CharField(source='album.name', read_only=True)

    class Meta:
        model = Song
        fields = ['id', 'title', 'duration', 'author_name', 'cover', 'release_date', 'description', 'album_name', 'slug']


class AlbumSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.name', read_only=True)

    class Meta:
        model = Album
        fields = ['id','name', 'author_name', 'cover', 'songs_count', 'release_date', 'description', 'slug']


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ['id', 'name', 'slug']