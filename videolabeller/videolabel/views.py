import os
import csv
import pandas as pd
from natsort import natsorted
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from videolabel.models import Video, VideoLabel
from videolabel.forms import CSVUploadForm
from videolabeller.settings import MEDIA_ROOT

def video_list(request):
    videos = Video.objects.all()
    context = {
        'videos': videos
    }
    return render(request, 'videolabel/video_list.html', context)

def update_csv(video_name, video_label):
    csv_file = 'video_labels.csv'
    if os.path.exists(csv_file):
        df = pd.read_csv(csv_file)
        if video_name in df['Video'].values:
            df.loc[df['Video'] == video_name, 'Label'] = video_label
        else:
            new_row = pd.DataFrame({"Video": [video_name], "Label": [video_label]})
            df = pd.concat([df, new_row], ignore_index=True)
    else:
        df = pd.DataFrame({"Video": [video_name], "Label": [video_label]})
    df.to_csv(csv_file, index=False)

def play_video(request, video_name):
    video_url = f'/media/{video_name}'
    success_message = None
    if request.method == 'POST':
        video_label = request.POST.get('video_label')
        video = Video.objects.get(video_name=video_name)
        video.label = video_label
        video.save()
        update_csv(video_name, video_label)
        label, _ = VideoLabel.objects.get_or_create(label=video_label)
        label.save()
        success_message = "Label saved successfully."
    current_video = get_object_or_404(Video, video_name=video_name)
    prev_video = Video.objects.filter(id__lt=current_video.id).order_by('-id').first()
    next_video = Video.objects.filter(id__gt=current_video.id).order_by('id').first()
    # video_labels = Video.objects.exclude(label__isnull=True).exclude(label='').values_list('label', flat=True).distinct()
    video_labels = VideoLabel.objects.all()
    context = {
        'video_url': video_url,
        'video_name': video_name,
        'success_message': success_message,
        'current_video': current_video,
        'current_label': current_video.label,
        'prev_video': prev_video,
        'next_video': next_video,
        'video_labels': video_labels
    }
    return render(request, 'videolabel/play_video.html', context)

def save_video_list(request):
    videos_folder = MEDIA_ROOT
    for root, dirs, files in os.walk(videos_folder):
        for file in natsorted(files):
            video_name = file
            if not Video.objects.filter(original_name=video_name).exists():
                video = Video(original_name=video_name)
                video.save()
    return HttpResponse("Video list saved successfully.")

def download_csv(request):
    videos = Video.objects.exclude(label__isnull=True).exclude(label='').values_list('video_name', 'label')
    df = pd.DataFrame(list(videos), columns=['Video', 'Label'])
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="video_labels.csv"'
    df.to_csv(path_or_buf=response, index=False)
    return response

def upload_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            csv_reader = csv.DictReader(decoded_file)
            for row in csv_reader:
                video_name = row['Video']
                label = row['Label']
                Video.objects.update_or_create(video_name=video_name, defaults={'label': label})
            messages.success(request, 'CSV file uploaded successfully.')
            return redirect('video_list')
    else:
        form = CSVUploadForm()
    return render(request, 'videolabel/upload_csv.html', {'form': form})

def add_unique_labels(request):
    unique_labels = Video.objects.exclude(label__isnull=True).exclude(label='').values_list('label', flat=True).distinct()
    for label in unique_labels:
        VideoLabel.objects.get_or_create(label=label)
    return render(request, 'add_unique_labels.html', {'message': 'Unique labels added successfully!'})