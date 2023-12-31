from django.db import models




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
  show_date = models.DateField(auto_now=False, auto_now_add=False)
  show_time = models.TimeField(auto_now=False, auto_now_add=False)
  artist_bio = models.CharField(max_length=255, default='', blank=True, null=False)
  artist_insta = models.CharField(max_length=255, blank=True, null=True)
  artist_website = models.CharField(max_length=255, blank=True, null=True)
  artist_music_page = models.CharField(max_length=200, default='search your self')
  music_artist_image = models.ImageField(upload_to ='media/', null=True, blank=True)

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
  vis_artist_name = models.CharField(max_length=50, default='', blank=True, null=False)
  vis_artist_medium = models.CharField(max_length=255, default='')
  vis_show_date_start = models.DateField(auto_now=False, auto_now_add=False)
  vis_show_date_end = models.DateField(auto_now=False, auto_now_add=False)
  vis_artist_bio = models.TextField(default='', blank=True, null=False)
  vis_artist_website = models.CharField(max_length=255, blank=True, null=True)
  vis_entry_price = models.FloatField(null=True, blank=True)
  age_restriction = models.BooleanField(default=False)
  vis_image_url = models.URLField(max_length=250, null=True, blank=True)
  visual_artist_image = models.ImageField(upload_to ='media/', null=True, blank=True)


  class Meta:
    ordering = ['vis_show_date_start']
    verbose_name = "Visual Artist"
    verbose_name_plural = "Visual Artists"



class Extra_curriucular_listing(models.Model):
  class_name = models.CharField(max_length=50, default='', blank=True, null=False)
  class_teacher = models.CharField(max_length=50, default="", blank=False, null=False)
  class_description = models.TextField(blank=False, null=False)
  class_day = models.CharField(max_length=30, null=True, blank=True)
  class_time = models.TimeField(auto_now=False, auto_now_add=False)
  class_location = models.CharField(max_length=50, default='Revolt Annex', null=False, blank=False)
  class_price = models.FloatField(null=True, blank=True)
  image_url = models.URLField(max_length=250, null=True, blank=True)
  class_artist_image = models.ImageField(upload_to ='media/', null=True, blank=True)

  class Meta:
    verbose_name = "Class listing"
    verbose_name_plural = "Class Listings"


# class Nearby_accomodations(models.Model):
#   accom_name = models.CharField(max_length=50, blank=False, null=False, primary_key=True)
#   accom_type = models.CharField(max_length=255, choices=ACCOM_TYPE_CHOICES, default='')
#   accom_distance = models.FloatField(null=False, blank=False)
#   accom_phone = models.CharField(max_length=12, blank=True, null=True)
#   accom_url = models.CharField(max_length=255, blank=False, null=True)

#   class Meta:
#     verbose_name = "Nearby Accomadation"
#     verbose_name_plural = "Nearby Accomadations"

# #     def is_edm(self):
# #         return self.genre_type in self.EVENT_GENRE_CHOICES


class Heads_up_music(models.Model):
  event_name = models.CharField(max_length=50, blank=False, null=False)
  event_date = models.DateField(auto_now=False,auto_now_add=False)
  event_time = models.TimeField(auto_now=False, auto_now_add=False)
  artist_name = models.CharField(max_length=50, blank=False, null=False)
  event_description = models.CharField(max_length=255, blank=False, null=False)
  artist_image = models.ImageField(upload_to ='media/', null=True, blank=True)

  class Meta:
    ordering = ['event_date']
    verbose_name = "HUM Event"
    verbose_name_plural = "HUM Events"



class Receive_email_updates(models.Model):
  emailform_message = models.TextField(max_length=600, null=True, blank=False)
  emailform_email = models.EmailField(max_length=255, null=True, blank=False)
  emailform_name = models.CharField(max_length=50, null=True, blank=True)
  emailform_subject = models.CharField(max_length=50, null=True, blank=True)
  emailform_consent = models.BooleanField()

 
  



class Archivedshowimagedata(models.Model):
    archive_show_name = models.CharField(max_length=50, null=False)
    archive_artist_name = models.CharField(max_length=75, blank=True, null=True)
    archive_start_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    archive_end_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    archive_folder_id = models.CharField(max_length=50)

    class Meta:
      ordering = ['archive_end_date']
      verbose_name = "Archive Image"
      verbose_name_plural = "Archive Images"
    def __str__(self):
        return self.archive_show_name
    

class Archiveimagefiles(models.Model):
   archive_image_id = models.CharField(max_length=100, null=True)
   archive_image_name = models.CharField(max_length=100, null=True)
   archive_fk = models.ForeignKey(Archivedshowimagedata, on_delete=models.CASCADE, null=True)


class VimeoVideo(models.Model):
    video_id = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    # Add other fields as needed

    def __str__(self):
        return self.title