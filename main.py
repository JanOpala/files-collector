import os
import argparse
from path_preparation import set_local_directory, prepare_paths
from data_generation import generate_data


if __name__ == "__main__":
    set_local_directory()
    print(os.getcwd())
    parser = argparse.ArgumentParser(description="Pliki zbieracza danych")
    parser.add_argument("--miesiące", "-m", nargs="+", default=["styczen","luty"], help="Miesiące")
    parser.add_argument("--dni", "-d", nargs="+", default=["pn-wt", "pt"], help="Dni tygodnia")
    parser.add_argument("--pory_dnia", "-p", nargs="+", default=["r","w"], help="Pory dnia")
    parser.add_argument("--tryb", "-t", choices=["t", "o"], required=True, help="Tryb działania: 't' - tworzenie, 'o' - odczyt")
    parser.add_argument("--format", "-f", choices=["j", "c"], required=True, help="Format pliku: 'j' - JSON, 'c' - CSV")
    args = parser.parse_args()
    paths = prepare_paths(args.miesiące, args.dni, args.pory_dnia)
    generate_data(paths,  args.tryb, args.format)