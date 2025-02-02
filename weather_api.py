import requests

WEATHER_API_KEY = "" #place your api key over here from open weather 

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return f"🌤️ {data['weather'][0]['description'].capitalize()}, 🌡️ Temp: {data['main']['temp']}°C"
    else:
        return "⚠️ Error: Could not retrieve weather data."
