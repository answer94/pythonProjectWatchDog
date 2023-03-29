import json
import os
import time
import ExcelSave

# file_log = input('Ведите путь до лога ')
filecontrol_path = input('Ведите путь до контроллируемой директории ')
# filecontrol_path =r"C:\Users\afanaskin\Desktop\Новая папка (2)"
# a = r'C:\Users\afanaskin\Desktop\[kts.studio, Александр Опрышко]  Асинхронное программирование на Python для начинающих (2022) part 1 (1-5)'

dict_path = dict()
list_filepath = list()
list_delete_file = list()
ExcelSave.first_start()

while True:

    try:

        with open('json_file.json') as json_file:
            dict_path = json.load(json_file)

        for root, dirs, files in os.walk(filecontrol_path):
            for filename in files:
                filepath = str(root) + '\\' + str(filename)
                list_filepath.append(filepath)
                if dict_path.get(filepath, 0) == 0:
                    dict_path[filepath] = True
                    ExcelSave.add_path(filepath)

        count_file = len(list_filepath)

        if len(dict_path.keys()) != len(list_filepath):
            for i in dict_path.keys():
                if i not in list_filepath:
                    list_delete_file.append(i)
                    ExcelSave.del_path(i)
                    dict_path.pop(i)

        list_delete_file.clear()
        list_filepath.clear()
        with open('json_file.json', 'w') as f:
            json.dump(dict_path, f)

        time.sleep(5)
    except Exception as e:
        pass
    finally:
        with open('json_file.json', "w") as f:
            json.dump(dict_path, f)
