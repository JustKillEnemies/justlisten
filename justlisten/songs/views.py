from django.shortcuts import render
from rest_framework import generics
from .models import Song, Album, Author
from .serializers import SongSerializer, AlbumSerializer, AuthorSerializer
from rest_framework import filters


class SongsAPIView(generics.ListAPIView):
    queryset = Song.objects.all().select_related('author', 'album')
    serializer_class = SongSerializer


class AlbumsAPIView(generics.ListAPIView):
    queryset = Album.objects.all().select_related('author')
    serializer_class = AlbumSerializer


class AuthorsAPIView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class SongAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all().select_related('author', 'album')
    serializer_class = SongSerializer
    lookup_field = 'slug'


class AlbumAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all().select_related('author')
    serializer_class = AlbumSerializer
    lookup_field = 'slug'


class AuthorAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    lookup_field = 'slug'


class SearchListView(generics.ListAPIView):
    filter_backends = [filters.SearchFilter]


class SearchAuthorAPIView(SearchListView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    search_fields = ['name']


class SearchAlbumAPIView(SearchListView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    search_fields = ['name', 'author__name']


class SearchSongAPIView(SearchListView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    search_fields = ['title', 'author__name']


class CreateAuthorAPIView(generics.CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer