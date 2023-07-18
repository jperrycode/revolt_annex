from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.annex_home, name='home_redirect'),
    path('revolt-art/', views.annex_home, name='annex_home'),
    path('contact_us/', views.contact_us, name='contact_us'),
   
]
