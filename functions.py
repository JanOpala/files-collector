import json
import os
import sys
import pathlib
import csv
import random
import argparse

week = {
    "pn": "poniedziałek",
    "wt": "wtorek",
    "sr": "środa",
    "cz": "czwartek ",
    "pt": "piątek",
    "so": "sobota",
    "ni": "niedziela"
}
pory_dnia = {
    "r": "rano",
    "w": "wieczor"
}

def set_local_directory():
    os.chdir(pathlib.Path(__file__).parent.resolve())
    
def prepare_day_slice(slic):
    if "-" in slic:
        days = slic.split("-")
        week_days = list(week.keys())
        return {week[day] for day in week_days[week_days.index(days[0]):week_days.index(days[1]) + 1]}
    else:
        return [week[slic]]
    
def prepare_paths(input_months=["styczen","luty"], input_days=["pn-wt", "pt"], input_times=["r","w"]):
    assert len(input_months) == len(input_days), "Rozna liczba dni i miesiecy"
    paths_list = []
    days_count = 0
    for ix, day in enumerate(input_days):
        month = input_months[ix]
        d = prepare_day_slice(day)
        for ds in d:
            time = input_times[days_count] if days_count < len(input_times) else "r"
            path = f"{month.capitalize()}/{ds}/{pory_dnia[time]}"
            paths_list.append(path)            
            days_count += 1 ### dodaje po dniach zeby wiedziec jaka pora dnia 
    return paths_list

def create(file_path, format, data):
    def generate_json():
        with open(file_path, "w") as f:
            json.dump(data, f)
    if format == "j":
        generate_json()
    elif format == "c":
        #### Some function for json
        
def read(file_path, format):
    if format == "j":
        with open(file_path, "r") as f:
            data = json.load(f)
            print(f"Odczytany plik {file_path}")
            print(data)
    elif format == "c":
        ### reading csv

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


if __name__ == "__main__":
    set_local_directory()
    print(os.getcwd())
    # args = parse_arguments()
    # paths = prepare_paths(dargs.miesiące, args.ni, args.pory_dnia)
    # generate_data(paths,  args.tryb, args.format)