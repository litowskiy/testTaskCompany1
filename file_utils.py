import os
import json

def open_file(cache_file):  #открытие файла (если существует — сразу возврат)
    if os.path.exists(cache_file):
        with open(cache_file, 'r') as f:
            return json.load(f)

def save_file(ids, cache_file):  #сохранение файла
    with open(cache_file, 'w') as f:
        json.dump(ids, f)
