"""
This script is used to label videos in a folder. 
The script will display each video in the folder and ask the user to input a label for the video. 
The labels are saved in a csv file called video_labels.csv. The csv file has two columns: Video and Label. 
The Video column contains the name of the video and the Label column contains the label for the video. 
The script uses OpenCV to display the videos and get the user input for the labels.

Usage:
    python dataset_new_labelling.py Crowd-11/

Args:
    videos_folder: Folder containing videos to label

Returns:
    None
"""

import cv2
import pandas as pd
import os
import argparse
from natsort import natsorted

def update_csv(video_name, label):
    df = pd.DataFrame({"Video": [video_name], "Label": [label]})
    with open("video_labels.csv", "a") as f:
        df.to_csv(f, header=f.tell()==0, index=False)

def label_videos(videos_folder):
    for root, dirs, files in os.walk(videos_folder):
        for file in natsorted(files):
            print("File: ", file)
            video_path = os.path.join(root, file)
            cap = cv2.VideoCapture(video_path)
            label = ""
            replay = False
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break
                cv2.imshow('Video', frame)
                cv2.waitKey(50)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                if cv2.waitKey(1) & 0xFF == ord('r'):
                    replay = True
                    break
            if replay:
                cap.release()
                cv2.destroyAllWindows()
                continue
            label = input("Enter label for {}: ".format(file))
            print(f"Saving label: {label} for video: {video_path}")
            update_csv(file, label)
            cap.release()
            cv2.destroyAllWindows()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Label videos')
    parser.add_argument('videos_folder', type=str, help='Folder containing videos to label')
    args = parser.parse_args()
    videos_folder = args.videos_folder
    label_videos(videos_folder)