import pandas as pd
import os
import shutil
import argparse

error_rows = []

def copy_videos(csv_file, source_folder_base, destination_folder):
    df = pd.read_csv(csv_file, delimiter=';', header=None, names=['source_name', 'video_name'])
    for index, row in df.iterrows():
        try:
            source_name = row['source_name']
            video_name = row['video_name']
            source_folder = os.path.join(source_folder_base, source_name)
            source_video_path = os.path.join(source_folder, video_name)
            if os.path.exists(source_video_path):
                destination_video_path = os.path.join(destination_folder, source_name, video_name)
                shutil.copyfile(source_video_path, destination_video_path)
                print(f"Copied '{video_name}' from '{source_name}' to '{destination_folder}'")
            else:
                print(f"Video '{video_name}' not found in '{source_name}'")
        except Exception as e:
            print(f"Error: {e}")
            error_rows.append(row)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Copy videos from existing dataset to a new folder')
    parser.add_argument('csv_file', type=str, help='CSV file containing existing dataset urls')
    parser.add_argument('source_folder_base', type=str, help='Base folder containing existing dataset')
    parser.add_argument('destination_folder', type=str, help='Folder to copy videos to')

    args = parser.parse_args()
    csv_file = args.csv_file
    source_folder_base = args.source_folder_base
    destination_folder = args.destination_folder

    copy_videos(csv_file, source_folder_base, destination_folder)
    with open('error_rows.csv', 'w') as f:
        for row in error_rows:
            f.write(f"{row}\n")