from django.shortcuts import render
from rest_framework import generics
from .models import Song, Album, Author
from .serializers import SongSerializer, AlbumSerializer, AuthorSerializer


class SongsAPIView(generics.ListAPIView):
    queryset = Song.objects.all().select_related('author', 'album')
    serializer_class = SongSerializer


class AlbumsAPIView(generics.ListAPIView):
    queryset = Album.objects.all().select_related('author')
    serializer_class = AlbumSerializer


class AuthorsAPIView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class SongAPIView(generics.RetrieveAPIView):
    queryset = Song.objects.all().select_related('author', 'album')
    serializer_class = SongSerializer
    lookup_field = 'slug'


class AlbumAPIView(generics.RetrieveAPIView):
    queryset = Album.objects.all().select_related('author')
    serializer_class = AlbumSerializer
    lookup_field = 'slug'


class AuthorAPIView(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    lookup_field = 'slug'