from django.test import TestCase, RequestFactory
from django.urls import reverse
from schedule.views import RevoltView, ResetView

class RevoltViewTestCase(TestCase):
    def test_revolt_view(self):
        request = RequestFactory().get('/revolt-gallery/')  # Replace with your actual URL
        response = RevoltView.as_view()(request)
        self.assertEqual(response.status_code, 200)  # Check if the response is successful
        # Add more assertions to check for specific context data, if needed

class ResetViewTestCase(TestCase):
    def test_reset_view(self):
        request = RequestFactory().get('/reset-performing-arts/')  # Replace with your actual URL
        response = ResetView.as_view()(request)
        self.assertEqual(response.status_code, 200)  # Check if the response is successful
        # Add more assertions to check for specific context data, if needed



from .models import Archivedshowimagedata, Archiveimagefiles

class ArchivedshowimagedataModelTest(TestCase):
    def setUp(self):
        self.archive_data = Archivedshowimagedata.objects.create(
            archive_show_name='Show Name',
            archive_artist_name='Artist Name',
            archive_start_date='2023-12-31',
            archive_end_date='2024-01-01',
            archive_folder_id='folder123',
            archive_artist_web='https://example.com'
            # Add other fields as needed
        )

    def test_archive_show_name(self):
        archive_data = Archivedshowimagedata.objects.get(archive_show_name='Show Name')
        self.assertEqual(archive_data.archive_show_name, 'Show Name')

    # Add more test cases for other fields as needed

class ArchiveimagefilesModelTest(TestCase):
    def setUp(self):
        self.archive_data = Archivedshowimagedata.objects.create(
            archive_show_name='Show Name',
            archive_artist_name='Artist Name',
            archive_start_date='2023-12-31',
            archive_end_date='2024-01-01',
            archive_folder_id='folder123',
            archive_artist_web='https://example.com'
        )
        self.archive_image = Archiveimagefiles.objects.create(
            archive_image_id='image123',
            archive_image_name='Image Name',
            archive_fk=self.archive_data
            # Add other fields as needed
        )

    def test_archive_image_id(self):
        archive_image = Archiveimagefiles.objects.get(archive_image_id='image123')
        self.assertEqual(archive_image.archive_image_id, 'image123')

    # Add more test cases for other fields as needed




from django.test import TestCase, Client
from django.urls import reverse
from .models import Archivedshowimagedata, Archiveimagefiles

class ModelsAndViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.archive_data = Archivedshowimagedata.objects.create(
            archive_show_name='Show Name',
            archive_artist_name='Artist Name',
            archive_start_date='2023-12-31',
            archive_end_date='2024-01-01',
            archive_folder_id='folder123',
            archive_artist_web='https://example.com'
            # Add other fields as needed
        )
        self.archive_image = Archiveimagefiles.objects.create(
            archive_image_id='image123',
            archive_image_name='Image Name',
            archive_fk=self.archive_data
            # Add other fields as needed
        )

    def test_view_and_model_interaction(self):
        response = self.client.get(reverse('gallery-revolt'))
        self.assertEqual(response.status_code, 200)
        
        # Check if the context contains the expected data
        self.assertIn('archive_show_data', response.context)
        
        # Assuming the context data is passed to the template
        archive_show_data = response.context.get('archive_show_data')
        self.assertIsNotNone(archive_show_data)
        
        # Check if the model instance data matches the expected values
        self.assertEqual(archive_show_data.archive_show_name, 'Show Name')
        self.assertEqual(archive_show_data.archive_artist_name, 'Artist Name')
        self.assertEqual(archive_show_data.archive_folder_id, 'folder123')
        
        # Error handling for missing keys in the context or invalid attribute values
        try:
            missing_archive_show_data = response.context['missing_archive_show_data']
        except KeyError:
            missing_archive_show_data = None
        
        self.assertIsNone(missing_archive_show_data)
        
        # Check if the retrieved context data matches the model instance
        if archive_show_data:
            self.assertIsInstance(archive_show_data, Archivedshowimagedata)
            self.assertEqual(archive_show_data.archive_show_name, 'Show Name')
            self.assertEqual(archive_show_data.archive_artist_name, 'Artist Name')
            self.assertEqual(archive_show_data.archive_folder_id, 'folder123')
