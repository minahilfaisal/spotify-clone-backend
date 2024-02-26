# Generated by Django 3.2 on 2023-08-31 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0004_auto_20230830_1240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='genre',
        ),
        migrations.AddField(
            model_name='album',
            name='genre',
            field=models.CharField(choices=[(1, 'pop rap'), (2, 'pop'), (3, 'edm'), (4, 'electro house'), (5, 'dance pop'), (6, 'lounge'), (7, 'house'), (8, 'urban contemporary'), (9, 'classical'), (10, 'alternative hip hop')], default=1, max_length=2),
        ),
    ]