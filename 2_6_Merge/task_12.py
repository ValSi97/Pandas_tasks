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

Получите список\массив с уникальными пользователями из Санкт-Петербурга и Москвы, заходивших в приложение с трех устройств - 'PC', 'laptop' и 'phone'.
Результат запишите в переменную user_list.
Скачайте файлы  user_merge.csv, region.csv и devices.csv,
чтобы решить упражнение локально, перед отправкой его на проверку.
Примечание: импортировать библиотеку Pandas не нужно, она уже импортирована.
"""
import pandas as pd
import numpy as np

users = pd.read_csv('user_merge.csv', )[['user', 'id_device', 'id_region']]
devices = pd.read_csv('devices.csv')[['id', 'device']]
region = pd.read_csv('region.csv')[['id', 'region']]
user_list = users.merge(devices, left_on='id_device', right_on='id', how='left')\
            .query('`device` in ["phone", "laptop", "PC"]')\

user_mask_all_devices = user_list\
                        .groupby('user')['device'].unique().apply(lambda x: len(x) == 3)
user_mask_all_devices = user_mask_all_devices[user_mask_all_devices]
user_list = user_list.merge(region, left_on='id_region', right_on='id', how='left')\
            .query('`region` in ["Санкт-Петербург", "Москва"]')['user']\
            .to_frame().merge(user_mask_all_devices, on='user', how='inner')['user'].unique()
print(user_list)
