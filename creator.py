import json
import csv

def generate_json(path, data):
        with open(path, "w") as f:
            json.dump(data, f)

def generate_csv(path, data):
    keys = data[0].keys()
    with open(path, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(keys)
        for key, value in data[0].items():
            writer.writerow([value])

def create(file_path, format, data):
    if format == "j":
        generate_json(file_path, data)
    elif format == "c":
        generate_csv(file_path, data)