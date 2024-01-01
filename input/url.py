"""
this script gets input from urls which are specified in arguments
"""
import requests
from utils.all import get_last_part_of_the_url_path, BASE_ARCHIVE_ORG_URL, send_get_request
from time import sleep

from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Suppress only the InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class UrlInput:
    def __init__(self, urls_list, timeout, req_sleep, block_sleep, download_dir_path):
        self.urls_list = urls_list  # get list of urls e.g --> ["URL1", "URL2", ...]
        self.timeout = timeout
        self.req_sleep = req_sleep
        self.block_sleep = block_sleep
        self.download_dir_path = download_dir_path

    def get_urls_content(self):
        """
        get content of URLs
        """

        for url in self.urls_list:
            sleep(self.req_sleep)
            new_url = BASE_ARCHIVE_ORG_URL + url
            last_part_name = get_last_part_of_the_url_path(url)
            try:
                req = send_get_request(url=new_url, timeout=self.timeout)
            except requests.ConnectionError as e:
                _num = 0
                print('Error occurred on GET request of ' + new_url + ', error (probably rate limit): ' + str(e))
                print('try 5 more times!')
                while _num <= 5:
                    print(f'Sleeping {self.block_sleep} seconds...')
                    sleep(self.block_sleep)
                    try:
                        req = send_get_request(url=new_url, timeout=self.timeout)
                    except Exception as e:
                        _num += 1
                        continue
                    break

            try:
                with open(f'{self.download_dir_path}/{last_part_name}', 'w', encoding='utf-8') as new_file:
                    new_file.write(str(req.content.decode()))
            except Exception as e:
                print(f'Error occurred on creating file {self.download_dir_path}/{last_part_name}. error : {str(e)}')
                continue

            print(f'Created file: {self.download_dir_path}/{last_part_name} from url: {url}')
