# Generated by Django 4.2.1 on 2023-07-09 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0018_extra_curriucular_listing_class_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heads_up_music',
            name='artist_name',
            field=models.CharField(max_length=50),
        ),
    ]