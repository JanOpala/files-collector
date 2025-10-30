import os
import random
from creator import create
from reader import read

def generate_data(paths, tryb, format):
    ### check if folder exist
    for path in paths:
        if not os.path.exists(path):
            os.makedirs(path)
        file = "Data.csv" if format == "c" else "Data.json"
        file_path = os.path.join(path, file) 
        exists = os.path.exists(file_path)
        ### generate data
        data = [{
            "Model": random.choice(["A", "B", "C"]),
            "Wynik": str(random.randint(0, 1000)),
            "Czas": random.randint(0, 1000)
        }]
        # print(data)
        if tryb == "t":
            if not exists:
                create(file_path, format, data)
            else:
                decision = input(f"File {file_path} exists. Do you want to overwrite it? (y/n)")
                if decision == "y":
                    os.remove(file_path)
                    create(file_path, format, data)
                elif decision == "n":
                    continue
                else:
                    print("Invalid choice")
        elif tryb == "o":
            if os.path.exists(file_path):
                read(file_path,format)
            else:
                print(f"File {file_path} does not exist")
