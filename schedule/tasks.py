#tasks.py

from celery import shared_task
from django.core.mail import send_mail
from revolt_annex import settings

@shared_task(bind=True)
def send_notification_mail(self, subject, email, message):
    send_mail(
        subject=subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email],
        fail_silently=False,
        )
    return "Done"