from django.apps import AppConfig



class ArchiveConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'schedule'
    verbose_name = 'Art and Music Schedule'

    def ready(self):
        # Import signal handlers
        import schedule.signals

# archive/__init__.py
default_app_config = 'archive.apps.ArchiveConfig'
