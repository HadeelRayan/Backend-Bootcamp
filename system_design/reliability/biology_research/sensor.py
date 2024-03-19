import json
import random
import time
from datetime import datetime
import json_fns as fns


def generate_record():
    """Generate a single sensor record."""
    return {
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'births': random.randint(0, 10),
        'deaths': random.randint(0, 10)
    }


def write_record_to_file(file_path, record):
    try:
        fns.raise_random_exception_with_probability()  # Attempt to simulate a failure

        # If no exception was raised, proceed to append the record to the file
        with open(file_path, 'r+') as file:
            # Read existing data
            file.seek(0)
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                # Handle empty file by initializing data as an empty list
                data = []

            # Append new record and write back to file
            data.append(record)
            file.seek(0)
            json.dump(data, file, indent=4)
            file.truncate()

        print("Record successfully written to file.")

    except FileNotFoundError:
        print("FileNotFoundError: The file was not found.")
    except PermissionError:
        print("PermissionError: You don't have permission to access this file.")
    except IsADirectoryError:
        print("IsADirectoryError: The specified path is a directory, not a file.")
    except FileExistsError:
        print("FileExistsError: The file already exists.")
    except NotADirectoryError:
        print("NotADirectoryError: A component of the path is not a directory.")
    except IOError:
        print("IOError: An I/O error occurred.")
    finally:
        global failure_probability
        failure_probability = 0


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
