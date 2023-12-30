from typing import Any
from django.contrib import admin


# Register your models here.

from .models import Music_artist_listing, Visual_artist_listing, Extra_curriucular_listing, Heads_up_music, Receive_email_updates, Archiveimagefiles, Archivedshowimagedata
from .forms import ArchiveimagefilesFormSet
from django.core.exceptions import ObjectDoesNotExist
from google.oauth2 import service_account
from googleapiclient.discovery import build
from revolt_annex import settings
import os
#register artist listing model

class MyAdminSite(admin.AdminSite):
    site_header = "Revolt/Reset Admin"

admin_site = MyAdminSite(name="admin")


class MusicScheduleAdmin(admin.ModelAdmin):
    list_display = ("artist_name", "show_date", "entry_price", "music_artist_image")
    


#register artist listing model
admin.site.register(Music_artist_listing, MusicScheduleAdmin)

#Register visual artist gallery schedule
class VisualSheduleAdmin(admin.ModelAdmin):
    list_display = ("vis_artist_name", "vis_show_date_start", "age_restriction",)

admin.site.register(Visual_artist_listing, VisualSheduleAdmin)


#register class schedule
class ExtraCurricularAdmin(admin.ModelAdmin):
    list_display = ("class_name", "class_day", "class_location")

admin.site.register(Extra_curriucular_listing, ExtraCurricularAdmin)

#register accomadation model

# class AccomodationAdmin(admin.ModelAdmin):
#     list_display = ("accom_name", "accom_phone", "accom_phone")

# admin.site.register(Nearby_accomodations, AccomodationAdmin)

class HeadsUpMusicAdmin(admin.ModelAdmin):
    list_display = ("event_name", "event_time", "artist_name")

admin.site.register(Heads_up_music, HeadsUpMusicAdmin)

class EmailConsent(admin.ModelAdmin):
    list_display = ("emailform_name", "emailform_email", "emailform_consent")
    list_display_links = ('emailform_name',)
    list_filter = ('emailform_consent',)

admin.site.register(Receive_email_updates, EmailConsent)



    





class Model2Inline(admin.StackedInline):
    model = Archiveimagefiles
    extra = 1

    
class Fullarchiveform(admin.ModelAdmin):
    model = Archivedshowimagedata
    inlines = [Model2Inline]
    list_display = ('archive_show_name','archive_start_date','archive_end_date','archive_folder_id')
    
    
    def save_model(self, request, obj, form, change):
        SERVICE_ACCOUNT_FILE = os.path.join(settings.BASE_DIR, 'schedule', 'taos-revolt-drive-0911d2bbf6a0.json')
        
        try:
            archive_show_name = form.cleaned_data.get('archive_show_name')
            archive_artist_name = form.cleaned_data.get('archive_artist_name')
            archive_start_date = form.cleaned_data.get('archive_start_date')
            archive_end_date = form.cleaned_data.get('archive_end_date')
            archive_folder_id = form.cleaned_data.get('archive_folder_id')
            archive_artist_web = form.cleaned_data.get('archive_artist_web')
            
            
            
            obj.archive_show_name = archive_show_name
            obj.archive_artist_name = archive_artist_name
            obj.archive_start_date = archive_start_date
            obj.archive_end_date = archive_end_date
            obj.archive_folder_id = archive_folder_id
            obj.archive_artist_web = archive_artist_web
            
            super().save_model(request, obj, form, change)
            
            main_object_id = obj.pk
            
            SCOPES = ['https://www.googleapis.com/auth/drive'] 
            credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES
         )
            service = build('drive', 'v3', credentials=credentials)
            query = f"'{archive_folder_id}' in parents"
            files = service.files().list(q=query, fields="files(name, id)").execute()
            response = files.get('files', [])
             
            for data in response:
                img_response = Archiveimagefiles(
                archive_image_id=data['id'],
                archive_image_name=data['name'],
                archive_fk_id=main_object_id)
                 
                img_response.save()
             
                    
        except Exception as e:
             # Handle any exceptions that might occur
            print(e)   
            
        
        
        
         
        
    
    
    


admin.site.register(Archivedshowimagedata, Fullarchiveform)