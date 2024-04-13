import os
import argparse

def remove_frame_name(directory_path):
    try:
        for file in os.listdir(directory_path):
            if file.endswith('.jpg'):
                print("Renaming file: ", file)
                os.rename(os.path.join(directory_path, file), os.path.join(directory_path, file.split('_')[1]))
    except Exception as e:
        print("Exception ->>> : ", e)

if __name__ == '__main__':

    try:
        parser = argparse.ArgumentParser(description='Remove frame name from video')
        parser.add_argument('directory_path', help='Path to files')
        args = parser.parse_args()
        directory_path = args.directory_path

        print("Got path from user: ", directory_path)

        remove_frame_name(directory_path)

    except Exception as e:
        print("Error: ", e)