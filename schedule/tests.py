
from .models import Music_artist_listing, Visual_artist_listing, Extra_curriucular_listing, Nearby_accomodations, Heads_up_music
from datetime import date, time
from django.test import TestCase, Client
from django.urls import reverse

from .forms import ContactForm

class ContactFormTest(TestCase):
    def test_valid_form(self):
        data = {
            'name': 'John Doe',
            'email': 'johndoe@example.com',
            'subject': 'Test Subject',
            'message': 'This is a test message.',
            'email_consent': True,
        }
        form = ContactForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {
            'name': '',
            'email': 'invalid-email',
            'subject': '',
            'message': '',
            'email_consent': False,
        }
        form = ContactForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 4)  # Four fields have errors

    def test_blank_email_consent(self):
        data = {
            'name': 'Alice Johnson',
            'email': 'alice@example.com',
            'subject': 'Another Test Subject',
            'message': 'Another test message.',
            'email_consent': '',
        }
        form = ContactForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1) 

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



class ExtraCurricularListingModelTest(TestCase):
    def setUp(self):
        self.listing = Extra_curriucular_listing.objects.create(
            class_name='Sample Class',
            class_teacher='John Doe',
            class_description='Sample description',
            class_date=date(2023, 8, 15),
            class_time=time(10, 30),
            class_location='Test Location',
            class_price=19.99,
            image_url='http://example.com/sample.jpg'
        )

    def test_listing_creation(self):
        self.assertEqual(self.listing.class_name, 'Sample Class')
        self.assertEqual(self.listing.class_teacher, 'John Doe')
        self.assertEqual(self.listing.class_description, 'Sample description')
        self.assertEqual(self.listing.class_date, date(2023, 8, 15))
        self.assertEqual(self.listing.class_time, time(10, 30))
        self.assertEqual(self.listing.class_location, 'Test Location')
        self.assertEqual(self.listing.class_price, 19.99)
        self.assertEqual(self.listing.image_url, 'http://example.com/sample.jpg')

class HeadsUpMusicModelTest(TestCase):
    def setUp(self):
        self.event = Heads_up_music.objects.create(
            event_name='Sample Event',
            event_date=date(2023, 8, 20),
            event_time=time(19, 0),
            artist_name='Jane Smith',
            event_description='Sample event description',
        )

    def test_event_creation(self):
        self.assertEqual(self.event.event_name, 'Sample Event')
        self.assertEqual(self.event.event_date, date(2023, 8, 20))
        self.assertEqual(self.event.event_time, time(19, 0))
        self.assertEqual(self.event.artist_name, 'Jane Smith')
        self.assertEqual(self.event.event_description, 'Sample event description')

    def test_event_ordering(self):
        event_2 = Heads_up_music.objects.create(
            event_name='Second Event',
            event_date=date(2023, 8, 18),
            event_time=time(15, 30),
            artist_name='Alice Johnson',
            event_description='Another event description',
        )

        events = Heads_up_music.objects.all()
        self.assertEqual(events[0], self.event)
        self.assertEqual(events[1], event_2)

# Additional tests can be added to cover more scenarios like updating, deleting, etc.




# views



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