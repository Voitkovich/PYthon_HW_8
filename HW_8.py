# Напишите функцию, которая сереализует содержимое текущей директории в json-файл. 
# В файле должен храниться список словарей, словарь описывает элемент внутри директории: 
# имя, расширение, тип. Если элемент - директория, то только тип и имя. 
# Пример результата для папки, где лежит файл test.txt и директория directory_test:
# [
# {
# 'name': 'test',
# 'extension': '.txt',
# 'type': 'file'
# },
# {
# 'name': 'directory_test',
# 'type': 'directory',
# }
# ]


import json
import os


def dir_walker(generation_dir):
    results = []
    for root, dirs, files in os.walk(generation_dir):                    
        for name in files:
            results.append({"name": name.split('.')[0],
                            "expansion": name.split('.')[1], 
                            "is_file": True,
                            })

            for name in dirs:
                results.append({"parent_directory": root, 
                                "name": name,
                                "is_directory": True,
                                })

    with open("output.json", "w") as json_file:
        json.dump(results, json_file, indent=4)


dir_walker("sem 9")

