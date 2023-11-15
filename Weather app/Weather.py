import requests
response = requests.get("https://www.weatherapi.com/my/fields.aspx")
print(response.status_code)