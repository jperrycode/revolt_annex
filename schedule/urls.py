from django.urls import path
from . import views
from .views import *

urlpatterns = [
    # path('revolt-gallery/schedule/', views.gallery_schedule, name='gallery_schedule'),
    # path('revolt-annex/schedule/', views.annex_music_schedule, name='annex_schedule'),
    path('revolt-art/', views.annex_home, name='annex_home'),
    # path('revolt-art-new/', views.annex_home_new, name='annex_home'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('contact_redirect/', views.contact_redirect, name='contact_redirect'),
   
]
