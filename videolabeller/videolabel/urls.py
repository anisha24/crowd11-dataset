from django.urls import path
from . import views

urlpatterns = [
    path('', views.video_list, name='video_list'),
    path('play/<str:video_name>/', views.play_video, name='play_video'),
    path('save_videos/', views.save_video_list, name='save_videos'),
    path('download-csv/', views.download_csv, name='download_csv'),
    path('upload-csv/', views.upload_csv, name='upload_csv'),
    # path('add-unique-labels/', views.add_unique_labels, name='add_unique_labels')
]