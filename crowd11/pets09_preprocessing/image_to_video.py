import cv2
import os
import argparse

def images_to_video(image_folder, output_video_path, fps):
    try:
        # listing images from directory
        images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]

        print(images)

        # sorting images in directory before processing
        images.sort(key=lambda x: int(x.split('.')[0]))

        print("-------------------------------------------------------")

        print(images)

        # reading first image to get height and width
        frame = cv2.imread(os.path.join(image_folder, images[0]))
        height, width, _ = frame.shape
        print(f"Height: {height}, Width: {width}")


        # defining video codec and creating video writer object
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        video_writer = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

        # writing images to video
        for image in images:
            video_writer.write(cv2.imread(os.path.join(image_folder, image)))

        # releasing video writer object and closing all windows
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

    print("Image folder: ", image_folder)
    print("Output video path: ", output_video_path)
    print("Frames per second: ", fps)

    images_to_video(image_folder, output_video_path, fps)
