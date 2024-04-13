import os
import pytube
import pandas as pd
import numpy as np
import argparse

def download_video(url, final_storage_path, storage_name, multiplier=None):

    try:
        youtube = pytube.YouTube(url)
        stream = youtube.streams.get_highest_resolution()
        video_file = stream.download(output_path=final_storage_path)

        if multiplier:
            multiplier = float(multiplier)
            new_file_name = f"{os.path.splitext(storage_name)[0]}_multiplied.mp4"
            os.rename(video_file, new_file_name)
            os.system(f"ffmpeg -i {new_file_name} -filter:v 'setpts={multiplier}*PTS' {storage_name}")
            os.remove(new_file_name)
        else:
            os.rename(video_file, final_storage_path + "/" + storage_name)
    except Exception as e:
        print(f"Failed to download video: {e}")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Download and save videos from CSV")
    parser.add_argument("csv_file_path", help="CSV file containing url, final_storage_name, and optional ts_multiplier column")
    parser.add_argument("final_storage_path", help="Folder to store the downloaded videos")
    args = parser.parse_args()

    csv_file_path = str(args.csv_file_path)
    final_storage_path = str(args.final_storage_path)
    
    try:
        df = pd.read_csv(csv_file_path, skiprows=1, header=None, names=['source_name', 'url', 'final_storage_name', 'ts_multiplier'])

        for index, row in df.iterrows():
            url = row['url']
            storage_name = row['final_storage_name']
            multiplier = row.get('ts_multiplier')
            if np.isnan(multiplier):
                multiplier = None

            print(f"Downloading video: {url}"
                f" and saving it as: {storage_name}"
                f" with multiplier: {multiplier}")
            
            download_video(url, final_storage_path, storage_name, multiplier)

        print("Videos downloaded and saved successfully!")

    except Exception as e:
        print(f"Failed to download videos: {e}")