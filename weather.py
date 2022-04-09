import requests

API_KEY = "a6fa0aa8edd005c7ffa67ad2b5a647d6"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


city = input("Enter a city name: ")

request_url = f"{BASE_URL}?q={city}&appid={API_KEY}"

response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temp = round(data['main']['temp'] - 273.15, 2)

    print("Weather: " + weather)
    print(f"Temperature: {temp} degrees celsius")

else:
    print("Error")


