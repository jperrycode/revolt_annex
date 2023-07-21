from django.test import TestCase
from .models import Music_artist_listing, Visual_artist_listing, Extra_curriucular_listing, Nearby_accomodations, Heads_up_music

class MusicArtistListingTest(TestCase):
    def setUp(self):
        self.artist = Music_artist_listing.objects.create(
            artist_name='John Doe',
            artist_genre='Rap',
            show_date='2023-07-25',
            show_time='18:00:00',
            artist_bio='Talented rapper',
            entry_price=15.99,
            image_url='https://example.com/image.jpg'
        )

    def test_artist_name(self):
        self.assertEqual(self.artist.artist_name, 'John Doe')

    def test_artist_genre(self):
        self.assertEqual(self.artist.artist_genre, 'Rap')

    def test_show_date(self):
        self.assertEqual(str(self.artist.show_date), '2023-07-25')

    def test_show_time(self):
        self.assertEqual(str(self.artist.show_time), '18:00:00')

    def test_artist_bio(self):
        self.assertEqual(self.artist.artist_bio, 'Talented rapper')

    def test_entry_price(self):
        self.assertEqual(self.artist.entry_price, 15.99)

    def test_image_url(self):
        self.assertEqual(self.artist.image_url, 'https://example.com/image.jpg')


class VisualArtistListingTest(TestCase):
    def setUp(self):
        self.artist = Visual_artist_listing.objects.create(
            visual_show_name='Art Show',
            artist_name='Jane Smith',
            artist_medium='Oil painting',
            show_date_start='2023-07-20',
            show_date_end='2023-07-30',
            artist_bio='Talented visual artist',
            entry_price=10.50,
            age_restriction=False,
            image_url='https://example.com/art_image.jpg'
        )

    def test_visual_show_name(self):
        self.assertEqual(self.artist.visual_show_name, 'Art Show')

    def test_artist_name(self):
        self.assertEqual(self.artist.artist_name, 'Jane Smith')





# views

from django.test import TestCase, Client
from django.urls import reverse
from .models import Music_artist_listing, Visual_artist_listing, Extra_curriucular_listing, Nearby_accomodations
from .forms import ContactForm

class ContactUsViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('contact_us')

    def test_contact_us_view_post(self):
        response = self.client.post(self.url, {
            'name': 'John Doe',
            'email': 'john@example.com',
            'subject': 'Hello',
            'message': 'This is a test message.',
        })
        self.assertEqual(response.status_code, 302)  # Expecting a redirect

        # Check if the email was sent successfully
        self.assertContains(response, 'email sent')

    def test_contact_us_view_invalid_header(self):
        response = self.client.post(self.url, {
            'name': 'John Doe',
            'email': 'john@example.com',
            'subject': 'Subject with\nnewline',
            'message': 'This is a test message.',
        })
        self.assertEqual(response.status_code, 200)  # Expecting a response with status code 200
        self.assertContains(response, 'Invalid header found.')

class AnnexHomeViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('annex_home')

        # Create some test data for Music_artist_listing and Visual_artist_listing models
        Music_artist_listing.objects.create(
            artist_name='John Doe',
            artist_genre='Rap',
            show_date='2023-07-25',
            show_time='18:00:00',
            artist_bio='Talented rapper',
            entry_price=15.99,
            image_url='https://example.com/image.jpg'
        )

        Visual_artist_listing.objects.create(
            visual_show_name='Art Show',
            artist_name='Jane Smith',
            artist_medium='Oil painting',
            show_date_start='2023-07-20',
            show_date_end='2023-07-30',
            artist_bio='Talented visual artist',
            entry_price=10.50,
            age_restriction=False,
            image_url='https://example.com/art_image.jpg'
        )

    def test_annex_home_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)  # Expecting a response with status code 200

        # Check if the context data contains the required objects
        self.assertTrue('show_listing' in response.context)
        self.assertTrue('gallery_listing' in response.context)
        self.assertTrue('extra_curriucular_listing' in response.context)
        self.assertTrue('bars_nearby' in response.context)
        self.assertTrue('place_image_list' in response.context)
        self.assertTrue('contact_form' in response.context)
        self.assertTrue('api_key' in response.context)

        # Check if the rendered page contains certain content based on the data we created in the setUp method
        self.assertContains(response, 'John Doe')
        self.assertContains(response, 'Art Show')