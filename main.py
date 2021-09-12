from bs4 import BeautifulSoup as BS
import requests

while True:
    URL = input('Введите ссылку:')
    if URL == None:
        print('Строка пустая')
        continue
    else:
        URL = URL.strip()
        break

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
           , 'accept': '*/*'}
HOSTS = 'https://auto.ria.com/'


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html, cars):
    soup = BS(html, 'html.parser')
    try:
        response = soup.find('link', rel='next').get('href')
    except:
        response = None
    items = soup.find_all('section', class_='proposition')

    for item in items:
        cars.append({
            'title': item.find('span', class_='link').get_text(),
            'cost': item.find('span', class_='green bold size22').get_text(strip=True)

        })
    for car in cars:
        print(car)
    return response

def parse(pages=2):
    cars = []
    page_url = URL
    for page in range(1, pages + 1):
        print('Page:' + str(page))
        try:
            html = get_html(page_url)
            if html.status_code == 200:
                response = get_content(html.text, cars)
                if response != None:
                    page_url = response
                else:
                    return cars
            else:
                print('Error1')
        except:
            print('Error')

pages = input('Введите количество строк: ')
if pages.isdigit():
    pages = int(pages)
    cars = parse(pages)
    print(f'Получено {len(cars)} автомобилей')
else:
    print('Invalid number')
input('Press Enter...')