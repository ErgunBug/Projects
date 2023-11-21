import requests

api_key =  '30d4741c779ba94c470ca1f63045390a'


user_input = input("Stadt eingeben: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

if weather_data.json() ["cod"] == "404":
    print("Stadt nicht gefunden!")
else:
    weather  = weather_data.json() ["weather"] [0] ["main"]
    temp = round(weather_data.json()["main"] ["temp"])
    print(f"Das Wetter in {user_input} ist: {weather}")
    print(f"Die Temperatur in {user_input} ist: {temp}")
