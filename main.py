# main.py
from parsers import extract_ids, parse_vals
from file_utils import open_file
import os
from dotenv import load_dotenv
import argparse
load_dotenv()

def get_max(data, id_to_name):
    for valuta, info in data.items():
        maxx = max(info, key=lambda x: x[1])
        print(id_to_name[valuta], ' | ', maxx[0], ' | ', maxx[1])

def get_min(data, id_to_name):
    for valuta, info in data.items():
        minn = min(info, key=lambda x: x[1])
        print(id_to_name[valuta], ' | ', minn[0], ' | ', minn[1])

def count_mean(data, id_to_name):
    for valuta, info in data.items():
        mean_val = round(sum(v for _, v in info) / len(info), 4)
        print(id_to_name[valuta], ' | ', mean_val)

def parse_args():
    parser = argparse.ArgumentParser(description="Анализ курса валют")
    parser.add_argument('--cache-file', required=True)
    parser.add_argument('--days', required=True)
    return parser.parse_args()

def main():

    args = parse_args()
    cache_file = args.cache_file
    days = args.days

    data = parse_vals(cache_file)
    id_to_name = open_file(cache_file)

    if not os.path.exists(cache_file):
        extract_ids('http://www.cbr.ru/scripts/XML_val.asp?d=0', cache_file)

    print(f"Загрузка курсов валют за период последних {days} дней")

    print("\nМаксимальные значения:")
    get_max(data, id_to_name)

    print("\nМинимальные значения:")
    get_min(data, id_to_name)

    print("\nСредние значения:")
    count_mean(data, id_to_name)

if __name__ == "__main__":
    main()
