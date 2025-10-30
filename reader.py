import json 
import csv

def read(file_path, format):
    if format == "j":
        with open(file_path, "r") as f:
            data = json.load(f)
            print(f"Odczytany plik {file_path}")
            print(data)
    elif format == "c":
        reader = csv.DictReader(open(file_path))
        data = [row for row in reader]
        print(f"Odczytany plik {file_path}")
        print(data)