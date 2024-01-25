# tasks.py

from celery import shared_task
from django.core.mail import send_mail
from revolt_annex import settings
from schedule.models import *

from .models import Visual_artist_listing, Archivedshowimagedata
from django.utils import timezone

# from schedule.models import VimeoVideo  # Replace 'yourapp' with your app's name
from background_task import background


@shared_task(bind=True)
def send_notification_mail(subject, email, message):
    send_mail(
        subject=subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email],
        fail_silently=False,
    )
    return "Done"


# @shared_task
# def fetch_and_save_vimeo_videos():
#     vimeo_token = str(os.getenv('VIMEO_ACCESS_TOKEN'))  # Replace with your Vimeo access token
#
#     try:
#         # Initialize the Vimeo client with the provided access token
#         client = vimeo.VimeoClient(
#             token=vimeo_token,
#         )
#
#         # Use the client to make API requests
#         videos_data = client.get('/me/videos')
#         videos_context = videos_data.json()
#
#         # Save the video data to the database
#         for video in videos_context.get('data', []):
#             video_id = video.get('uri').split('/')[-1]
#             title = video.get('name')
#             description = video.get('description')
#
#             vimeo_video, created = VimeoVideo.objects.get_or_create(
#                 video_id=video_id,
#                 defaults={
#                     'title': title,
#                     'description': description,
#                     # Add other fields as needed
#                 }
#             )
#
#             if not created:
#                 vimeo_video.title = title
#                 vimeo_video.description = description
#                 # Update other fields if needed
#                 vimeo_video.save()
#
#         print('Successfully fetched and saved Vimeo videos.')
#     except Exception as e:
#         print(f'Failed to fetch Vimeo videos. Error: {str(e)}')
#


# @background(schedule=24 * 60 * 60)  # Schedule the task to run every 24 hours
# def scan_and_move_rows():
#     current_datetime = timezone.now()
#
#     # Get rows to move where end date has passed the current date and hour
#     rows_to_move = Visual_artist_listing.objects.filter(
#         vis_show_date_end__lt=current_datetime,
#     )
#
#     for row in rows_to_move:
#         # Move the row to Archivedshowimagedata
#         Archivedshowimagedata.objects.create(
#             archive_show_name=row.visual_show_name,
#             archive_artist_name=row.vis_artist_name,
#             archive_start_date=row.vis_show_date_start,
#             archive_end_date=row.vis_show_date_end,
#             # Add other fields as needed
#         )
#
#         # Delete the row from Visual_artist_listing
#         row.delete()
