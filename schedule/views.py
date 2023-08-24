from django.views import View
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import TemplateView
from .models import Music_artist_listing, Visual_artist_listing, Extra_curriucular_listing
import requests
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from.signals import contact_form_saved



# Define a custom signal




class ContactUsView(View):
    def post(self, request):
        from_email = settings.DEFAULT_FROM_EMAIL
        contact_form = ContactForm(request.POST)
        
        if contact_form.is_valid():
            subject = contact_form.cleaned_data['subject']
            user_email = contact_form.cleaned_data['email']
            name = contact_form.cleaned_data['name']
            message = contact_form.cleaned_data['message']
            email_consent = contact_form.cleaned_data['email_consent']
            print('got all data')
            body = {
                'name': name,
                'message': message,
            }
            
            message = "\n".join(body.values())
            
            try:
                send_mail(subject, message, from_email, [user_email])
                print('email sent')

                # Emit the custom signal with additional args
                contact_form_saved.send(
                    sender=self.__class__,
                    name=name,
                    email_consent=email_consent,
                    user_email=user_email
                )
                print('signal sent well')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            
            return redirect('annex_home')
        
        return redirect('annex_home')






class AnnexHomeView(TemplateView):
    template_name = 'schedule/master-new.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # google_api_key = env.str('PROXY_GOOGLE')

        # nearby_params = {
        #     "rankby": "prominence",
        #     "location": "36.4107818,-105.5711364",
        #     "radius": "1500",
        #     "type": "bar",
        #     "key": google_api_key,
        # }
        # nearby_api_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
        # nearby_data = requests.get(nearby_api_url, params=nearby_params).json()

        # place_ids = [result["place_id"] for result in nearby_data.get("results", [])]

        # def get_place_info(place_id):
        #     response = requests.get(f"https://maps.googleapis.com/maps/api/place/details/json", params={"place_id": place_id, "key": google_api_key})
        #     return response.json()

        # bars = ['bar1', 'bar2', 'bar3']
        # bar_nearby_data_context = {
        #     bar: get_place_info(place_id)
        #     for bar, place_id in zip(bars, place_ids[:3])
        # }

        # place_image_list = [place_image_value for result in nearby_data.get("results", []) for place_image_value in result.get("photos", [])]

        context.update({
            'range_reset': [str(i) for i in range(2, 10)],
            'show_listing': Music_artist_listing.objects.all().order_by('show_date').values(),
            'gallery_listing': Visual_artist_listing.objects.all().values(),
            'extra_curricular_listing': Extra_curriucular_listing.objects.all().values(),
            # 'bars_nearby': bar_nearby_data_context,
            # 'place_image_list': place_image_list,
            'contact_form': ContactForm(),
            # 'api_key': google_api_key,
        })
        return context


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





