"""
В программе созданы файлы с данными - "user_merge.csv", "region.csv", "devices.csv".
Файл "user_merge.csv" содержит столбцы:
            'user' - имена пользователей приложения,
            'id_device' - id устройства, с которого пользователи заходили в приложение,
            'date' - дата когда пользователи заходили в приложение,
            'action' -  совершил пользователь целевое действие или нет(True - совершил, False - не совершил),
            'id_region' - id региона, в котором проживает пользователь.
Файл "region.csv" содержит столбцы:
            'id' - id региона,
            'region' - регион.
Файл "devices.csv" содержит столбцы:
            'id' - id устройства,
            'device' - устройство.

Получите список\массив устройств, с которыx пользователи заходили в приложение.
Результат запишите в переменную device_list.
Скачайте файлы  user_merge.csv, region.csv и devices.csv,
чтобы решить упражнение локально, перед отправкой его на проверку.
Примечание: импортировать библиотеку Pandas не нужно, она уже импортирована.
"""
import pandas as pd
import numpy as np

users = pd.read_csv('user_merge.csv', )[['user', 'id_device']]
devices = pd.read_csv('devices.csv')[['id', 'device']]
device_list = users.merge(devices, left_on='id_device', right_on='id').drop_duplicates()['device'].unique()
print(device_list)
