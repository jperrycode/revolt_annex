# Generated by Django 4.2.6 on 2024-01-02 00:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Archivedshowimagedata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archive_show_name', models.CharField(max_length=50)),
                ('archive_artist_name', models.CharField(blank=True, max_length=75, null=True)),
                ('archive_start_date', models.DateField(blank=True, null=True)),
                ('archive_end_date', models.DateField(blank=True, null=True)),
                ('archive_folder_id', models.CharField(max_length=50)),
                ('archive_artist_web', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'Archive',
                'verbose_name_plural': 'Archive',
                'ordering': ['archive_end_date'],
            },
        ),
        migrations.CreateModel(
            name='Extra_curriucular_listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(blank=True, default='', max_length=50)),
                ('class_teacher', models.CharField(default='', max_length=50)),
                ('class_description', models.TextField()),
                ('class_day', models.CharField(blank=True, max_length=30, null=True)),
                ('class_time', models.TimeField()),
                ('class_location', models.CharField(default='Revolt Annex', max_length=50)),
                ('class_price', models.FloatField(blank=True, null=True)),
                ('image_url', models.URLField(blank=True, max_length=250, null=True)),
                ('class_artist_image', models.ImageField(blank=True, null=True, upload_to='media/')),
            ],
            options={
                'verbose_name': 'Class listing',
                'verbose_name_plural': 'Class Listings',
            },
        ),
        migrations.CreateModel(
            name='Heads_up_music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=50)),
                ('event_date', models.DateField()),
                ('event_time', models.TimeField()),
                ('artist_name', models.CharField(max_length=50)),
                ('event_description', models.CharField(max_length=255)),
                ('artist_image', models.ImageField(blank=True, null=True, upload_to='media/')),
            ],
            options={
                'verbose_name': 'HUM Event',
                'verbose_name_plural': 'HUM Events',
                'ordering': ['event_date'],
            },
        ),
        migrations.CreateModel(
            name='Music_artist_listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist_name', models.CharField(blank=True, default='', max_length=50)),
                ('artist_genre', models.CharField(choices=[('rap', 'Rap'), ('Drum and Bass', 'Drum and Bass'), ('House', 'House'), ('Techno', 'Techno'), ('Rock and Roll', 'Rock and Roll'), ('Folk', 'Folk'), ('Scheduled Class', 'Scheduled Class'), ('Bass Music', 'Bass Music'), ('Other', 'Other'), ('UK Grime', 'UK Grime'), ('Hip Hop', 'Hip Hop')], default='', max_length=255)),
                ('show_date', models.DateField()),
                ('show_time', models.TimeField()),
                ('artist_bio', models.CharField(blank=True, default='', max_length=255)),
                ('artist_insta', models.CharField(blank=True, max_length=255, null=True)),
                ('artist_website', models.CharField(blank=True, max_length=255, null=True)),
                ('artist_music_page', models.CharField(default='search your self', max_length=200)),
                ('music_artist_image', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('entry_price', models.FloatField(null=True)),
            ],
            options={
                'verbose_name': 'Musician',
                'verbose_name_plural': 'Musicians',
                'ordering': ['show_date'],
            },
        ),
        migrations.CreateModel(
            name='Receive_email_updates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emailform_message', models.TextField(max_length=600, null=True)),
                ('emailform_email', models.EmailField(max_length=255, null=True)),
                ('emailform_name', models.CharField(blank=True, max_length=50, null=True)),
                ('emailform_subject', models.CharField(blank=True, max_length=50, null=True)),
                ('emailform_consent', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='VimeoVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_id', models.CharField(max_length=255, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Visual_artist_listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visual_show_name', models.CharField(default='Show Title', max_length=50)),
                ('vis_artist_name', models.CharField(blank=True, default='', max_length=50)),
                ('vis_artist_medium', models.CharField(default='', max_length=255)),
                ('vis_show_date_start', models.DateField()),
                ('vis_show_date_end', models.DateField()),
                ('vis_artist_bio', models.TextField(blank=True, default='')),
                ('vis_artist_website', models.CharField(blank=True, max_length=255, null=True)),
                ('vis_entry_price', models.FloatField(blank=True, null=True)),
                ('age_restriction', models.BooleanField(default=False)),
                ('vis_image_url', models.URLField(blank=True, max_length=250, null=True)),
                ('visual_artist_image', models.ImageField(blank=True, null=True, upload_to='media/')),
            ],
            options={
                'verbose_name': 'Visual Artist',
                'verbose_name_plural': 'Visual Artists',
                'ordering': ['vis_show_date_start'],
            },
        ),
        migrations.CreateModel(
            name='Archiveimagefiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archive_image_id', models.CharField(max_length=100, null=True)),
                ('archive_image_name', models.CharField(max_length=100, null=True)),
                ('archive_fk', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='image_files', to='schedule.archivedshowimagedata')),
            ],
        ),
    ]
