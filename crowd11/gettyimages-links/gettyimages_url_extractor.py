import argparse
import pandas as pd

parser = argparse.ArgumentParser(description="Download and save videos from CSV")
parser.add_argument("csv_file_path", help="CSV file containing source_name, url, final_storage_name, and optional ts_multiplier column")
parser.add_argument("final_storage_path", help="Filename to store the final CSV file with only gettyimages rows")
args = parser.parse_args()

csv_file_path_parsed = str(args.csv_file_path)
final_storage_path_parsed = str(args.final_storage_path)

df = pd.read_csv(csv_file_path_parsed, sep=',', skiprows=1, header=None, names=['source_name', 'url', 'final_storage_name', 'ts_multiplier'])
urls = df.iloc[:, 1]
# names = df.iloc[:, 2]
with open(final_storage_path_parsed, 'w') as f:
    for i in range(len(urls)):
        # f.write(f'"{urls[i]}____{names[i]}",\n')
        f.write(f'"{urls[i]}",\n')

print(f'URLs extracted from the CSV file and saved to {final_storage_path_parsed}')
