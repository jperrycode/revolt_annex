# Generated by Django 4.2.6 on 2024-01-08 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='archiveimagefiles',
            name='archive_img_height',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='archiveimagefiles',
            name='archive_img_width',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
