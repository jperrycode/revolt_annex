from django.contrib import admin


# Register your models here.

from .models import Music_artist_listing, Visual_artist_listing, Extra_curriucular_listing, Nearby_accomodations, Heads_up_music, Receive_email_updates

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
    list_display = ("artist_name", "show_date_start", "age_restriction",)

admin.site.register(Visual_artist_listing, VisualSheduleAdmin)


#register class schedule
class ExtraCurricularAdmin(admin.ModelAdmin):
    list_display = ("class_name", "class_date", "class_location")

admin.site.register(Extra_curriucular_listing, ExtraCurricularAdmin)

#register accomadation model

class AccomodationAdmin(admin.ModelAdmin):
    list_display = ("accom_name", "accom_phone", "accom_phone")

admin.site.register(Nearby_accomodations, AccomodationAdmin)

class HeadsUpMusicAdmin(admin.ModelAdmin):
    list_display = ("event_name", "event_time", "artist_name")

admin.site.register(Heads_up_music, HeadsUpMusicAdmin)

class EmailConsent(admin.ModelAdmin):
    list_display = ("emailform_name", "emailform_email", "emailform_consent")
    list_display_links = ('emailform_name',)
    list_filter = ('emailform_consent',)

admin.site.register(Receive_email_updates, EmailConsent)