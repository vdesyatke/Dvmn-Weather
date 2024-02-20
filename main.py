import requests
import time


if __name__ == '__main__':
    places = ['Лондон', 'Шереметьево', 'Череповец']
    for place in places:
        url = f'https://www.wttr.in/{place}?nTqmM&lang=ru'
        response = requests.get(url)
        print(response.text)
