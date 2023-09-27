import django
django.setup()
from django.views import View
from django.shortcuts import redirect
from django.views.generic import TemplateView
from schedule.models import Music_artist_listing, Visual_artist_listing, Extra_curriucular_listing
from schedule.forms import ContactForm
from.signals import contact_form_saved
import os
import vimeo
import smtplib 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.conf import settings
from django.core.mail import EmailMessage





# Define a custom signal




class ContactUsView(View):
    def post(self, request):
        contact_form = ContactForm(request.POST)
        
        if contact_form.is_valid():
            print('success 1')
            # smtp_server = str(settings.EMAIL_HOST)
            # smtp_port = 587  # For TLS/STARTTLS

            # email = str(settings.EMAIL_HOST_USER)
            # password = str(settings.EMAIL_HOST_PASSWORD)

            subject = contact_form.cleaned_data['subject']
            print('success 2')
            user_email = contact_form.cleaned_data['email']
            print('success 3')
            name = contact_form.cleaned_data['name']
            print('success 4')
            message = contact_form.cleaned_data['message']
            print('success 5')
            email_consent = contact_form.cleaned_data['email_consent']
            print('success 6')
            print('got all data')
            body = {
                'name': str(name),
                'message': f'CONTENT == {message}, {user_email} thank you ',
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
                    user_email=user_email
                )
                print('signal sent well')
            except Exception as e:
                print(f'An error occurred: {str(e)}')
            
            return redirect('annex_home')
        else:
            # Form is not valid, print error messages to the CLI
            for field, errors in contact_form.errors.items():
                for error in errors:
                    print(f"Field: {field}, Error: {error}")

        return redirect('annex_home')






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
    template_name = 'schedule/master-new.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['range_reset'] = [str(i) for i in range(2, 10)]
        context['gallery_listing'] = Visual_artist_listing.objects.all().values()
        context['extra_curricular_listing'] = Extra_curriucular_listing.objects.all().values()
        context['vimeo_video_data'] = self.get_vimeo_videos()
        context['contact_form'] = ContactForm()
        context['music_artist_listing'] = Music_artist_listing.objects.all().values()
        return context

    def get_vimeo_videos(self):
        vimeo_token = str(os.getenv('VIMEO_ACCESS_TOKEN'))  # Replace with your Vimeo access token

        try:
            # Initialize the Vimeo client with the provided access token
            client = vimeo.VimeoClient(
                token=vimeo_token,
            )

            # Use the client to make API requests
            videos_data = client.get('/me/videos')
            videos_context = videos_data.json()
            
            # with open('vimeo_data.json', 'w', encoding='utf-8') as f:
            #     json.dump(videos_context, f, indent=4)

            return videos_context
        except Exception as e:
            print(f"Failed to fetch Vimeo videos. Error: {str(e)}")

        return []





# class ArchiveView(TemplateView):
#     template_name = 'schedule/contact-us.html'  # Replace with your actual template path

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context.update({'extra_curricular_listing': Extra_curriucular_listing.objects.all().values(),})
#         return context

# class AnnexTestView(TemplateView):
#     template_name = 'schedule/dev_template.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # google_api_key = env.str('PROXY_GOOGLE')

#         # nearby_params = {
#         #     "rankby": "prominence",
#         #     "location": "36.4107818,-105.5711364",
#         #     "radius": "1500",
#         #     "type": "bar",
#         #     "key": google_api_key,
#         # }
#         # nearby_api_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
#         # nearby_data = requests.get(nearby_api_url, params=nearby_params).json()

#         # place_ids = [result["place_id"] for result in nearby_data.get("results", [])]

#         # def get_place_info(place_id):
#         #     response = requests.get(f"https://maps.googleapis.com/maps/api/place/details/json", params={"place_id": place_id, "key": google_api_key})
#         #     return response.json()

#         # bars = ['bar1', 'bar2', 'bar3']
#         # bar_nearby_data_context = {
#         #     bar: get_place_info(place_id)
#         #     for bar, place_id in zip(bars, place_ids[:3])
#         # }


#         context.update({
#             'show_listing': Music_artist_listing.objects.all().order_by('show_date').values(),
#             'gallery_listing': Visual_artist_listing.objects.all().values(),
#             'extra_curricular_listing': Extra_curriucular_listing.objects.all().values(),
           
#             'contact_form': ContactForm(),
#             # 'api_key': google_api_key,
#         })
#         return context





