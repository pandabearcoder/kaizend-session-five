from bs4 import BeautifulSoup


def generate_html():
    return """
        <html>
          <head></head>
          <body>
            <a href="/a.html">A</a>
            <a href="/b.html">B</a>
            <a href="/c.html">C</a>
            <a href="/d.html">D</a>
          </body>
        </html>
    """


def main():
    html_doc = generate_html()
    soup = BeautifulSoup(html_doc, 'html.parser')

    anchor_elements = soup.find_all('a')
    for anchor in anchor_elements:
        print(anchor.attrs['href'])


if __name__ == '__main__':
    main()
