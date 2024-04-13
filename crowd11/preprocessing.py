"""
This script reads a CSV file containing clip information and creates clips from the original videos.

The CSV file must have the following columns:
- video_name: name of the video file
- label: label of the video
- start_frame: start frame of the clip
- end_frame: end frame of the clip
- left_distance: distance from the left side of the video
- top_distance: distance from the top side of the video
- width: width of the clip
- height: height of the clip
- dataset: name of the dataset
- scene_number: number of the scene
- crop_number: number of the crop

The script reads the CSV file, creates the clips and saves them to the output folder.

Usage: python preprocessing.py preprocessing.csv --input_folder ./VOI/ --output_folder ./Crowd-11/
"""

from moviepy.editor import VideoFileClip, concatenate_videoclips
import os
import csv
from collections import namedtuple
import argparse

Clip = namedtuple('Clip', 'video_name label start_frame end_frame width height left_distance top_distance dataset scene_number crop_number')
INPUT_FOLDER = ''
OUTPUT_FOLDER = ''
error_clips = []


def read_line(line):
    video_name = line[0]
    label = line[1]
    start_frame = int(line[2])
    end_frame = int(line[3])
    left_distance = float(line[4])
    top_distance = float(line[5])
    width = float(line[6])
    height = float(line[7])
    dataset = line[8]
    scene_number = line[9]
    crop_number = str(int(line[10]))
    clip = Clip(video_name, label, start_frame, end_frame, width, height, left_distance, top_distance, dataset, scene_number, crop_number)
    return clip

def create_clips(clip):
    try:
        input_video_folder = os.path.join(INPUT_FOLDER, clip.dataset)
        input_video_path = os.path.join(input_video_folder, clip.video_name)
        if not os.path.exists(input_video_path):
            return
        output_video_path = os.path.join(OUTPUT_FOLDER, f"{clip.label}_{clip.scene_number}_{clip.crop_number}_{clip.video_name}")
        if os.path.exists(output_video_path):
            return
        original_clip = VideoFileClip(input_video_path)
        start_frame = clip.start_frame
        end_frame = clip.end_frame
        video = original_clip.subclip(start_frame / original_clip.fps, end_frame / original_clip.fps)
        cropped_video = video.crop(x1=clip.left_distance * video.w, 
                                y1=clip.top_distance * video.h, 
                                width=clip.width * video.w, 
                                height=clip.height * video.h)
        if cropped_video.h < 224:
            cropped_video = cropped_video.resize(height=224)
        cropped_video.write_videofile(output_video_path, codec="libx264", audio_codec="aac")
        video.close()
        original_clip.close()
    except Exception as e:
        print(f"Error: {e}")
        error_clips.append(clip)


if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(description='Create clips from a CSV file')
        parser.add_argument('file', type=str, help='CSV file containing clip information')
        parser.add_argument('--input_folder', type=str, help='Folder containing input videos')
        parser.add_argument('--output_folder', type=str, help='Folder to save output videos')
        args = parser.parse_args()
        file = args.file
        INPUT_FOLDER = args.input_folder
        OUTPUT_FOLDER = args.output_folder
        if not os.path.exists(OUTPUT_FOLDER):
            os.makedirs(OUTPUT_FOLDER)
        list_clips = []
        with open(file, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='|')
            for line in reader:
                clip = read_line(line)
                list_clips.append(clip)
        for clip in list_clips:
            create_clips(clip)
        with open('error_clips.txt', 'w') as f:
            for clip in error_clips:
                f.write(f"{clip}")
    except Exception as e:
        print(f"Error: {e}")