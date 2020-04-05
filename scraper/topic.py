import requests
import random
from time import sleep

from bs4 import BeautifulSoup
from IPython import embed


BASE_URL = 'http://sample-target-bucket-with-html-pages.s3-website-ap-southeast-1.amazonaws.com'

PAGES = [
    '1.html',
    '2.html',
    '3.html',
    '4.html',
    '5.html',
]


def delay(seconds):
    print(f'Sleeping for {seconds} second(s)')
    sleep(seconds)


def get_random_number():
    return random.randint(1, 5)


def main():
    for page in PAGES:
        target_url = BASE_URL + '/' + page
        print(f'Scraping {target_url}')


        print('Done')
        delay(get_random_number())


if __name__ == '__main__':
    main()
