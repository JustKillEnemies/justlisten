from django.db import models
from slugify import slugify


def simple_unique_slug(instance, field_value, slug_field_name='slug'):
    base_slug = slugify(field_value)
    similar = instance.__class__.objects.filter(**{f"{slug_field_name}__startswith": base_slug}).count()
    return f"{base_slug}-{similar + 1}"


class Song(models.Model):
    title = models.CharField(max_length=255)
    duration = models.DurationField(name='duration')
    author = models.ForeignKey("Author", on_delete=models.SET_NULL, null=True, related_name='songs')
    cover = models.ImageField(upload_to='song_covers/', max_length=255, blank=True, name='cover')
    release_date = models.DateField(null=True)
    description = models.TextField(blank=True, null=True)
    album = models.ForeignKey("Album", on_delete=models.SET_NULL, null=True, related_name='related_songs')
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = simple_unique_slug(self, self.title)
        super().save(*args, **kwargs)


class Author(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = simple_unique_slug(self, self.name)
        super().save(*args, **kwargs)


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
