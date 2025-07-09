import json
import requests
from datetime import datetime
import os

def extract():
    print("🚀 Starting extract script...")

    with open('config/api_config.json') as f:
        api_key = json.load(f)['api_key']
    print(f"🔑 Using API Key: {api_key[:4]}****")

    with open('config/cities.json') as f:
        cities = json.load(f)['cities']
    print(f"🌍 Fetching weather for cities: {cities}")

    base_url = "http://api.openweathermap.org/data/2.5/weather"
    os.makedirs("data", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = f"data/weather_raw_{timestamp}.json"

    all_data = []

    for city in cities:
        params = {
            'q': city,
            'appid': api_key,
            'units': 'metric'
        }

        try:
            response = requests.get(base_url, params=params)
            if response.status_code == 200:
                data = response.json()
                all_data.append(data)
                print(f"✅ Fetched data for {city}")
            else:
                print(f"⚠️ Failed to fetch data for {city}: {response.status_code}")
        except Exception as e:
            print(f"❌ Error fetching data for {city}: {e}")

    with open(output_path, 'w') as f:
        json.dump(all_data, f, indent=4)

    print(f"\n📁 Weather data saved to: {output_path}")
    print(json.dumps(all_data, indent=2))  # Optional: show output in console

if __name__ == "__main__":
    extract()
