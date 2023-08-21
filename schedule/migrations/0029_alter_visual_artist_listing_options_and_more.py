# Generated by Django 4.2.4 on 2023-08-19 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0028_rename_class_date_extra_curriucular_listing_class_day'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='visual_artist_listing',
            options={'ordering': ['vis_show_date_start'], 'verbose_name': 'Visual Artist', 'verbose_name_plural': 'Visual Artists'},
        ),
        migrations.RenameField(
            model_name='visual_artist_listing',
            old_name='artist_bio',
            new_name='vis_artist_bio',
        ),
        migrations.RenameField(
            model_name='visual_artist_listing',
            old_name='artist_medium',
            new_name='vis_artist_medium',
        ),
        migrations.RenameField(
            model_name='visual_artist_listing',
            old_name='artist_name',
            new_name='vis_artist_name',
        ),
        migrations.RenameField(
            model_name='visual_artist_listing',
            old_name='artist_website',
            new_name='vis_artist_website',
        ),
        migrations.RenameField(
            model_name='visual_artist_listing',
            old_name='entry_price',
            new_name='vis_entry_price',
        ),
        migrations.RenameField(
            model_name='visual_artist_listing',
            old_name='image_url',
            new_name='vis_image_url',
        ),
        migrations.RenameField(
            model_name='visual_artist_listing',
            old_name='show_date_end',
            new_name='vis_show_date_end',
        ),
        migrations.RenameField(
            model_name='visual_artist_listing',
            old_name='show_date_start',
            new_name='vis_show_date_start',
        ),
    ]
