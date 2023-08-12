# signals.py
from .models import Receive_email_updates
from django.db.models.signals import Signal
from django.dispatch import receiver

# Define a custom signal
contact_form_saved = Signal()

@receiver(contact_form_saved)
def handle_contact_form_saved(sender, **kwargs):
    name = kwargs.get("name")
    email_consent = kwargs.get("email_consent")
    user_email = kwargs.get("user_email")

    if email_consent:
        Receive_email_updates.objects.create(emailform_name=name, emailform_email=user_email, emailform_consent=True)
        print(f"Saved contact submission: {name}, email_consent={email_consent}, user_email={user_email}")