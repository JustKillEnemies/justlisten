from django.contrib import admin
from .models import Song, Album, Author
from django.utils.text import slugify



@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    # prepopulated_fields = {'slug': ('name',)}
    fields = ['name']
    list_display = ['name', 'slug']

    def save_model(self, request, obj, form, change):
        if not obj.slug:
            base_slug = slugify(obj.name)
            addition = Author.objects.filter(slug__startswith=base_slug).count()
            if addition == 0:
                obj.slug = base_slug
            else:
                obj.slug = f"{base_slug}-{addition}"

        super().save_model(request, obj, form, change)

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    # prepopulated_fields = {'slug': ('title',)}
    fields = ['title', 'duration','author', 'cover', 'release_date', 'description', 'album', ]
    list_display = ['title', 'duration','author', 'cover', 'release_date', 'description', 'album', 'slug']
    list_display_links = ['title']

    def save_model(self, request, obj, form, change):
        if not obj.slug:
            base_slug = slugify(obj.title)
            addition = Song.objects.filter(slug__startswith=base_slug).count()
            if addition == 0:
                obj.slug = base_slug
            else:
                obj.slug = f"{base_slug}-{addition}"

        super().save_model(request, obj, form, change)


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    fields = ['name', 'author', 'songs_count', 'cover', 'release_date', 'description', 'slug']
    list_display = ['name', 'author', 'songs_count', 'cover', 'release_date', 'description', 'slug']

    # def save_model(self, request, obj, form, change):
    #     if not obj.slug:
    #         base_slug = slugify(obj.name)
    #         addition = Album.objects.filter(slug__startswith=base_slug).count()
    #         if addition == 0:
    #             obj.slug = base_slug
    #         else:
    #             obj.slug = f"{base_slug}-{addition}"
    #
    #     super().save_model(request, obj, form, change)


