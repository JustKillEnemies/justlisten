from justlisten import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from songs import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)


urlpatterns = [
    path('api/v1/songslist/', views.SongsAPIView.as_view()),
    path('api/v1/albumslist/', views.AlbumsAPIView.as_view()),
    path('api/v1/authorslist/', views.AuthorsAPIView.as_view()),
    path('api/v1/authorslist/search/', views.SearchAuthorAPIView.as_view(), name='search-authors'),
    path('api/v1/songslist/search/', views.SearchSongAPIView.as_view(), name='search-songs'),
    path('api/v1/albumslist/search/', views.SearchAlbumAPIView.as_view(), name='search-albums'),
    path('api/v1/songslist/<slug:slug>/', views.SongAPIView.as_view()),
    path('api/v1/albumslist/<slug:slug>/', views.AlbumAPIView.as_view()),
    path('api/v1/authorslist/<slug:slug>/', views.AuthorAPIView.as_view()),
    path('api/v1/authors/create/', views.CreateAuthorAPIView.as_view(), name='author-create'),


    ]

