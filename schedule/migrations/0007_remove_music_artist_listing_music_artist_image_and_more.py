# Generated by Django 4.2.6 on 2024-02-01 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0006_alter_archivedresetdata_archive_reset_artist_web'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='music_artist_listing',
            name='music_artist_image',
        ),
        migrations.AddField(
            model_name='music_artist_listing',
            name='music_artist_image_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
