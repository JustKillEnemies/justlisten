from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=255)
    duration = models.DurationField(name='duration')
    author = models.ForeignKey("Author", on_delete=models.SET_NULL, null=True, related_name='songs')
    cover = models.CharField(max_length=255, blank=True, name='cover')
    release_date = models.DateTimeField(null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    album = models.ForeignKey("Album", on_delete=models.SET_NULL, null=True, related_name='related_songs')


class Author(models.Model):
    name = models.CharField(max_length=255)


class Album(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey("Author", on_delete=models.SET_NULL, related_name='albums')
    songs_count = models.IntegerField(blank=True, null=True)
    release_date = models.DateTimeField(null=True, blank=True)
    description = models.TextField(blank=True, null=True)




