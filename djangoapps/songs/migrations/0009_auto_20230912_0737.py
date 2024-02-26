# Generated by Django 3.2 on 2023-09-12 07:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('songs', '0008_alter_song_unique_together'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='songlike',
            name='song',
        ),
        migrations.RemoveField(
            model_name='songlike',
            name='user',
        ),
        migrations.AddField(
            model_name='album',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='album_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='song',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='song_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='AlbumLike',
        ),
        migrations.DeleteModel(
            name='SongLike',
        ),
    ]
