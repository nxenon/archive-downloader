"""
check requirements of running
"""
import os


def start_checking():
    check_download_dir()

def check_download_dir():
    download_dir_path = "downloads/"
    if not os.path.exists(download_dir_path):
        os.makedirs(download_dir_path)
