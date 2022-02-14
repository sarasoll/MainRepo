import requests
api = "https://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q="
city = input('Where are you?!!...  ')
url = f"{api}{city}"
send = requests.get(url).json()
print(send['weather'][0]['main'])


