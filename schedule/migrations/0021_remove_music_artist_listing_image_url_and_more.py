# Generated by Django 4.2.1 on 2023-07-24 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0020_extra_curriucular_listing_image_url_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='music_artist_listing',
            name='image_url',
        ),
        migrations.AddField(
            model_name='extra_curriucular_listing',
            name='class_artist_image',
            field=models.ImageField(blank=True, default='test', null=True, upload_to='uploads/% Y/% m/% d/'),
        ),
        migrations.AddField(
            model_name='heads_up_music',
            name='artist_image',
            field=models.ImageField(blank=True, default='test', null=True, upload_to='uploads/% Y/% m/% d/'),
        ),
        migrations.AddField(
            model_name='music_artist_listing',
            name='music_artist_image',
            field=models.ImageField(blank=True, default='test', null=True, upload_to='uploads/% Y/% m/% d/'),
        ),
        migrations.AddField(
            model_name='visual_artist_listing',
            name='visual_artist_image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='uploads/% Y/% m/% d/'),
        ),
    ]
