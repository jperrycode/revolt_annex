from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Music_artist_listing, Visual_artist_listing, Extra_curriucular_listing, Nearby_accomodations
import requests
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from revolt_annex.settings import DEFAULT_FROM_EMAIL as from_email
import environ

env = environ.Env(interpolate=True)

# send email functionality 
def contact_us(request):
  if request.method == 'POST':
    print('method-post')
    contact_form = ContactForm(request.POST)
    if contact_form.is_valid():
      subject = contact_form.cleaned_data['subject'] 
      user_email=contact_form.cleaned_data['email']
      body = {            
			'name': contact_form.cleaned_data['name'],   
			'message': contact_form.cleaned_data['message'], 
			}
      
      message = "\n".join(body.values())
      print(message)
      try:
        send_mail(subject, message, from_email, [user_email]) 
        print('email sent')
      except BadHeaderError:
        return HttpResponse('Invalid header found.')
      # return redirect ('annex_home')
    contact_form = ContactForm()
  print(contact_form.errors)
  return redirect('annex_home')
    







def annex_home(request):
  google_api_key = env.str('PROXY_GOOGLE')
  
  nearby_api_params_keys = ("rankby=","&location=","&radius=","&type=")
  nearby_api_params_values = ("prominence","36.4107818%2C-105.5711364","1500","bar")
  places_info_api = 'https://maps.googleapis.com/maps/api/place/details/json?place_id='
  bar_nearby = []
  bars = ['bar1', 'bar2', 'bar3']
  


  nearby_api_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?"+nearby_api_params_keys[0]+nearby_api_params_values[0]+nearby_api_params_keys[1]+nearby_api_params_values[1]+nearby_api_params_keys[2]+nearby_api_params_values[2]+nearby_api_params_keys[3]+nearby_api_params_values[3]+'&key='+google_api_key
  con_1 = requests.get(nearby_api_url)
  
  nearby_data = con_1.json()

  place_id_list = [place_id_value for bar_data_int in nearby_data['results'] for place_id_key,place_id_value in bar_data_int.items() if place_id_key == "place_id"]
  
  place_image_list = [place_image_value for hotel_image_data in nearby_data['results'] for place_image_key,place_image_value in hotel_image_data.items() if place_image_key == "photos"]
  
  for place_id_inter in place_id_list[0:3]: 
    con_2 = requests.get(places_info_api+place_id_inter+google_api_key)
    
    bar_data_int_1 = con_2.json()
    bar_nearby.append(bar_data_int_1)  

  bar_nearby_data_context = dict(zip(bars,bar_nearby)) 
  show_listing = Music_artist_listing.objects.all().order_by('show_date').values()
  gallery_listing = Visual_artist_listing.objects.all().values()
  extra_curriucular_listing = Extra_curriucular_listing.objects.all().values()
  contact_form = ContactForm()
  return render(request, 'annex_master_backup.html',{'show_listing':show_listing,
             'gallery_listing':gallery_listing,
             'extra_curriucular_listing':extra_curriucular_listing,
             'bars_nearby': bar_nearby_data_context,
             'place_image_list': place_image_list,
              'contact_form': contact_form,
              'api_key': env.str('PROXY_GOOGLE'),}
             )

# def annex_home_new(request):
#   show_listing = Music_artist_listing.objects.all().values()
#   template = loader.get_template('annex_home_new.html')
#   context = {'show_listing':show_listing}
#   return HttpResponse(template.render(context, request))

# def gallery_schedule(request):
#   show_listing = Visual_artist_listing.objects.all().values()
#   template = loader.get_template('annex_home.html')
#   context = {'show_listing':show_listing}
#   return HttpResponse(template.render(context, request))

# # def contact_us(request):
#   show_listing = Visual_artist_listing.objects.all().values()
#   template = loader.get_template('contact-us.html')
#   context = {'show_listing':show_listing}
#   return HttpResponse(template.render(context, request))

# def annex_music_schedule(request):
#   show_listing = Music_artist_listing.objects.all().values()
#   template = loader.get_template('annex_music_schedule.html')
#   context = {'show_listing':show_listing}
#   return HttpResponse(template.render(context, request))