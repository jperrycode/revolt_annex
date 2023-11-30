#tasks.py

from celery import shared_task
from django.core.mail import send_mail
from revolt_annex import settings
import os
import json
import vimeo
from django.core.management import call_command
from schedule.models import VimeoVideo  # Replace 'yourapp' with your app's name


# @shared_task(bind=True)
# def send_notification_mail(self, subject, email, message):
#     send_mail(
#         subject=subject,
#         message=message,
#         from_email=settings.EMAIL_HOST_USER,
#         recipient_list=[email],
#         fail_silently=False,
#         )
#     return "Done"


# @shared_task
# def fetch_and_save_vimeo_videos():
#     vimeo_token = str(os.getenv('VIMEO_ACCESS_TOKEN'))  # Replace with your Vimeo access token

#     try:
#         # Initialize the Vimeo client with the provided access token
#         client = vimeo.VimeoClient(
#             token=vimeo_token,
#         )

#         # Use the client to make API requests
#         videos_data = client.get('/me/videos')
#         videos_context = videos_data.json()

#         # Save the video data to the database
#         for video in videos_context.get('data', []):
#             video_id = video.get('uri').split('/')[-1]
#             title = video.get('name')
#             description = video.get('description')

#             vimeo_video, created = VimeoVideo.objects.get_or_create(
#                 video_id=video_id,
#                 defaults={
#                     'title': title,
#                     'description': description,
#                     # Add other fields as needed
#                 }
#             )

#             if not created:
#                 vimeo_video.title = title
#                 vimeo_video.description = description
#                 # Update other fields if needed
#                 vimeo_video.save()

#         print('Successfully fetched and saved Vimeo videos.')
#     except Exception as e:
#         print(f'Failed to fetch Vimeo videos. Error: {str(e)}')