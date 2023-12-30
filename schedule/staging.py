 import django
django.setup()
from django.views import View
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from schedule.models import Music_artist_listing, Visual_artist_listing, Extra_curriucular_listing, Archiveimagefiles
from schedule.forms import ContactForm
from .signals import contact_form_saved
import os
import vimeo
from django.core.mail import EmailMessage
from django.urls import reverse_lazy
from django.http import JsonResponse
from google.oauth2 import service_account
from googleapiclient.discovery import build
from revolt_annex import settings
 
 SCOPES = ['https://www.googleapis.com/auth/drive']
 SERVICE_ACCOUNT_FILE = os.path.join(settings.BASE_DIR, 'schedule', 'taos-revolt-drive-0911d2bbf6a0.json')
   #Replace with your Google Drive directory ID

 class GoogleAPIView(TemplateView):
     template_name = 'schedule/google_api_test.html'
   
     #connect to API
     def get(self, request, *args, **kwargs):
         context = self.get_context_data(**kwargs)
         try:
             credentials = service_account.Credentials.from_service_account_file(
             SERVICE_ACCOUNT_FILE, scopes=SCOPES
         )
             service = build('drive', 'v3', credentials=credentials)
             query = f"'{DIRECTORY_ID}' in parents"
             files = service.files().list(q=query, fields="files(name, id)").execute()
             response = files.get('files', [])
             context['drive_files'] = response
             for data in response:
                 img_response = Archiveimagefiles(
                     archive_image_id=data['id'],
                     archive_image_name=data['name'],
                 )
                 img_response.save()
             for i in context['drive_files']:
                  file_metadata = service.files().get(fileId=i['id']).execute()
                  print(file_metadata)     
         except Exception as e:
             # Handle any exceptions that might occur
             context['error'] = str(e)
             print(e)
            

         return self.render_to_response(context)