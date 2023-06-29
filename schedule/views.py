from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from .models import Music_artist_listing, Visual_artist_listing, Extra_curriucular_listing, Nearby_accomodations
import requests
from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError






def annex_home_hotel_data():
  pass

# send email functionality 
def contact_us(request):
	if request.method == 'POST':
		contact_form = ContactForm(request.POST)
		if contact_form.is_valid():
			subject = contact_form.cleaned_data['subject'] 
			body = {            
			'name': contact_form.cleaned_data['name'],  
			'email': contact_form.cleaned_data['email'], 
			'message': contact_form.cleaned_data['message'], 
			}
			message = "\n".join(body.values())

			try:
				send_mail(subject, message, 'admin@example.com', ['admin@example.com']) 
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
		return render(request, "annex_home")
      
	contact_form = ContactForm()
  
  
	return render(request, "contact_redirect", {'contact_form':contact_form})


def contact_redirect(request):
     return redirect (annex_home)


def annex_music_schedule(request):
  show_listing = Music_artist_listing.objects.all().values()
  template = loader.get_template('annex_music_schedule.html')
  context = {'show_listing':show_listing}
  return HttpResponse(template.render(context, request))

def annex_home(request):
  google_api_key = "&key=AIzaSyBlib4QaWTu_44UfVXhmg3vJAgtAuU8PAM"
  # google_key = os.eviron.get('')
  pass_api_key = 'AIzaSyBlib4QaWTu_44UfVXhmg3vJAgtAuU8PAM'
  nearby_api_params_keys = ("rankby=","&location=","&radius=","&type=")
  nearby_api_params_values = ("prominence","36.4107818%2C-105.5711364","1500","lodging")
  places_info_api = 'https://maps.googleapis.com/maps/api/place/details/json?place_id='
  nearby_api_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?"
  hotel_nearby = []
  hotels = ['hotel1', 'hotel2', 'hotel3']
  


  nearby_api_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?"+nearby_api_params_keys[0]+nearby_api_params_values[0]+nearby_api_params_keys[1]+nearby_api_params_values[1]+nearby_api_params_keys[2]+nearby_api_params_values[2]+nearby_api_params_keys[3]+nearby_api_params_values[3]+google_api_key
  con_1 = requests.get(nearby_api_url)
  nearby_data = con_1.json()
  place_id_list = [place_id_value for hotel_data in nearby_data['results'] for place_id_key,place_id_value in hotel_data.items() if place_id_key == "place_id"]
  place_image_list = [place_image_value for hotel_image_data in nearby_data['results'] for place_image_key,place_image_value in hotel_image_data.items() if place_image_key == "photos"]
  for place_id_inter in place_id_list[0:3]: 
    con_2 = requests.get(places_info_api+place_id_inter+google_api_key)
    hotel_data_1 = con_2.json()
    hotel_nearby.append(hotel_data_1)  

  hotel_nearby_data_context = dict(zip(hotels,hotel_nearby)) 
  show_listing = Music_artist_listing.objects.all().values()
  gallery_listing = Visual_artist_listing.objects.all().values()
  extra_curriucular_listing = Extra_curriucular_listing.objects.all().values()
  contact_form = ContactForm()
  return render(request, 'master-new.html',{'show_listing':show_listing,
             'gallery_listing':gallery_listing,
             'extra_curriucular_listing':extra_curriucular_listing,
             'nearby_accomodations': hotel_nearby_data_context,
             'place_image_list': place_image_list,
             'api_key': pass_api_key,
              'contact_form': contact_form,}
             )

def annex_home_new(request):
  show_listing = Music_artist_listing.objects.all().values()
  template = loader.get_template('annex_home_new.html')
  context = {'show_listing':show_listing}
  return HttpResponse(template.render(context, request))

def gallery_schedule(request):
  show_listing = Visual_artist_listing.objects.all().values()
  template = loader.get_template('annex_home.html')
  context = {'show_listing':show_listing}
  return HttpResponse(template.render(context, request))

# # def contact_us(request):
#   show_listing = Visual_artist_listing.objects.all().values()
#   template = loader.get_template('contact-us.html')
#   context = {'show_listing':show_listing}
#   return HttpResponse(template.render(context, request))