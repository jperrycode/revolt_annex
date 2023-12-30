from typing import Any
from django import forms
from django.forms import ModelForm
from django.core.validators import EmailValidator
from .models import Archivedshowimagedata, Archiveimagefiles, Receive_email_updates

from django.forms import inlineformset_factory

# from django.conf import settings
# from django.core.mail import send_mail

class ContactForm(forms.ModelForm):
        class Meta:
            model = Receive_email_updates
            fields = ('emailform_name','emailform_email', 'emailform_subject', 'emailform_message', 'emailform_consent')

            widgets = {
                'emailform_name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Your Name'}),
                'emailform_email': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Your Email'}),
                'emailform_subject': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Subject'}),
                'emailform_message': forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Message'}),
                'emailform_consent': forms.CheckboxInput(attrs={'class':'form-control'}),
            }
           

                




class ArchiveimagefilesForm(forms.ModelForm):
    class Meta:
        model = Archiveimagefiles
        fields = '__all__'
        
  

ArchiveimagefilesFormSet = inlineformset_factory(Archivedshowimagedata, Archiveimagefiles, form=ArchiveimagefilesForm, extra=1)