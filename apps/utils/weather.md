city_weather = {
            'city'              : city.upper(),
            'icon'              : r['weather'][0]['icon'],
            'temperature'       : r['main']['temp'],
            'description'       : r['weather'][0]['description'],
        }



2332453
{
    "coord": {"lon": 7.5401, "lat": 44.9331}, 
    "weather": [{"id": 803, "main": "Clouds", "description": "broken clouds", "icon": "04d"}], 
    "base": "stations",
    "main": {"temp": 12.61, "feels_like": 10.71, "temp_min": 11.14, "temp_max": 13.33, "pressure": 1031, "humidity": 30}, "visibility": 10000, 
    "wind": {"speed": 0.45, "deg": 0, "gust": 0.89}, 
    "clouds": {"all": 67}, 
    "dt": 1647795816, 
    "sys": {"type": 2, "id": 2008171, "country": "IT", "sunrise": 1647754405, "sunset": 1647798078}, 
    "timezone": 3600, 
    "id": 3172215, 
    "name": "None",
    "cod": 200
    }