import urllib.request
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
import ssl
from typing import NamedTuple

class CharPoint(NamedTuple):
    x: int
    y: int
    char: str

def parse_table(html: str, has_header: bool = True) -> list[CharPoint]:
    result: list[CharPoint] = []
    try:
        soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
        table = soup.find('table')
        if table is None:
            raise ValueError('No <table> tag found in HTML.')
        
        rows = table.find_all('tr')
        if has_header:
            rows = rows[1:]
        
        for row in rows:
            cells = row.find_all(['td'])
            x_coord = cells[0].get_text()
            char_text = cells[1].get_text(strip=True)
            y_coord = cells[2].get_text()

            x, y = int(x_coord.strip()), int(y_coord.strip())
            #print(x, y , char_text)
            result.append(CharPoint(x=x, y=y, char=char_text))
    except Exception as e:
        print(e)

    return result

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

try:

    #url = 'https://docs.google.com/document/d/e/2PACX-1vTMOmshQe8YvaRXi6gEPKKlsC6UpFJSMAk4mQjLm_u1gmHdVVTaeh7nBNFBRlui0sTZ-snGwZM4DBCT/pub'
    url = 'https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub'
    html = urllib.request.urlopen(url).read()
    print()
    cells = parse_table(html)
    print(type(cells))

    charpoints = sorted(cells, key=lambda p:(-p.y, p.x))
    
    prev_y = None
    for cell in charpoints:
        if prev_y is not None and cell.y != prev_y:
            print('\n')
        print(cell.char, end='')
        prev_y = cell.y
    print()

except HTTPError as e:
    print(f"HTTP Error occurred! Status code: {e.code}")

except URLError as e:
    print(f"URL Error occurred! {e}")

except Exception as e:
    print(f"An unexpected error occurred! {e}")
