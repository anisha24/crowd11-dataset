import argparse
import pandas as pd

"""
This script filters a CSV file based on a column value and saves the filtered rows to a new CSV file.
Usage: python filter_csv.py csv_file_path final_storage_path filtering_column
Example: python filter_csv.py data.csv filtered_data.csv <gettyimages/youtube/pond5>
"""

parser = argparse.ArgumentParser(description="Download and save videos from CSV")
parser.add_argument("csv_file_path", help="CSV file containing source_name, url, final_storage_name, and optional ts_multiplier column")
parser.add_argument("final_storage_path", help="Filename to store the final CSV file with only gettyimages rows")
parser.add_argument("filtering_column", help="Column to filter on")
args = parser.parse_args()

csv_file_path_parsed = str(args.csv_file_path)
final_storage_path_parsed = str(args.final_storage_path)
filtering_column = str(args.filtering_column)

df = pd.read_csv(csv_file_path_parsed, sep=';', skiprows=1, header=None, names=['source_name', 'url', 'final_storage_name', 'ts_multiplier'])
filtered_df = df[df[df.columns[0]] == filtering_column]
new_csv_path = final_storage_path_parsed
filtered_df.to_csv(new_csv_path, index=False)