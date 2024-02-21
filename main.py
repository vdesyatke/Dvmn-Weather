import requests
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Description: this program prints out Weather in London, Cherepovets, Sheremetyevo'
    )
    parser.parse_args()

    places = ['Лондон', 'Шереметьево', 'Череповец']
    payload = {'nTqmM': '', 'lang': 'ru'}
    for place in places:
        url = f'https://www.wttr.in/{place}'
        response = requests.get(url, params=payload)
        response.raise_for_status()
        print(response.text)

