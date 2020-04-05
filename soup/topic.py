from bs4 import BeautifulSoup


def generate_html():
    return """
        <html>
          <head></head>
          <body>
            <div id="target">Hello World</div>
            <div>A</div>
            <div>B</div>
            <div>C</div>
            <div>D</div>
          </body>
        </html>
    """


def main():
    html_doc = generate_html()
    soup = BeautifulSoup(html_doc, 'html.parser')

    target = soup.find(id='target')
    target_text = target.get_text()
    print(f'Target: {target_text}')

    div_elements = soup.find_all('div')
    print('Div Texts')
    for div in div_elements:
        print(f'{div.get_text()}')


if __name__ == '__main__':
    main()
