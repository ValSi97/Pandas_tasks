"""
Расчет продуктовой метрики DAU. DAU - количество уникальных пользователей в день.

В программе созданы файлы с данными - "user_visit.csv".

Файл "user_visit.csv" содержит столбцы:
            'user' - имена пользователей приложения,
            'date' - дата когда пользователи заходили в приложение.

Рассчитайте метрику DAU.

Результат запишите в переменную dau.

Скачайте файлы  user_visit.csv чтобы решить упражнение локально, перед отправкой его на проверку.
"""
import pandas as pd
import numpy as np
import random as rd

df = pd.read_csv('user_visit.csv')
#dau = df.copy().groupby('date', as_index=False).agg(DAU=('user', 'count'))
dau = df.copy().groupby('date', as_index=False)['user'].nunique()
dau.rename(columns={'user': 'DAU'}, inplace=True)
#dau = dau.groupby('date', as_index=False)['user'].agg(DAU=('user', len(dau['user'])))
#dau['DAU'] = dau['user'].str.len()
#dau = dau[['date', 'DAU']]
print(dau)

