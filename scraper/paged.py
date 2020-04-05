import requests
import random
from time import sleep

from bs4 import BeautifulSoup
from IPython import embed


BASE_URL = 'http://sample-target-bucket-with-html-pages.s3-website-ap-southeast-1.amazonaws.com'


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


def extract_page_link(html_string):
    soup = BeautifulSoup(html_string, 'html.parser')
    anchor_elements = soup.find_all('a')
    links = []

    for a in anchor_elements:
        links.append(a.attrs['href'])
    else:
        return links


def main():
    main_url = BASE_URL + '/group2/index.html'
    main_html = extract_html_content(main_url)
    pages = extract_page_link(main_html)

    target_values = []
    for page in pages:
        target_url = BASE_URL + page
        print(f'Scraping {target_url}')

        html_string = extract_html_content(target_url)
        target_value = extract_target_value_from_page(html_string)
        target_values.append(target_value)

        print('Done')
        delay(get_random_number())
    else:
        print(', '.join(target_values))


if __name__ == '__main__':
    main()
