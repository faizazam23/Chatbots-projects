import requests
import json
import gzip

# OpenWeatherMap API Key (Replace with your API key)
API_KEY = "2a27039acd74e862bd41c30c75d1a39d"

# Base URL for API
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# Load city list from the downloaded file
CITY_LIST_FILE = "city.list.json.gz"

# Load cities into a dictionary for quick lookup
def load_city_list():
    try:
        with gzip.open(CITY_LIST_FILE, 'rt', encoding='utf-8') as f:
            cities = json.load(f)
        
        # Convert to dictionary {city_name_lower: country_code}
        city_dict = {city['name'].lower(): city['country'] for city in cities}
        return city_dict
    except Exception as e:
        print(f"⚠️ Error loading city list: {e}")
        return {}

# Get weather data
def get_weather(city):
    city_dict = load_city_list()
    
    if city.lower() not in city_dict:
        print(f"❌ Error: City '{city}' not found in the list!")
        return
    
    # API request URL
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses (404, 500, etc.)
        data = response.json()

        # Check if city exists
        if data.get("cod") == 200:
            main = data["main"]
            temperature = main["temp"]
            humidity = main["humidity"]
            weather_desc = data["weather"][0]["description"]

            print("\n🌦️ Weather Report:")
            print(f"🏙️ City: {city}, {city_dict[city.lower()]}")
            print(f"🌡️ Temperature: {temperature}°C")
            print(f"💧 Humidity: {humidity}%")
            print(f"📜 Condition: {weather_desc.capitalize()}")
        else:
            print(f"❌ Error: {data.get('message', 'City not found!')}")

    except requests.exceptions.RequestException as e:
        print(f"🚨 Request error: {e}")

# User input
if __name__ == "__main__":
    city_name = input("Enter city name: ")
    get_weather(city_name)
