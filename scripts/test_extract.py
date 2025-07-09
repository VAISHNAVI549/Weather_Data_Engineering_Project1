import os
import json


def test_extract_output():
    data_dir = "data"

    # Find raw weather data files
    json_files = [
        f for f in os.listdir(data_dir)
        if f.startswith("weather_raw_") and f.endswith(".json")
    ]
    assert json_files, "❌ No raw weather JSON file found."

    latest_file = sorted(json_files)[-1]
    path = os.path.join(data_dir, latest_file)

    # Test 1: File exists
    assert os.path.exists(path), "❌ Output JSON file does not exist."

    # Test 2: Valid JSON
    with open(path, 'r') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            assert False, "❌ File is not valid JSON."

    # Test 3: Not empty
    assert len(data) > 0, "❌ Output file is empty."

    # Test 4: Check essential fields in each city entry
    required_keys = ["name", "dt", "main", "weather", "wind"]
    for entry in data:
        for key in required_keys:
            assert key in entry, f"❌ Missing key '{key}' in entry."

    print("✅ All tests passed for extract script!")


if __name__ == "__main__":
    test_extract_output()
