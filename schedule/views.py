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
# from google.oauth2 import service_account
# from googleapiclient.discovery import build
from revolt_annex import settings

# SCOPES = ['https://www.googleapis.com/auth/drive']
# SERVICE_ACCOUNT_FILE = os.path.join(settings.BASE_DIR, 'schedule', 'taos-revolt-drive-0911d2bbf6a0.json')
# DIRECTORY_ID = '1eParAfXZy-cPhxzX7uNbDQkFZ2L-WWI8'  # Replace with your Google Drive directory ID

# class GoogleAPIView(TemplateView):
#     template_name = 'schedule/google_api_test.html'
   
#     #connect to API
#     def get(self, request, *args, **kwargs):
#         context = self.get_context_data(**kwargs)
#         try:
#             credentials = service_account.Credentials.from_service_account_file(
#             SERVICE_ACCOUNT_FILE, scopes=SCOPES
#         )
#             service = build('drive', 'v3', credentials=credentials)
#             query = f"'{DIRECTORY_ID}' in parents"
#             files = service.files().list(q=query, fields="files(name, id)").execute()
#             response = files.get('files', [])
#             context['drive_files'] = response
#             for data in response:
#                 img_response = Archiveimagefiles(
#                     archive_image_id=data['id'],
#                     archive_image_name=data['name'],
#                 )
#                 img_response.save()
#             # for i in context['drive_files']:
#             #     file_metadata = service.files().get(fileId=i['id']).execute()
#             #     print(file_metadata)     
#         except Exception as e:
#             # Handle any exceptions that might occur
#             context['error'] = str(e)
#             print(e)
            

#         return self.render_to_response(context)


# Define a custom signal
class Contact_form_view(CreateView):
    form_class = ContactForm
    template_name = 'schedule/contact_index.html'
    success_url = reverse_lazy('contact-us-success/')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_form'] = ContactForm()
        return context




class ContactUsView(View):
    def post(self, request):
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            print('isvalid')
            subject = contact_form.cleaned_data['emailform_subject']
            user_email = contact_form.cleaned_data['emailform_email']
            name = contact_form.cleaned_data['emailform_name']
            message = contact_form.cleaned_data['emailform_message']
            # email_consent = contact_form.cleaned_data['email_consent']
            email_consent = 'False'
            body = {
                'name': str(name),
                'message': f'Contact form Message from {user_email} \n {message} \n thank you ',
            }

            message = "\n".join(body.values())

            try:
                email = EmailMessage(
                    subject=str(subject),
                    body=message,
                    from_email='contact@taosrevolt.com',
                    to=['taosrevolt@gmail.com'],
                    reply_to=['contact@taosrevolt.com'],
                    headers={'Content-Type': 'text/plain'},
                )
                email.send()

                print('Email sent successfully!')
                # Emit the custom signal with additional args
                contact_form_saved.send(
                    sender=self.__class__,
                    name=name,
                    email_consent=email_consent,
                    user_email=user_email,
                    user_message=message
                )
                print('signal sent well')

                # Create the success context
                success_context = {
                    'subject': subject,
                    'name': name,
                    'user_email': user_email,
                    'message': message,
                    'email_consent': email_consent,
                }

                # Render the success template
                return render(request, 'schedule/contact_success.html', {'data':success_context })

            except Exception as e:
                print(f'An error occurred: {str(e)}')
                return render(request, 'schedule/contact_fail.html')

        else:
            # Form is not valid, print error messages to the CLI
            for field, errors in contact_form.errors.items():
                for error in errors:
                    print(f"Field: {field}, Error: {error}")

            return render(request, 'schedule/contact_fail.html')


class ContactSuccessView(View):
    template_name = 'schedule/contact_success.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_form'] = ContactForm()
        return context
    
class ClassesView(TemplateView):
    template_name = 'schedule/classes_section_index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['classes_data'] = Extra_curriucular_listing.objects.all().values()
        return context
    
class RevoltView(TemplateView):
    template_name = 'schedule/gallery_all_swtiching.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gallery_listing'] = Visual_artist_listing.objects.all().values()
        return context
    
    
class ResetView(TemplateView):
    template_name = 'schedule/reset_venue_index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['music_artist_listing'] = Music_artist_listing.objects.all().values()
        # context['vimeo_video_data'] = self.get_vimeo_videos()
        return context
    
    # def get_vimeo_videos(self):
    #     vimeo_token = str(os.getenv('VIMEO_ACCESS_TOKEN'))  # Replace with your Vimeo access token

    #     try:
    #         # Initialize the Vimeo client with the provided access token
    #         client = vimeo.VimeoClient(
    #             token=vimeo_token,
    #         )

    #         # Use the client to make API requests
    #         videos_data = client.get('/me/videos')
    #         videos_context = videos_data.json()
            
    #         # with open('vimeo_data.json', 'w', encoding='utf-8') as f:
    #         #     json.dump(videos_context, f, indent=4)

    #         return videos_context
    #     except Exception as e:
    #         print(f"Failed to fetch Vimeo videos. Error: {str(e)}")

    #     return []

#   

# class AnnexHomeView(TemplateView):
#     template_name = 'schedule/master-new.html'
#     videos_data = []
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         vimeo_client_id = str(os.getenv('VIMEO_CLIENT_ID'))
#         vimeo_secret = str(os.getenv('VIMEO_SECRET'))
#         vimeo_token = str(os.getenv('VIMEO_ACCESS_TOKEN'))

#         vimeo_auth_url = 'https://api.vimeo.com/oauth/authorize/client'
#         auth_data = {
#             'grant_type': 'client_credentials',
#             'scope': 'private',
#                     }
#         auth_response = requests.post(vimeo_auth_url, data=auth_data, auth=(vimeo_client_id, vimeo_secret))
#         vimeo_token = auth_response.json()['access_token']
#         video_url = 'https://api.vimeo.com/me/videos'
#         headers = {'Authorization': f'Bearer {vimeo_token}',}

#         vimeo_response = requests.get(video_url, headers=headers)
        
#         if vimeo_response.status_code == 200:
#             videos_data = vimeo_response.json()
#             print(videos_data)
#         else:
#             print(f"Failed to fetch videos. Status code: {vimeo_response.status_code}")

 


#         context.update({
#             'range_reset': [str(i) for i in range(2, 10)],
#             'show_listing': Music_artist_listing.objects.all().order_by('show_date').values(),
#             'gallery_listing': Visual_artist_listing.objects.all().values(),
#             'extra_curricular_listing': Extra_curriucular_listing.objects.all().values(),
#             'vimeo_video_data': videos_data,
#             'contact_form': ContactForm(),
            
#         })
#         return context







class AnnexHomeView(TemplateView):
    # template_name = 'schedule/master-new.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['range_reset'] = [str(i) for i in range(2, 10)]
        context['gallery_listing'] = Visual_artist_listing.objects.all().values()
        context['music_artist_listing'] = Music_artist_listing.objects.all().values()
        
        return context







# class ArchiveView(TemplateView):
#     template_name = 'schedule/contact-us.html'  # Replace with your actual template path

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context.update({'extra_curricular_listing': Extra_curriucular_listing.objects.all().values(),})
#         return context

# 




