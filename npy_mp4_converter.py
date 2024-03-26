import cv2
import numpy as np
import os
import subprocess

def npy_to_video(npy_path, output_video_path, fps=30):
    # Load NPY file with allow_pickle=True
    frames = np.load(npy_path, allow_pickle=True)

    # Check if frames is a dictionary, and extract values if necessary
    if isinstance(frames, dict):
        frames = list(frames.values())

    # Check if frames is a list, and convert to numpy array if necessary
    if isinstance(frames, list):
        frames = np.array(frames)

    # Get video dimensions from the first frame
    height, width, _ = frames[0].shape

    # Define video codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

    # Write frames to the video
    for frame in frames:
        out.write(frame)

    # Release VideoWriter
    out.release()



def convert_npy_to_mp4(npy_folder, output_folder, fps=30):

    npy_path = "/Users/anaralik/Documents/IISc/Project/Phase 2/Datasets/crowd11-dataset/pets2009-test-view-001.npy"

    # Define output video path
    video_name = npy_folder + ".mp4"
    output_video_path = os.path.join(output_folder, video_name)

    # Convert NPY to MP4
    npy_to_video(npy_path, output_video_path, fps)

if __name__ == "__main__":
    npy_folder = "pets2009-test-view-001.npy"
    output_folder = "./output/"
    convert_npy_to_mp4(npy_folder, output_folder)
