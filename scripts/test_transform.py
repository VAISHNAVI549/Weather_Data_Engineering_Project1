import os
import pandas as pd

def test_transform_output():
    # List all files in the data directory
    data_dir = "data"
    if not os.path.exists(data_dir):
        raise FileNotFoundError("❌ 'data/' directory not found. Please run extract and transform scripts first.")

    # Find cleaned CSV files
    json_files = [
        f for f in os.listdir(data_dir)
        if f.startswith("weather_cleaned_") and f.endswith(".json")
    ]

    if not json_files:
        raise FileNotFoundError("❌ No cleaned json file found. Make sure transform script has been run.")

    # Pick the latest cleaned file
    latest_json = sorted(json_files)[-1]
    json_path = os.path.join(data_dir, latest_json)

    # Load CSV
    df = pd.read_json(json_path)

    # Check if DataFrame is not empty
    assert not df.empty, "❌ CSV file is empty."

    # Check for required columns
    required_columns = ["city", "temperature_C", "humidity_%", "weather_main"]
    for col in required_columns:
        assert col in df.columns, f"❌ Missing column: {col}"

    print("✅ All tests passed! Cleaned CSV file looks good.")

if __name__ == "__main__":
    test_transform_output()
