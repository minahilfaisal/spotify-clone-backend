# Generated by Django 3.2 on 2023-09-14 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playlists', '0003_remove_playlist_likes'),
        ('songs', '0010_auto_20230914_0934'),
        ('userdata', '0003_auto_20230914_1000'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RecentlyPlayedAlbums',
            new_name='RecentlyPlayedAlbum',
        ),
        migrations.RenameModel(
            old_name='RecentlyPlayedPlaylists',
            new_name='RecentlyPlayedPlaylist',
        ),
    ]
