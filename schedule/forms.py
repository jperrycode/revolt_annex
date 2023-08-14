from django import forms
from django.forms import ModelForm
from django.core.validators import EmailValidator
from .models import Archivedshowimagedata, Archiveimagefiles

from django.forms import inlineformset_factory

# from django.conf import settings
# from django.core.mail import send_mail

class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form_control', 'id':'name', 'type':'text','placeholder':'Your name', }), required=True, max_length=50)
    email = forms.EmailField(validators=[EmailValidator()], required=True, max_length=50)
    subject = forms.CharField(required=True, max_length=100)
    message = forms.CharField(widget=forms.Textarea, max_length=2000)
    email_consent = forms.BooleanField()




class ArchiveimagefilesForm(forms.ModelForm):
    class Meta:
        model = Archiveimagefiles
        fields = '__all__'

ArchiveimagefilesFormSet = inlineformset_factory(Archivedshowimagedata, Archiveimagefiles, form=ArchiveimagefilesForm, extra=1)