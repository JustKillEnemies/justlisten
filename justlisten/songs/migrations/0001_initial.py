# Generated by Django 5.2.2 on 2025-06-12 14:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('songs_count', models.IntegerField(blank=True, null=True)),
                ('release_date', models.DateField(null=True)),
                ('description', models.TextField(blank=True, default='Отсутствует', null=True)),
                ('cover', models.ImageField(blank=True, max_length=255, upload_to='album_covers/')),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='albums', to='songs.author')),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('duration', models.DurationField()),
                ('cover', models.ImageField(blank=True, max_length=255, upload_to='song_covers/')),
                ('release_date', models.DateField(null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                ('test', models.CharField(blank=True, max_length=10)),
                ('album', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='related_songs', to='songs.album')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='songs', to='songs.author')),
            ],
        ),
    ]
