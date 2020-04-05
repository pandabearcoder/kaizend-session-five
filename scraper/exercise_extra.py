import requests
import random
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


def debugger(func):

    def wrapper(*args, **kwargs):
        print(f'[START: {func.__name__}]')
        output = func(*args, **kwargs)
        print(f'[END: {func.__name__}]')
        return output

    return wrapper


@debugger
def delay(seconds):
    print(f'Sleeping for {seconds} second(s)')
    sleep(seconds)


def get_random_number():
    return random.randint(1, 5)


@debugger
def extract_html_content(target_url):
    print(f'Downloading HTML contents of {target_url}')
    response = requests.get(target_url)
    output = response.text
    print(output)
    return output


@debugger
def extract_target_value_from_page(html_string):
    soup = BeautifulSoup(html_string, 'html.parser')
    target = soup.find(id='target')
    target_text = target.get_text()
    print(target_text)
    return target_text


def main():
    target_values = []
    for page in PAGES:
        target_url = BASE_URL + '/' + page
        html = extract_html_content(target_url)

        target_value = extract_target_value_from_page(html)
        target_values.append(target_value)

        delay(get_random_number())
    else:
        print(f'[SCRAPED {len(target_values)} ITEMS] ' + ', '.join(target_values))


if __name__ == '__main__':
    main()
