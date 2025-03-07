import requests


def get_london_weather(url_template):
    url = url_template.format('/Лондон')
    response = requests.get(url)
    return response.text


def get_sheremetyevo_weather(url_template):
    url = url_template.format('/Шереметьево')
    response = requests.get(url)
    return response.text


def get_cherepovets_weather(url_template):
    url = url_template.format('/Череповец?mnqTM&lang=ru')
    response = requests.get(url)
    return response.text


def main():
    url_template = 'https://wttr.in{}'
    london_weather = get_london_weather(url_template)
    sheremetyevo_weather = get_sheremetyevo_weather(url_template)
    cherepovets_weather = get_cherepovets_weather(url_template)
    print(
        london_weather,
        sheremetyevo_weather,
        cherepovets_weather
        )


if __name__ == '__main__':
    main()
