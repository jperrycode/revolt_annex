from django.test import TestCase
from django.urls import reverse
from .models import Music_artist_listing, Visual_artist_listing, Extra_curriucular_listing
from django.http import HttpResponse
from django.shortcuts import render
from .views import ContactUsView, AnnexHomeView, ArchiveView, AnnexTestView
from .forms import ContactForm
from unittest import mock

class ContactUsViewTestCase(TestCase):
    def test_contact_us_post_valid_form(self):
        response = self.client.post(reverse('contact_us'), {
            'name': 'John Doe',
            'email': 'john@example.com',
            'subject': 'Test Subject',
            'message': 'Test Message',
            'email_consent': True,
        })
        self.assertEqual(response.status_code, 302)  # Redirect response
        self.assertRedirects(response, reverse('annex_home'))

    def test_contact_us_post_invalid_form(self):
        response = self.client.post(reverse('contact_us'), {})
        self.assertEqual(response.status_code, 302)  # Redirect response
        self.assertRedirects(response, reverse('annex_home'))

class AnnexHomeViewTestCase(TestCase):
    def test_annex_home_view(self):
        response = self.client.get(reverse('annex_home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'schedule/annex_master_backup.html')
        # Test context variables
        self.assertIn('show_listing', response.context)
        self.assertIn('gallery_listing', response.context)
        self.assertIn('extra_curricular_listing', response.context)
        # ... add more checks for other context variables ...

class ArchiveViewTestCase(TestCase):
    def test_archive_view(self):
        response = self.client.get(reverse('archive_view'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'schedule/contact-us.html')
        # Test context variables
        self.assertIn('extra_curricular_listing', response.context)

class AnnexTestViewTestCase(TestCase):
    def test_annex_test_view(self):
        response = self.client.get(reverse('annex_test_view'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'schedule/dev_template.html')
        # Test context variables
        self.assertIn('show_listing', response.context)
        self.assertIn('gallery_listing', response.context)
        self.assertIn('extra_curricular_listing', response.context)
        # ... add more checks for other context variables ...
