# Generated by Django 4.2.4 on 2023-08-14 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0025_archivedshowimagedata_archiveimagefiles'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='archivedshowimagedata',
            options={'ordering': ['archive_end_date'], 'verbose_name': 'Archive Image', 'verbose_name_plural': 'Archive Images'},
        ),
        migrations.AddField(
            model_name='archivedshowimagedata',
            name='archive_end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='archivedshowimagedata',
            name='archive_start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]