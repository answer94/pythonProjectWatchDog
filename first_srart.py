import json
import os
import time

import ExcelSave

filecontrol_path = input('Ведите путь до контроллируемой директории ')
# filecontrol_path = r"C:\Users\afanaskin\Desktop\Новая папка (2)"


dict_path = dict()
list_filepath = list()
list_delete_file = list()
ExcelSave.first_start()



for root, dirs, files in os.walk(filecontrol_path):
    for filename in files:
        filepath = str(root) + '\\' + str(filename)
        list_filepath.append(filepath)
        if dict_path.get(filepath, 0) == 0:
            dict_path[filepath] = True
            print(filepath)
            ExcelSave.add_path(filepath)

count_file = len(list_filepath)

with open('json_file.json', 'w') as f:
    json.dump(dict_path, f)
    list_filepath.clear()


