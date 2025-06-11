from justlisten import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from songs import views
# # где Categorys -  общий  вью,  который   вызывает нужную, в зависимости от пришедшего cat
#   path('api/v1/<str:cat>/<?int:id>', Categorys.as_view()),
urlpatterns = [
    path('api/v1/songslist/', views.SongsAPIView.as_view()),
    path('api/v1/albumslist/', views.AlbumsAPIView.as_view()),
    path('api/v1/authorslist/', views.AuthorsAPIView.as_view()),
    path('api/v1/songslist/<slug:slug>/', views.SongAPIView.as_view()),
    path('api/v1/albumslist/<slug:slug>/', views.AlbumAPIView.as_view()),
    path('api/v1/authorslist/<slug:slug>/', views.AuthorAPIView.as_view()),
    ]

