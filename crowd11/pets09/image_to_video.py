import cv2
import os
import argparse

def images_to_video(image_folder, output_video_path, fps):
    try:
        images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
        frame = cv2.imread(os.path.join(image_folder, images[0]))
        height, width, _ = frame.shape
        print(f"Height: {height}, Width: {width}")

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        video_writer = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

        for image in images:
            video_writer.write(cv2.imread(os.path.join(image_folder, image)))

        cv2.destroyAllWindows()
        video_writer.release()
    except Exception as e:
        print(f"Failed to convert images to video: {e}")

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Convert images to videos")
    parser.add_argument("image_folder", help="Path to the folder containing images")
    parser.add_argument("output_video_path", help="Path to the output video")
    parser.add_argument("fps", help="Frames per second", type=int)
    args = parser.parse_args()
    image_folder = str(args.image_folder)
    output_video_path = str(args.output_video_path)
    fps = int(args.fps)

    images_to_video(image_folder, output_video_path, fps)
