"""
Code to download videos from Gettyimages using UI automation (selinium)

This script reads a file containing Gettyimages URLs and downloads the videos using UI automation.

Usage: python gettyimages_url_selinium_downloader_from_ui.py urls_gettyimages.txt
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import argparse

failed_links = []

def automate_ui(link):
    print("Curent Link: ", link)

    try:

        download_directory = "/home/anish_a24/IISc/Project/crowd11-dataset/crowd11/gettyimages-links/downloads"

        chrome_options = Options()
        chrome_options.add_argument(f"--no-sandbox")
        chrome_options.add_argument(f"--disable-dev-shm-usage")
        chrome_options.add_argument(f"--disable-gpu")
        chrome_options.add_argument(f"--window-size=1920x1080")
        chrome_options.add_argument(f"--disable-infobars")
        chrome_options.add_argument(f"--disable-notifications")
        chrome_options.add_experimental_option("prefs", {
            "download.default_directory": download_directory,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        })
        driver = webdriver.Chrome()
        driver.get(link)

        download_button = driver.find_element(By.CLASS_NAME, "f05EVVQW8iYfSZTUwEJ_")
        download_button.click()
        popup = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "ciLUNHwEcSyOueUD0sEm"))
        )
        download_button_popup = popup.find_element(By.CLASS_NAME, "vb4pQUw6N8T8vh72xdbx")
        download_button_popup.click()

        time.sleep(10)
        driver.quit()
    
    except Exception as e:
        print(f"Failed to download video: {e}")
        failed_links.append(link)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Download and save videos from Gettyimages using UI")
    parser.add_argument("url_file_path", help="File containing Gettyimages URLs")
    args = parser.parse_args()

    url_file_path = str(args.url_file_path)

    try:
        with open(url_file_path, "r") as file:
            links = file.readlines()
        print("Read all links from file")
        print("Total links: ", len(links))

        print("Starting to download videos")
        for link in links:
            automate_ui(link)

        print("All videos downloaded successfully!")
        print("Saving failed links to a file...")

        with open('output.txt', 'w') as file:
            for link in failed_links:
                file.write(link+"\n")

        print("Failed links saved to output.txt")

    except Exception as e:
        print("Error: ", e)


