from typing import Any
from django.contrib import admin
import flickrapi

# Import necessary models and modules
from .models import (
    Music_artist_listing, Visual_artist_listing, Extra_curriucular_listing,
    Receive_email_updates, Archiveimagefiles, Archivedshowimagedata
)

from revolt_annex import settings
import os


# Customizing admin site header
class MyAdminSite(admin.AdminSite):
    site_header = "Revolt/Reset Admin"


# Creating an instance of the customized admin site
admin_site = MyAdminSite(name="admin")


# Define Music Schedule Admin model
class MusicScheduleAdmin(admin.ModelAdmin):
    list_display = ("artist_name", "show_date", "entry_price", "music_artist_image")


# Register Music_artist_listing model with MusicScheduleAdmin
admin.site.register(Music_artist_listing, MusicScheduleAdmin)


# Define Visual Schedule Admin model
class VisualSheduleAdmin(admin.ModelAdmin):
    list_display = ("vis_artist_name", "vis_show_date_start", "age_restriction",)


# Register Visual_artist_listing model with VisualSheduleAdmin
admin.site.register(Visual_artist_listing, VisualSheduleAdmin)


# Define Extra Curricular Admin model
class ExtraCurricularAdmin(admin.ModelAdmin):
    list_display = ("class_name", "class_day", "class_location")


# Register Extra_curriucular_listing model with ExtraCurricularAdmin
admin.site.register(Extra_curriucular_listing, ExtraCurricularAdmin)


# Define Email Consent Admin model
class EmailConsent(admin.ModelAdmin):
    list_display = ("emailform_name", "emailform_email", "emailform_consent")
    list_display_links = ('emailform_name',)
    list_filter = ('emailform_consent',)


# Register Receive_email_updates model with EmailConsent
admin.site.register(Receive_email_updates, EmailConsent)


# Define the Inline model for Archiveimagefiles
class Model2Inline(admin.StackedInline):
    model = Archiveimagefiles
    extra = 1


# Define Fullarchiveform model
def remove_duplicates_by_key(seq, key):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if x[key] not in seen and not seen_add(x[key])]


class Fullarchiveform(admin.ModelAdmin):
    model = Archivedshowimagedata
    inlines = [Model2Inline]
    list_display = ('archive_show_name', 'archive_start_date', 'archive_end_date', 'archive_folder_id')

    # Overriding save_model method to handle saving images from Flickr
    def save_model(self, request, obj, form, change, photo_height=None):
        try:
            # Extract form data
            archive_show_name = form.cleaned_data.get('archive_show_name')
            archive_artist_name = form.cleaned_data.get('archive_artist_name')
            archive_start_date = form.cleaned_data.get('archive_start_date')
            archive_end_date = form.cleaned_data.get('archive_end_date')
            archive_folder_id = form.cleaned_data.get('archive_folder_id')
            archive_artist_web = form.cleaned_data.get('archive_artist_web')

            # Update object attributes
            obj.archive_show_name = archive_show_name
            obj.archive_artist_name = archive_artist_name
            obj.archive_start_date = archive_start_date
            obj.archive_end_date = archive_end_date
            obj.archive_folder_id = archive_folder_id
            obj.archive_artist_web = archive_artist_web

            super().save_model(request, obj, form, change)

            # Fetch main object ID
            main_object_id = obj.pk

            # Fetch images from Flickr
            flickr = flickrapi.FlickrAPI(settings.flickr_key, settings.flickr_secret, format='parsed-json')
            photos = flickr.photosets.getPhotos(api_key=settings.flickr_key, photoset_id=archive_folder_id,
                                                user_id=settings.flickr_user_id)

            # Process image details and save the first 10 images sorted by height into Archiveimagefiles model
            image_details = []
            for photo in photos['photoset']['photo']:
                photo_id = photo['id']
                photo_title = photo['title']
                photo_secret = photo['secret']
                photo_server = photo['server']
                photo_url = flickr.photos.getSizes(api_key=settings.flickr_key, photo_id=photo_id)['sizes']['size']
                for size in photo_url:
                    photo_height = size['height']
                    photo_width = size['width']

                    image_details.append({
                        'photo_id': photo_id,
                        'photo_title': photo_title,
                        'photo_secret': photo_secret,
                        'photo_server': photo_server,
                        'photo_height': photo_height,
                        'photo_width': photo_width,
                    })

                print("Processed image details:")

            # Sort images by height and get the first 10
            sorted_images = sorted(image_details, key=lambda x: (x['photo_height'], x['photo_id']))
            unique_sorted_images = remove_duplicates_by_key(sorted_images, 'photo_id')
            for i in sorted_images:
                print('got height sorted', i)
            sorted_images_first_10 = unique_sorted_images[:10]

            print("Sorted images (first 10):")

            # Save the first 10 images into Archiveimagefiles model
            for image in sorted_images_first_10:
                img_response = Archiveimagefiles(
                    archive_img_width=image['photo_width'],
                    archive_img_height=image['photo_height'],
                    archive_image_server=image['photo_server'],
                    archive_image_secret=image['photo_secret'],
                    archive_image_id=image['photo_id'],
                    archive_image_name=image['photo_title'],
                    archive_fk_id=main_object_id
                )
                img_response.save()

        except Exception as e:
            print(e)


# Register Archivedshowimagedata model with Fullarchiveform
admin.site.register(Archivedshowimagedata, Fullarchiveform)
