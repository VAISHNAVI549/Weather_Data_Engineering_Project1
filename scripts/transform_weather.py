import os
import json
import pandas as pd
from datetime import datetime


def transform():
    print("🔄 Starting transformation script...")

    # Get the latest raw file from the data directory
    data_dir = "data"
    raw_files = [f for f in os.listdir(data_dir) if f.startswith("weather_raw_") and f.endswith(".json")]
    if not raw_files:
        print("❌ No raw weather data files found.")
        return

    latest_file = sorted(raw_files)[-1]
    print(f"📂 Using file: {latest_file}")

    with open(os.path.join(data_dir, latest_file), 'r') as f:
        raw_data = json.load(f)

    # Extract structured data
    transformed_data = []
    for entry in raw_data:
        record = {
            "city": entry.get("name"),
            "datetime": datetime.utcfromtimestamp(entry.get("dt")).strftime('%Y-%m-%d %H:%M:%S'),
            "temperature_C": entry["main"].get("temp"),
            "humidity_%": entry["main"].get("humidity"),
            "weather_main": entry["weather"][0].get("main") if entry.get("weather") else None,
            "description": entry["weather"][0].get("description") if entry.get("weather") else None,
            "wind_speed_m/s": entry["wind"].get("speed"),
            "pressure_hPa": entry["main"].get("pressure")
        }
        transformed_data.append(record)

    # Save to JSON
    output_file = os.path.join(data_dir, f"weather_cleaned_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
    with open(output_file, 'w') as f:
        json.dump(transformed_data, f, indent=4)

  #  print(f"✅ Transformation complete. File saved to: {output_file}")

    print(f"✅ Transformation complete. File saved to: {output_file}")
#    print(df.head())


if __name__ == "__main__":
    transform()
