"""
This script renames files in a directory. It is used to rename files downloaded from Getty Images.

Usage: python gettyimages_file_renamer.py data/gettyimages
"""

import os
import argparse

def rename_files(directory):
    print(f"Renaming files in directory: {directory}")
    try:
        for filename in os.listdir(directory):
            print(f"Checking file: {filename}")
            if filename.startswith("gettyimages-") and filename.endswith("-640_adpp.mp4"):
                print(f"Renaming {filename}")
                file_id = filename.split("-")[1]
                file_id = file_id.split("_")[0]
                new_filename = f"{file_id}.mp4"
                os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
                print(f"Renamed {filename} to {new_filename}")

    except Exception as e:
        print(f"Failed to rename files: {e}")
        print("issue with URL: ", filename) 

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Rename files in a directory")
    parser.add_argument("directory", help="Directory containing files to rename")
    args = parser.parse_args()
    dataset_directory = args.directory
    rename_files(dataset_directory)