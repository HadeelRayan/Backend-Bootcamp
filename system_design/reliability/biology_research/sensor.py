import json
import random
import time
from datetime import datetime


def generate_record():
    """Generate a single sensor record."""
    return {
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'births': random.randint(0, 10),
        'deaths': random.randint(0, 10)
    }


def write_record_to_file(file_path, record):
    """Append a record to the JSON file, ensuring data integrity."""
    try:
        with open(file_path, 'r+') as file:
            # Move to the beginning of the file, read existing data, then return to start
            file.seek(0)
            data = json.load(file)
            file.seek(0)
            data.append(record)
            json.dump(data, file, indent=4)
            file.truncate()  # Remove any remaining part of old data
    except FileNotFoundError:
        # If the file does not exist, create it and write the record as the first entry
        with open(file_path, 'w') as file:
            json.dump([record], file, indent=4)


def create_sensor_record(file_path, total_records=100):
    records = []
    for _ in range(total_records):
        record = generate_record()
        write_record_to_file(file_path, record)
        print(f"Generated record: {record}")
        time.sleep(random.randint(5, 10))  # waits for a random interval between 5 and 10 sec

    # Write records to the JSON file
    with open(file_path, 'w') as file:
        json.dump(records, file, indent=4)


file_path = 'sensor_data.json'
create_sensor_record(file_path, total_records=10)
#return file_path
