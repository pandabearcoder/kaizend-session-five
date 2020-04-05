import requests
import random
from contextlib import contextmanager
from time import sleep

from bs4 import BeautifulSoup
from IPython import embed


BASE_URL = 'http://sample-target-bucket-with-html-pages.s3-website-ap-southeast-1.amazonaws.com'

PAGES = [
    'group1/1.html',
    'group1/2.html',
    'group1/3.html',
    'group1/4.html',
    'group1/5.html',
]


class ScrapingJob:

    def __init__(self, url):
        self.url = url
        self.html = None
        self.scraped_item = None

    def request(self):
        print(f'Scraping {self.url}')
        self.html = extract_html_content(self.url)
        print(self.html)
        return self

    def extract(self):
        target_value = extract_target_value_from_page(self.html)
        print(target_value)
        print('Done')
        return target_value


def delay(seconds):
    print(f'Sleeping for {seconds} second(s)')
    sleep(seconds)


def get_random_number():
    return random.randint(1, 5)


def extract_html_content(target_url):
    response = requests.get(target_url)
    return response.text


def extract_target_value_from_page(html_string):
    soup = BeautifulSoup(html_string, 'html.parser')
    target = soup.find(id='target')
    target_text = target.get_text()
    return target_text


@contextmanager
def scraper(label):
    job = ScrapingJob(label)
    yield job


def main():
    target_values = []

    for page in PAGES:
        target_url = BASE_URL + '/' + page

        with scraper(target_url) as job:
            value = job.request().extract()
            target_values.append(value)

        delay(get_random_number())
    else:
        print(f'[SCRAPED {len(target_values)} ITEMS] ' + ', '.join(target_values))


if __name__ == '__main__':
    main()
