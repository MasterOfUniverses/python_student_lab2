import requests

def check_direction(deg):
        if (deg>=0 and deg<=22) or (deg> 337 and deg<=360):
            return "С"
        elif (deg>22 and deg<=67):
            return "СВ"
        elif (deg>67 and deg<=112):
            return "В"
        elif (deg>112 and deg<=157):
            return "ЮВ"
        elif (deg>157 and deg<=202):
            return "Ю"
        elif (deg>202 and deg<=247):
            return "ЮЗ"
        elif (deg>247 and deg<=292):
            return "З"
        elif (deg>292 and deg<=337):
            return "СЗ"
        else:
            return "Error"

    

city = "Moscow,RU"
appid = "a16fec156d951b4d2450f31bfa54d7d8"

res = requests.get("http://api.openweathermap.org/data/2.5/weather",
             params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()

print("Город:", city)
print("Погодные условия:", data['weather'][0]['description'])
print("Температура:", data['main']['temp'])
print("Минимальная температура:", data['main']['temp_min'])
print("Максимальная температура", data['main']['temp_max'])
deg = data['wind']['deg']
direction=""
direction=check_direction(deg)
print(f"Ветер: {data['wind']['speed']} м/с, {direction}")
print(f"Видимость: {data['visibility']}")
print("\n ____________________________ \n")

res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                   params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("Прогноз погоды на неделю:")
for i in data['list']:
    print("Дата <", i['dt_txt'], "> \r\nТемпература <", '{0:+3.0f}'.format(i['main']['temp']), "> \r\nПогодные условия <", i['weather'][0]['description'], ">")
    deg = i['wind']['deg']
    direction=""
    direction=check_direction(deg)
    print(f"Ветер: {i['wind']['speed']} м/с, {direction}")
    print(f"Видимость: {i['visibility']}")
    print("\n ____________________________ \n")
