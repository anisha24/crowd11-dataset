import argparse
import pandas as pd

def modify_link(link):
    modified_link = link.replace("http://media.gettyimages.com/videos/", "https://gettyimages.in/detail/video/")
    modified_link = modified_link.replace("-id", "/")
    return modified_link

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Change Gettyimages URL to new format")
    parser.add_argument("csv_file_path", help="CSV file containing old gettyimages URL")
    parser.add_argument("final_storage_path", help="CSV file to store new gettyimages URL")
    args = parser.parse_args()

    csv_file_path_parsed = str(args.csv_file_path)
    final_storage_path_parsed = str(args.final_storage_path)

    df = pd.read_csv(csv_file_path_parsed)
    df['url'] = df['url'].apply(modify_link)
    df.to_csv(final_storage_path_parsed, index=False)

    print("Links modified and saved to", final_storage_path_parsed)