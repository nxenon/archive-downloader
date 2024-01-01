"""
all utils
"""
from datetime import datetime
from urllib.parse import urlparse
import os
import requests

BASE_ARCHIVE_ORG_URL = 'https://web.archive.org/web/0js_/'

def get_now_time_string():
    current_time = datetime.now()

    # Format the current time as 'year-month-day-hour-minute'
    formatted_time = current_time.strftime('%Y-%m-%d-%H-%M')
    return formatted_time


def create_directory_in_download_dir(dir_name):
    new_path = f"downloads/{dir_name}"
    if not os.path.exists(new_path):
        os.mkdir(new_path)

    print(f'Created a directory with name {new_path} to save files in it.')


def get_last_part_of_the_url_path(url):
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    return filename


def send_get_request(url, timeout):
    req = requests.get(url, timeout=timeout, verify=False)
    return req
