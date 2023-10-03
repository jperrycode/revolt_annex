from django.urls import path
from . import views
from .views import *
from django.views.generic import RedirectView
from django.contrib import admin
from django.views.generic import TemplateView


urlpatterns = [
    path('', RedirectView.as_view(url='revolt-art/')),
    path('revolt-art/', TemplateView.as_view(template_name = 'schedule/master-new.html'), name='annex_home'),
    # path('revolt-test/', AnnexTestView.as_view(), name='annex_test'),
    path('contact_us/', ContactUsView.as_view(), name='contact_us'),
    # path('art-archive/', ArchiveView.as_view(), name='archive-home'),
#    path('contact_us_success', views.ContactSuccessView, name='contact_success'),
]

admin.site.site_header = 'Revolt Gallery - Reset Performing Arts'
admin.site.site_title = 'Revolt and Reset '