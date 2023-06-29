# Generated by Django 4.2.1 on 2023-05-25 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0010_visual_artist_listing_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='music_artist_listing',
            options={'verbose_name': 'Musician', 'verbose_name_plural': 'Musicians'},
        ),
        migrations.AlterModelOptions(
            name='visual_artist_listing',
            options={'verbose_name': 'Visual Artist', 'verbose_name_plural': 'Visual Artists'},
        ),
        migrations.RenameField(
            model_name='visual_artist_listing',
            old_name='age_restricion',
            new_name='age_restriction',
        ),
    ]
