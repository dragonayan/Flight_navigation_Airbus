

import os
import requests
import json
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()


# Example function to fetch data from an API (OpenWeatherMap API is used here)
def fetch_weather_data(api_url):
    response = requests.get(api_url)
    return response.json()

# Save sample data
def save_sample_data(data, filename='./data/sample_data.json'):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w') as f:
        json.dump(data, f)

if __name__ == '__main__':
    load_dotenv()
    api_key = os.getenv('API_KEY')
    
    # Replace with your actual API key and URL
    api_url = f'https://api.openweathermap.org/data/2.5/weather?q=London&appid={api_key}'

    sample_data = fetch_weather_data(api_url)
    save_sample_data(sample_data)
