import requests


def search_city(city):
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=f4149d0d859828b86a82f7fdb6c0fc14"
    response = requests.get(url.format(city)).json()
    data = {
            'city'              : city.upper(),
            'icon'              : response['weather'][0]['icon'],
            'temperature'       : int(response['main']['temp']),
            'description'       : response['weather'][0]['description'],
        }
    return data