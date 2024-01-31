from django.apps import AppConfig




class ArchiveConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'schedule'
    verbose_name = 'Art and Music Schedule'

    def ready(self):
        # Import signal handlers from your app
        import schedule.signals  # Replace "schedule" with your app's name
#
#
# # archive/__init__.py
default_app_config = 'archive.apps.ArchiveConfig'


class ScheduleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'schedule'

