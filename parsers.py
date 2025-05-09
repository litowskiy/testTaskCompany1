import requests
import xml.etree.ElementTree as ET
from datetime import date, timedelta
from collections import defaultdict
from file_utils import open_file, save_file

def parse_dates(days):  # можно устанавливать число дней назад
    td = date.today()
    sd = td - timedelta(days=days)
    return {'sd': sd.strftime("%d/%m/%Y"), 'td': td.strftime("%d/%m/%Y")}

def get_vals(cache_file):
    info = []
    ids_arr = open_file(cache_file)
    dates = parse_dates(90)
    for i in ids_arr:
        response = requests.get(
            f'https://www.cbr.ru/scripts/XML_dynamic.asp?date_req1={dates["sd"]}'
            f'&date_req2={dates["td"]}&VAL_NM_RQ={i}'
        )
        info.append(response.content)
    return info

def extract_ids(url, cache_file):
    """
    функция для получения кодов валют.
    Поскольку нет необходимости использовать регулярно (валюты новые добавляются редко),
    выгружает в json-файл валюты, а сам файл переиспользуется
    """
    open_file(cache_file)
    response = requests.get(url)
    root = ET.fromstring(response.text)
    id_to_name = {}
    for item in root.findall('Item'):
        val_id = item.attrib['ID']
        name = item.find('Name').text
        id_to_name[val_id] = name
    save_file(id_to_name, cache_file)
    return id_to_name

def parse_vals(cache_file):
    vals_arr = defaultdict(list)
    info = get_vals(cache_file)
    for chunk in info:
        root = ET.fromstring(chunk)
        for record in root.findall('Record'):
            val_id = record.attrib['Id']
            dt = record.attrib['Date']
            value = float(record.find('Value').text.replace(',', '.'))
            vals_arr[val_id].append((dt, value))
    return vals_arr
