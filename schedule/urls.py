from django.urls import path
from . import views
from .views import *
from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [
    path('', views.annex_home, name='home_redirect'),
    path('revolt-art/', views.annex_home, name='annex_home'),
    path('contact_us/', views.contact_us, name='contact_us'),
   
]

