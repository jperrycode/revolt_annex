from django.apps import AppConfig
from background_task.models import Task
from background_task.models import Task
from django.db.models import F
from . import tasks  # Import your tasks module
from django.utils import timezone
from schedule.models import *


class ArchiveConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'schedule'
    verbose_name = 'Art and Music Schedule'

    def ready(self):
        # Import signal handlers from your app
        import schedule.signals  # Replace "schedule" with your app's name


# archive/__init__.py
default_app_config = 'archive.apps.ArchiveConfig'


class ScheduleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'schedule'

    def ready(self):
        # Schedule the task to run every 24 hours
        Task.objects.create(
            name='schedule.tasks.scan_and_move_rows',
            task='schedule.tasks.scan_and_move_rows',
            schedule_type=Task.DAILY,
            schedule='24:00',  # Run every 24 hours
        )
