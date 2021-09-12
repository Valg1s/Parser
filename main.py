from bs4 import BeautifulSoup as BS
import requests
import os
import csv

# while True:
#     URL = input('Введите ссылку:')
#     if URL == None:
#         print('Строка пустая')
#         continue
#     else:
#         URL = URL.strip()
#         break

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
           , 'accept': '*/*'}
HOSTS = 'https://auto.ria.com/'
FILE = 'Cars.csv'


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
            'cost_dollar': item.find('span', class_='green bold size22').get_text(strip=True),
            'cost_UAH': item.find('span', class_='size16').get_text(),
            'region': item.find('span', class_='item region').get_text()
        })
    # print(cars)
    return response

def write_file(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Название', 'Цена в долларах', 'Цена в гривнах', 'Город'])
        for item in items:
            writer.writerow([item['title'], item['cost_dollar'], item['cost_UAH'], item['region']])


def parse(pages=2, URL='https://auto.ria.com/uk/newauto/marka-mitsubishi/'):
    cars = []
    page_url = URL
    for page in range(1, pages + 1):
        try:
            html = get_html(page_url)
            print(f'Парсинг страницы {page}')
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
            return cars
    return cars


def for_cmd():
    pages = input('Введите колличество страниц: ')
    if pages.isdigit():
        pages = int(pages)
        cars = parse(pages)
        print(f'Получено {len(cars)} автомобилей')
        write_file(cars, FILE)
        os.startfile(FILE)
    else:
        print('Invalid number')
    input('Press Enter...')


def for_GUI(pages='5', URL='https://auto.ria.com/uk/newauto/marka-mitsubishi/'):
    if pages.isdigit():
        site_pages = int(pages)
        cars = parse(site_pages, URL)
        response_message = f'Получено {len(cars)} автомобилей.'
        if response_message != 'Получено 0 автомобилей.':
            write_file(cars, FILE)
            os.startfile(FILE)
        else:
            response_message = 'Ошибка ввода.'
    else:
        response_message = 'Ошибка ввода.'
    return response_message