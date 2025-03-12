import requests


def get_weather(url_template, city):
    url = url_template.format(f'/{city}')
    payload = {
        'm': '',
        'n': '',
        'q': '',
        'T': '',
        'M': '',
        'lang': 'ru'
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    return response.text


def main():
    url_template = 'https://wttr.in{}'
    cities = ['Лондон', 'Шереметьево', 'Череповец']
    for city in cities:
        print(get_weather(url_template, city))


if __name__ == '__main__':
    main()
