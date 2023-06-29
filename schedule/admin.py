from django.contrib import admin

# Register your models here.

from .models import Music_artist_listing, Visual_artist_listing, Extra_curriucular_listing, Nearby_accomodations

#register artist listing model
class MusicScheduleAdmin(admin.ModelAdmin):
    list_display = ("artist_name", "show_date", "entry_price",)

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
