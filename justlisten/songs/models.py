from django.db import models
from slugify import slugify
from .utils import simple_unique_slug
from users.models import CustomUser

class Song(models.Model):
    title = models.CharField(max_length=255)
    duration = models.DurationField(name='duration')
    author = models.ForeignKey("Author", on_delete=models.SET_NULL, null=True, related_name='songs')
    cover = models.ImageField(upload_to='song_covers/', max_length=255, blank=True, name='cover')
    release_date = models.DateField(null=True)
    description = models.TextField(blank=True, null=True)
    album = models.ForeignKey("Album", on_delete=models.SET_NULL, null=True, related_name='related_songs')
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    test = models.CharField(max_length=10, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = simple_unique_slug(self, self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = simple_unique_slug(self, self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey("Author", on_delete=models.SET_NULL, related_name='albums', null=True)
    songs_count = models.IntegerField(blank=True, null=True,)
    release_date = models.DateField(null=True)
    description = models.TextField(blank=True, null=True, default="Отсутствует")
    cover = models.ImageField(upload_to='album_covers/', max_length=255, blank=True, name='cover')
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = simple_unique_slug(self, self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


    #           НА БУДУЩЕЕ

# class Like(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_likes')
#     song = models.ForeignKey(Song, null=True, blank=True, on_delete=models.CASCADE)
#     album = models.ForeignKey(Album, null=True, blank=True, on_delete=models.CASCADE)
#
#     class Meta:
#         constraints = [
#             models.CheckConstraint(
#                 check=(
#                     models.Q(song__isnull=False, album__isnull=True) |
#                     models.Q(song__isnull=True, album__isnull=False)
#                 ),
#                 name='only_one_like_target'
#             ),
#             models.UniqueConstraint(
#                 fields=['user', 'song'],
#                 name='unique_user_song_like',
#                 condition=models.Q(song__isnull=False)
#             ),
#             models.UniqueConstraint(
#                 fields=['user', 'album'],
#                 name='unique_user_album_like',
#                 condition=models.Q(album__isnull=False)
#             )
#         ]