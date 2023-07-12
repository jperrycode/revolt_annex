from django.test import TestCase, Client
from django.urls import reverse
from .forms import ContactForm
from unittest.mock import patch

# Create your tests here.
from .models import Music_artist_listing, Visual_artist_listing, Extra_curriucular_listing, Nearby_accomodations, Heads_up_music


class MusicArtistListingTestCase(TestCase):
    def setUp(self):
        self.artist = Music_artist_listing.objects.create(
            artist_name='John Doe',
            artist_genre='Rap',
            show_date='2023-07-01',
            show_time='10:10',
            artist_bio='Lorem ipsum dolor sit amet',
            artist_insta='john.doe',
            artist_website='https://example.com',
            artist_music_page='https://musicpage.com',
            entry_price=20.5
        )

    def test_artist_name(self):
        self.assertEqual(self.artist.artist_name, 'John Doe')


class VisualArtistListingTestCase(TestCase):
    def setUp(self):
        self.visual_artist = Visual_artist_listing.objects.create(
            visual_show_name='Art Show',
            artist_name='Jane Smith',
            artist_medium='Painting',
            show_date_start='2023-07-01',
            show_date_end='2023-07-10',
            artist_bio='Lorem ipsum dolor sit amet',
            artist_website='https://example.com',
            entry_price=10.99,
            age_restriction=False
        )

    def test_visual_show_name(self):
        self.assertEqual(self.visual_artist.visual_show_name, 'Art Show')


class ExtraCurricularListingTestCase(TestCase):
    def setUp(self):
        self.extra_curricular = Extra_curriucular_listing.objects.create(
            class_name='Dance Class',
            class_teacher='John Smith',
            class_description='Lorem ipsum dolor sit amet',
            class_date='2023-07-01',
            class_time='10:00',
            class_location='Revolt Annex',
            class_price=15.99
        )

    def test_class_name(self):
        self.assertEqual(self.extra_curricular.class_name, 'Dance Class')


class NearbyAccommodationsTestCase(TestCase):
    def setUp(self):
        self.accommodation = Nearby_accomodations.objects.create(
            accom_name='Hotel ABC',
            accom_type='Hotel',
            accom_distance=1.5,
            accom_phone='1234567890',
            accom_url='https://example.com/hotel'
        )

    def test_accom_name(self):
        self.assertEqual(self.accommodation.accom_name, 'Hotel ABC')


class HeadsUpMusicTestCase(TestCase):
    def setUp(self):
        self.music_event = Heads_up_music.objects.create(
            event_name='Concert',
            event_date='2023-07-01',
            event_time='19:30',
            artist_name='John Doe',
            event_description='Lorem ipsum dolor sit amet'
        )

    def test_event_name(self):
        self.assertEqual(self.music_event.event_name, 'Concert')



class ContactUsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    @patch('django.core.mail.send_mail')
    def test_contact_us_post(self, mock_send_mail):
        form_data = {
            'name': 'John Doe',
            'email': 'john.doe@example.com',
            'subject': 'Test Subject',
            'message': 'Test message',
        }
        response = self.client.post(reverse('contact_us'), data=form_data)
        self.assertEqual(response.status_code, 302)  # Assuming a successful redirect
        self.assertRedirects(response, reverse('annex_home'))
        mock_send_mail.assert_called_once_with(
            form_data['subject'],
            '\n'.join(form_data.values()),
            'admin@example.com',
            ['admin@example.com']
        )

    def test_contact_us_invalid_header(self):
        form_data = {
            'name': 'John Doe',
            'email': 'john.doe@example.com',
            'subject': 'Test Subject',
            'message': 'Test message',
            # Invalid header field, may result in BadHeaderError
            'subject\nfield': 'Invalid header',
        }
        response = self.client.post(reverse('contact_us'), data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(), 'Invalid header found.')


class AnnexHomeTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_annex_home_get(self):
        response = self.client.get(reverse('annex_home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'master-new.html')


# Additional test cases for other view functions can be added similarly









