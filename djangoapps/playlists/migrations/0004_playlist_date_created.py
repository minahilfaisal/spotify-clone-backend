# Generated by Django 3.2 on 2023-09-26 07:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('playlists', '0003_remove_playlist_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
