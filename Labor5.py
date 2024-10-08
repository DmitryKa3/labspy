import os
import datetime

def infofromdirect(direct, file):
    with open(file, 'w', encoding='utf-8') as file:
        list = os.listdir(direct)
        for id, name in enumerate(list, start=1):
            info = os.stat(os.path.join(direct, name))
            file.write(f"Файл {id}:\n")
            file.write(f"Имя: {name}\n")
            file.write(f"Формат: {name.split('.')[-1]}\n")
            file.write(f"Размер: {info.st_size} bait\n")
            file.write(f"Дата создания: {datetime.datetime.fromtimestamp(info.st_ctime)}\n")
            file.write("\n")
print("Введите директорию")
dir = input()
f = "D:/py/lab1/Labspy/labor5file.txt"
try:
    infofromdirect(dir, f)
except: print("Директория задана некоректно"); exit()
print("Успешно")