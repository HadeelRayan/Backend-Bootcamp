import json
import random
import time
from datetime import datetime


def json_interaction_with_fault_tolerance(file_path, operation="read", data=None):
    failure_probability = 0.2

    def raise_random_exception_with_probability():
        nonlocal failure_probability
        if random.random() < failure_probability:
            random_exception = random.choice([
                FileNotFoundError,
                PermissionError,
                IsADirectoryError,
                FileExistsError,
                NotADirectoryError,
                IOError,
            ])
            raise random_exception("Random exception raised")
        else:
            if operation == "read":
                with open(file_path, 'r') as file:
                    return json.load(file)
            elif operation == "write" and data is not None:
                with open(file_path, 'w') as file:
                    json.dump(data, file, indent=4)
            if failure_probability < 1.0:
                failure_probability += 0.05

    while True:
        try:
            return raise_random_exception_with_probability()
        except Exception as e:
            print(f"Error: {e}. Retrying operation...")
            time.sleep(1)


def process_records(file_path):
    living_rabbits = 100  # Starting population
    try:
        records = json_interaction_with_fault_tolerance(file_path, operation="read")
        processed_records = 0

        for record in records:
            if processed_records % 10 == 0 and processed_records > 0:
                print(f"Total living rabbits after processing {processed_records} records: {living_rabbits}")

            births = record['births']
            deaths = record['deaths']

            if deaths > living_rabbits:
                print(f"Error in record {record['timestamp']}: Deaths exceed living rabbits. Record ignored.")
                continue

            living_rabbits += (births - deaths)
            processed_records += 1

    except Exception as e:
        print(f"Failed to process records due to error: {e}")

    print(f"Final count of living rabbits: {living_rabbits}")
