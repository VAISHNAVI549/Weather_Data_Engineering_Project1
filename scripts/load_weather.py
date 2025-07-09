import psycopg2
import json
import os
from datetime import datetime

# DB connection parameters
user = "vaishnaviyvs"
password = ""  # leave empty if passwordless
host = "localhost"
port = "5432"
database = "weather_db"

# Locate latest cleaned JSON
data_dir = "data"
json_files = [f for f in os.listdir(data_dir) if f.startswith("weather_cleaned_") and f.endswith(".json")]
if not json_files:
    raise FileNotFoundError("❌ No cleaned JSON file found.")

latest_file = sorted(json_files)[-1]
file_path = os.path.join(data_dir, latest_file)

# Read JSON data
with open(file_path, 'r') as f:
    weather_data = json.load(f)

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname=database,
    user=user,
    password=password,
    host=host,
    port=port
)
cur = conn.cursor()

# Insert data
for row in weather_data:
    cur.execute("""
        INSERT INTO weather_data (
            city, datetime, temperature_C, humidity_percent,
            weather, description, wind_speed, pressure
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        row.get("city"),
        row.get("datetime"),
        row.get("temperature_C"),
        row.get("humidity_%"),
        row.get("weather"),
        row.get("description"),
        row.get("wind_speed_m/s"),
        row.get("pressure_hPa")
    ))

conn.commit()
cur.close()
conn.close()
print(f"✅ Successfully loaded data from {latest_file} into PostgreSQL.")
