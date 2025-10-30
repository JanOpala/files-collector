import os
import pathlib
from day_slicer import prepare_day_slice, pory_dnia

def set_local_directory():
    os.chdir(pathlib.Path(__file__).parent.resolve())
    
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