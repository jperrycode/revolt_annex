from django.urls import path

from .views import *
from django.views.generic import RedirectView, TemplateView
from django.contrib import admin

urlpatterns = [
    path('', RedirectView.as_view(url='revolt-art/')),
    path('revolt-art/', AnnexHomeView.as_view(), name='annex_home'),
    # path('revolt-test/', AnnexTestView.as_view(), name='annex_test'),
    path('contact_us/', ContactUsView.as_view(), name='contact-us'),
    path('contact-us-success/', ContactSuccessView.as_view(), name='contact-success'),
    path('contact-revolt/', Contact_form_view.as_view(), name='contact-revolt'),
    path('hut-out-front/', HutView.as_view(), name='hut'),
    path('reset-performing-arts/', ResetView.as_view(), name='music-reset'),
    path('revolt-gallery/', RevoltView.as_view(), name='gallery-revolt'),
    path('revolt-gallery/archive/<str:pk>/details/', ArchivePageView.as_view(), name='archive_details'),
    # path('api-test/', GoogleAPIView.as_view(), name='api-test'),
]

admin.site.site_header = 'Revolt Gallery - Reset Performing Arts'
admin.site.site_title = 'Revolt and Reset'
