import csv
import json
import os

def save_results_to_csv(results, filename):
    """Save results to a CSV file."""
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Username', 'Social Network', 'URL', 'Status'])  # Example header
        for result in results:
            writer.writerow([result['username'], result['social_network'], result['url'], result['status']])

def save_results_to_json(results, filename):
    """Save results to a JSON file."""
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(results, file, ensure_ascii=False, indent=4)

# Additional functions for other output formats or operations can be added here
