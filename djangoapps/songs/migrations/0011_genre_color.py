# Generated by Django 3.2 on 2023-09-27 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0010_auto_20230914_0934'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='color',
            field=models.CharField(default='#FFC0CB', max_length=200),
            preserve_default=False,
        ),
    ]
