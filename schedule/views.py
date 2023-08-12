from django.views import View
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import TemplateView
from .models import Music_artist_listing, Visual_artist_listing, Extra_curriucular_listing, Receive_email_updates
import requests
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from.signals import contact_form_saved
from django.dispatch import receiver
import environ
from .signals import contact_form_saved  # Import the signal


environ.Env.read_env()
env = environ.Env(interpolate=True)


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
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            
            return redirect('annex_home')
        
        return redirect('annex_home')



# home class view

class AnnexHomeView(TemplateView):
    template_name = 'annex_master_backup.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        google_api_key = env.str('PROXY_GOOGLE')

        nearby_api_params_keys = ("rankby=", "&location=", "&radius=", "&type=")
        nearby_api_params_values = ("prominence", "36.4107818%2C-105.5711364", "1500", "bar")
        places_info_api = 'https://maps.googleapis.com/maps/api/place/details/json?place_id='
        bars = ['bar1', 'bar2', 'bar3']

        nearby_api_url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?{nearby_api_params_keys[0]}{nearby_api_params_values[0]}{nearby_api_params_keys[1]}{nearby_api_params_values[1]}{nearby_api_params_keys[2]}{nearby_api_params_values[2]}{nearby_api_params_keys[3]}{nearby_api_params_values[3]}&key={google_api_key}"
        con_1 = requests.get(nearby_api_url)
        nearby_data = con_1.json()

        place_id_list = [place_id_value for bar_data_int in nearby_data['results'] for place_id_key, place_id_value in bar_data_int.items() if place_id_key == "place_id"]

        place_image_list = [place_image_value for hotel_image_data in nearby_data['results'] for place_image_key, place_image_value in hotel_image_data.items() if place_image_key == "photos"]

        bar_nearby = []
        for place_id_inter in place_id_list[0:3]:
            con_2 = requests.get(places_info_api + place_id_inter + google_api_key)
            bar_data_int_1 = con_2.json()
            bar_nearby.append(bar_data_int_1)

        bar_nearby_data_context = dict(zip(bars, bar_nearby))
        show_listing = Music_artist_listing.objects.all().order_by('show_date').values()
        gallery_listing = Visual_artist_listing.objects.all().values()
        extra_curricular_listing = Extra_curriucular_listing.objects.all().values()
        contact_form = ContactForm()
        range_reset = [str(i) for i in range(2,10)]

        context['range_reset'] = range_reset
        context['show_listing'] = show_listing
        context['gallery_listing'] = gallery_listing
        context['extra_curricular_listing'] = extra_curricular_listing
        context['bars_nearby'] = bar_nearby_data_context
        context['place_image_list'] = place_image_list
        context['contact_form'] = contact_form
        context['api_key'] = env.str('PROXY_GOOGLE')
        return context

    








