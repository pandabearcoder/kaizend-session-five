import requests
import random
from time import sleep

from bs4 import BeautifulSoup
from IPython import embed


BASE_URL = 'http://sample-target-bucket-with-html-pages.s3-website-ap-southeast-1.amazonaws.com'
TARGET_URL = BASE_URL + '/group3/target.html'


def delay(seconds):
    print(f'Sleeping for {seconds} second(s)')
    sleep(seconds)


def get_random_number():
    return random.randint(1, 5)


def extract_html_content(target_url):
    response = requests.get(target_url)
    return response.text


def main():
    html_string = extract_html_content(TARGET_URL)
    soup = BeautifulSoup(html_string, 'html.parser')
    div_elements = soup.find_all('div', {'class': 'content_section_text'})
    target_div = div_elements[1]

    list_items = target_div.find('ul').find_all('li')
    for item in list_items:
        item_text = item.get_text().replace('\n', '')
        text_list = [text for text in item_text.split(' ') if text]
        clean_text = ' '.join(text_list)
        print(clean_text, '\n')


if __name__ == '__main__':
    main()
