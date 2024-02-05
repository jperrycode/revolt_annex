# Generated by Django 4.2.6 on 2024-02-04 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0009_remove_music_artist_listing_artist_music_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='music_artist_listing',
            name='reset_flyer_img_id',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='music_artist_listing',
            name='reset_flyer_img_secret',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='music_artist_listing',
            name='reset_flyer_serverID',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='visual_artist_listing',
            name='flyer_img_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]