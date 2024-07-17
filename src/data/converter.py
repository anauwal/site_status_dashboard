import csv
import json

def csv_to_json(csv_file_path, json_file_path):
    # Create a dictionary
    data = []

    # Read the CSV and add the data to the dictionary
    with open(csv_file_path, mode='r', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            # Clean up the row by stripping whitespace from keys and values
            clean_row = {key.strip(): value.strip() if value.strip() else "" for key, value in row.items()}
            data.append(clean_row)

    # Write the data to a JSON file
    with open(json_file_path, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)

# Example usage
csv_file_path = 'export.csv'  # Path to your CSV file
json_file_path = 'export.json'  # Path to the output JSON file
csv_to_json(csv_file_path, json_file_path)
