import os
import requests

# Load API key from environment variable
api_key = os.getenv("WEATHER_API_KEY")
base_url = "https://api.weatherapi.com/v1/current.json"

def get_weather(location):
    params = {"key": api_key, "q": location, "aqi": "no"}
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        try:
            data = response.json()
            print(f"Weather in {data['location']['name']}")
            print(f"Temperature (C): {data['current']['temp_c']}")
            print(f"Condition: {data['current']['condition']['text']}")
        except KeyError as e:
            print(f"Unexpected response format: {e}")
    else:
        print(f"Failed to get data: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    city = input("Enter a city: ")
    get_weather(city)
