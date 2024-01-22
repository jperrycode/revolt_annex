import django
django.setup()
from typing import Any
from django.views import View
from django.views.generic import DetailView
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from schedule.models import Music_artist_listing, Visual_artist_listing, Extra_curriucular_listing
from schedule.forms import ContactForm
from .signals import contact_form_saved
from schedule.models import Archiveimagefiles, Archivedshowimagedata
import os
import vimeo
from django.core.mail import EmailMessage
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.db.models import Prefetch
from revolt_annex import settings
from django.shortcuts import get_object_or_404
from django.shortcuts import reverse


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
                return render(request, 'schedule/contact_success.html', {'data': success_context})

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
        context['classes_data'] = Extra_curriucular_listing.objects.all()
        return context


class RevoltView(TemplateView):
    template_name = 'schedule/gallery_all_swtiching.html'

    def get_context_data(self, **kwargs):
        try:

            context = super().get_context_data(**kwargs)

            # Fetching data efficiently
            gallery_listing = Visual_artist_listing.objects.all()

            # Fetching Archivedshowimagedata instances and prefetching specific fields from related Archiveimagefiles instances
            image_show_data = (
                Archivedshowimagedata.objects
                .prefetch_related(
                    Prefetch('image_files', queryset=Archiveimagefiles.objects.all())
                )
                .all()
            )

            context['gallery_listing'] = gallery_listing
            context['archive_show_data'] = image_show_data
        except Exception as e:
            print(e)

        return context


class ResetView(TemplateView):
    template_name = 'schedule/reset_venue_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['music_artist_listing'] = Music_artist_listing.objects.all().values()
        # context['vimeo_video_data'] = self.get_vimeo_videos()
        return context


class ArchivePageView(DetailView):
    template_name = 'schedule/archive-list-view-new.html'
    model = Archivedshowimagedata

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        try:
            # Get the primary key (pk) from URL kwargs
            pk = self.kwargs.get('pk')

            # Retrieve the parent model instance (Archivedshowimagedata) based on the pk
            show_instance_data = get_object_or_404(Archivedshowimagedata, pk=pk)

            # Retrieve related Archiveimagefiles instances for the Archivedshowimagedata instance
            related_images = show_instance_data.image_files.all().order_by('archive_img_width')

            context['show_instance_data'] = show_instance_data
            context['related_images'] = related_images

        except Archivedshowimagedata.DoesNotExist:
            # Handle the case where the Archivedshowimagedata instance doesn't exist
            context['show_instance_data'] = None
            context['related_images'] = None

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
