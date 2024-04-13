#!/bin/bash

# Download web data from various sources

# separate urls for different sources from the web_urls.csv
python crowd11/url_extractor_different_source_webcsv.py crowd11/web_urls.csv crowd11/data/pond5/pond5.csv pond5
python crowd11/url_extractor_different_source_webcsv.py crowd11/web_urls.csv crowd11/data/pond5/gettyimages.csv gettyimages
python crowd11/url_extractor_different_source_webcsv.py crowd11/web_urls.csv crowd11/data/pond5/youtube.csv youtube

# download data from the urls for pond5
python crowd11/download_data.py crowd11/data/pond5/pond5.csv crowd11/data/pond5/pond5
python crowd11/pond5_preprocessing/pond5_video_downloader.py crowd11/pond5_preprocessing/pond5.csv crowd11/data/pond5/

# download data from the urls for youtube
python crowd11/download_data.py crowd11/data/pond5/youtube.csv crowd11/data/pond5/youtube
