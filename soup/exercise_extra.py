import re

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

            <script>
              var hello = 'yoh';
              alert(hello);
            </script>
          </body>
        </html>
    """


def main():
    html_doc = generate_html()
    soup = BeautifulSoup(html_doc, 'html.parser')

    script_tags = soup.find_all('script')

    target_script = script_tags[0].string.strip()
    script_lines = target_script.split('\n')

    variable_value = extract_script_variable_value(script_lines[0], 'hello')
    print(variable_value)


def extract_script_variable_value(script_line, variable_name):
    matches = re.match(f"var {variable_name}(\s?)=(\s?)'(?P<value>\D+)';", script_line)

    if not matches:
        return

    results = matches.groupdict()
    return results.get('value')


if __name__ == '__main__':
    main()
