import requests

def test_api_key(api_key):
    """Test if the OpenWeatherMap API key is valid"""
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    
    params = {
        "appid": api_key,
        "q": "London,uk",
        "units": "metric"
    }
    
    print(f"Testing API key: {api_key}")
    print(f"Request URL: {base_url}")
    print(f"Parameters: {params}")
    print("-" * 50)
    
    try:
        response = requests.get(base_url, params=params, timeout=10)
        
        print(f"Status Code: {response.status_code}")
        print(f"Response Headers: {dict(response.headers)}")
        
        if response.status_code == 200:
            data = response.json()
            print("✓ SUCCESS! API key is valid")
            print(f"Location: {data['name']}, {data['sys']['country']}")
            print(f"Temperature: {data['main']['temp']}°C")
            print(f"Weather: {data['weather'][0]['description']}")
            return True
        else:
            print("✗ FAILED!")
            print(f"Error response: {response.text}")
            return False
            
    except requests.RequestException as e:
        print(f"✗ REQUEST ERROR: {e}")
        return False

# Test your API key
api_key = "5436904ce02320afdf94b21692e2b99e"
test_api_key(api_key)
