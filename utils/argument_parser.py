"""
parse arguments which are passed to script
"""

from argparse import ArgumentParser
from input import url, urls_list_file
from utils.all import get_now_time_string, create_directory_in_download_dir


class ScriptParser:
    def __init__(self):
        self.parser = ArgumentParser(usage='python3 %(prog)s --help',
                                     allow_abbrev=False, add_help=False)

    def start_parsing(self):
        self.parser.add_argument('--help', '-h', action='store_true')
        self.parser.add_argument('--urls', nargs='*')
        self.parser.add_argument('--urls-file')
        self.parser.add_argument('--timeout', default=3.0)
        self.parser.add_argument('--block-sleep', default=60.0)
        self.parser.add_argument('--sleep', default=1.0)

    def print_help(self):
        help_text = f''' Usage:  python3 {self.parser.prog} [Input] [Arguments]

    Input Arguments:
      --urls              url addresses to download JS files from URL or URLs
      --urls-file         name of the file which URLs are in it
    
    Config Arguments:
      --timeout           timeout for GET requests [default 3.0 SECs: 3.0]
      --sleep             sleep between each request before sending [default 1.0 SECs: 1.0]
      --block-sleep       sleep after the request that got blocked [default 60.0 SECs: 60.0] 

    Help:  
      --help              print help message

    Examples:
      --urls https://example.com/1.js https://example.com/2.js --timeout 2.0
      --urls-file urls.txt --timeout 1.5 --sleep 5.0
'''
        print(help_text)

    def get_parser(self):
        """
        return parser object
        :return:
        """
        return self.parser

    def check_arguments(self):
        args, unknown = self.parser.parse_known_args()
        try:
            args.timeout = float(args.timeout)
        except Exception as e:
            print('Error in converting timeout to float')
            print('Example: --timeout 3.0')
            exit()

        try:
            args.sleep = float(args.sleep)
        except Exception as e:
            print('Error in converting sleep param to float')
            print('Example: --sleep 5.0')
            exit()

        try:
            args.block_sleep = float(args.block_sleep)
        except Exception as e:
            print('Error in converting --block-sleep param to float')
            print('Example: --block-sleep 1.0')
            exit()

        if (args.help is not None) and (args.help is True):
            self.print_help()
            exit()

        if (args.urls is not None) or (args.urls_file is not None):

            now_time = get_now_time_string()
            create_directory_in_download_dir(dir_name=now_time)
            final_dir_path = f"downloads/{now_time}"

            if args.urls is not None:
                url.UrlInput(
                    urls_list=args.urls,
                    timeout=args.timeout,
                    download_dir_path=final_dir_path,
                    req_sleep=args.sleep,
                    block_sleep= args.block_sleep,
                ).get_urls_content()
            if args.urls_file is not None:
                urls_list_file.UrlsListFileInput(
                    urls_file_name=args.urls_file,
                    timeout=args.timeout,
                    download_dir_path=final_dir_path,
                    req_sleep=args.sleep,
                    block_sleep=args.block_sleep,
                ).get_urls_in_file()

        else:
            print('You have to set source!')
            print('--urls or --urls-file')
            self.parser.print_usage()
