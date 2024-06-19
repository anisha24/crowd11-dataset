"""
Get motion labels from video dataset

Usage:
    python create_motion_labels.py --path /home/anish_a24/IISc/Project/crowd11-dataset/crowd11/Crowd-11 --output motion_flow_labels.csv
"""

import os
import pandas as pd
import argparse

def get_motion_labels(dataset_path):
    """
    Get motion labels from video dataset

    Args:
    - dataset_path: Path to the dataset containing the videos

    Returns:
    - motion_labels_df: DataFrame containing the motion labels
    """
    
    df = pd.DataFrame(columns=['file_name', 'motion_label'])
    for root, dirs, files in os.walk(dataset_path):
        for file in files:
            if file.endswith('.mp4'):
                df = pd.concat([df, pd.DataFrame({'file_name': [file], 'motion_label': [file.split('_')[0]]})], ignore_index=True)
    return df

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Get motion labels from video dataset")
    parser.add_argument("--path", type=str, help='Path of the dataset')
    parser.add_argument("--output", type=str, help='Path to save the motion labels')
    args = parser.parse_args()
    dataset_path = args.path
    output_file_path = args.output

    motion_labels_df = get_motion_labels(dataset_path)
    with open(output_file_path, 'w') as motion_csv:
        motion_labels_df.to_csv(motion_csv, index=False)