# weather_bot.py
import requests

API_KEY = "your_openweathermap_api_key"  # Replace with your actual API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

def get_weather(city):
    url = BASE_URL + "q=" + city + "&appid=" + API_KEY + "&units=metric"
    response = requests.get(url)
    data = response.json()
    
    if data["cod"] == 200:
        main = data["main"]
        temperature = main["temp"]
        humidity = main["humidity"]
        weather_desc = data["weather"][0]["description"]
        
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {weather_desc}")
    else:
        print("City not found!")

def main():
    print("Welcome to the Weather Bot!")
    city = input("Enter the name of the city: ")
    get_weather(city)

if __name__ == "__main__":
    main()
