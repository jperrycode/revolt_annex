from django.db import models
from revolt_annex import settings


EVENT_GENRE_CHOICES = [
    ('rap', 'Rap'),
    ("Drum and Bass", 'Drum and Bass'),
    ("House", 'House'),
    ('Techno', 'Techno'),
    ('Rock and Roll', 'Rock and Roll'),
    ('Folk', 'Folk'),
    ('Scheduled Class', 'Scheduled Class'),
    ('Bass Music', 'Bass Music'),
    ('Other', 'Other'),
    ('UK Grime', 'UK Grime'),
    ('Hip Hop', 'Hip Hop'),
    ]

ACCOM_TYPE_CHOICES = [
  ('Hotel', 'Hotel'),
  ('Air-BNB', 'Air-BNB'),
  ('Bed-n-Breakfast', 'Bed-n-Breakfast'),
  ('Camping', 'Camping'),                    
  ]

# artist information model
class Music_artist_listing(models.Model):
  artist_name = models.CharField(max_length=50, default='', blank=True, null=False)
  artist_genre = models.CharField(max_length=255, choices=EVENT_GENRE_CHOICES, default='')
  # music_show_datetime = models.DateTimeField(blank=True, verbose_name="date and time", default='2025-07-01 10:10')
  show_date = models.DateField(auto_now=False, auto_now_add=False)
  show_time = models.TimeField(auto_now=False, auto_now_add=False)
  artist_bio = models.CharField(max_length=255, default='', blank=True, null=False)
  artist_insta = models.CharField(max_length=255, blank=True, null=True)
  artist_website = models.CharField(max_length=255, blank=True, null=True)
  artist_music_page = models.CharField(max_length=200, default='search your self')
  # artist_image = models.ImageField(upload_to='images/')
  entry_price = models.FloatField(null=True)

  class Meta:
    verbose_name = "Musician"
    verbose_name_plural = "Musicians"
    ordering = ["show_date"]

  def __str__(self):
        return self.artist_name 


# gallery information model
class Visual_artist_listing(models.Model):
  visual_show_name = models.CharField(max_length=50, default='Show Title', blank=False)
  artist_name = models.CharField(max_length=50, default='', blank=True, null=False)
  artist_medium = models.CharField(max_length=255, default='')
  show_date_start = models.DateField(auto_now=False, auto_now_add=False)
  show_date_end = models.DateField(auto_now=False, auto_now_add=False)
  artist_bio = models.CharField(max_length=255, default='', blank=True, null=False)
  artist_website = models.CharField(max_length=255, blank=True, null=True)
  entry_price = models.FloatField(null=True, blank=True)
  age_restriction = models.BooleanField(default=False)

  class Meta:
    ordering = ['show_date_start']
    verbose_name = "Visual Artist"
    verbose_name_plural = "Visual Artists"



class Extra_curriucular_listing(models.Model):
  class_name = models.CharField(max_length=50, default='', blank=True, null=False)
  class_teacher = models.CharField(max_length=50, default="", blank=False, null=False)
  class_description = models.TextField(blank=False, null=False)
  class_date = models.DateField(auto_now=False, auto_now_add=False)
  class_time = models.TimeField(auto_now=False, auto_now_add=False)
  class_location = models.CharField(max_length=50, default='Revolt Annex', null=False, blank=False)
  class_price = models.FloatField(null=True, blank=True)

  class Meta:
    ordering = ['class_date']
    verbose_name = "Class listing"
    verbose_name_plural = "Class Listings"


class Nearby_accomodations(models.Model):
  accom_name = models.CharField(max_length=50, blank=False, null=False, primary_key=True)
  accom_type = models.CharField(max_length=255, choices=ACCOM_TYPE_CHOICES, default='')
  accom_distance = models.FloatField(null=False, blank=False)
  accom_phone = models.CharField(max_length=12, blank=True, null=True)
  accom_url = models.CharField(max_length=255, blank=False, null=True)

  class Meta:
    verbose_name = "Nearby Accomadation"
    verbose_name_plural = "Nearby Accomadations"

#     def is_edm(self):
#         return self.genre_type in self.EVENT_GENRE_CHOICES


class Heads_up_music(models.Model):
  event_name = models.CharField(max_length=50, blank=False, null=False)
  event_date = models.DateField(auto_now=False,auto_now_add=False)
  event_time = models.TimeField(auto_now=False, auto_now_add=False)
  artist_name = models.CharField(max_length=50, blank=False, null=False)
  event_description = models.CharField(max_length=255, blank=False, null=False)

  class Meta:
    ordering = ['event_date']
    verbose_name = "HUM Event"
    verbose_name_plural = "HUM Events"