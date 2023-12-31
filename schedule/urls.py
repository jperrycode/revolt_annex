from django.urls import path
from . import views
from .views import *
from django.views.generic import RedirectView, TemplateView
from django.contrib import admin



urlpatterns = [
    path('', RedirectView.as_view(url='revolt-art/')),
    path('revolt-art/', TemplateView.as_view(template_name = 'schedule/master-new.html'), name='annex_home'),
    # path('revolt-test/', AnnexTestView.as_view(), name='annex_test'),
    path('contact_us/', ContactUsView.as_view(), name='contact-us'),
    path('contact-us-success/', ContactSuccessView.as_view(), name='contact-success'),
    path('contact-revolt/', Contact_form_view.as_view(), name='contact-revolt'),
    path('community-classes/', ClassesView.as_view(), name='class-reset'),
    path('reset-performing-arts/', ResetView.as_view(), name='music-reset'),
    path('revolt-gallery/', RevoltView.as_view(), name='gallery-revolt'),
    # path('api-test/', GoogleAPIView.as_view(), name='api-test'),
]

admin.site.site_header = 'Revolt Gallery - Reset Performing Arts'
admin.site.site_title = 'Revolt and Reset'