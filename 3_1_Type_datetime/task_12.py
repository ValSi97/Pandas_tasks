"""
Расчет продуктовой метрики WAU. WAU - количество уникальных пользователей в неделю.
В программе созданы файлы с данными - "user_visit.csv".

Файл "user_visit.csv" содержит столбцы:
            'user' - имена пользователей приложения,
            'date' - дата когда пользователи заходили в приложение.

Рассчитайте метрику WAU.
Результат запишите в переменную wau.
Элементы индекса строк - это порядковый номер недели в году.
Начинаются с 52, тк первое января 2023 года это конец недели начавшейся в 2022 году.
Метод groupby() по умолчанию сортирует данные по группируемому столбцу\столбцам,
тк аргумент sort по умолчанию имеет значение True.
Иногда нужно сохранить исходный порядок в группируемом столбце\столбцах,
для этого в аргумент sort нужно передать False.
Скачайте файлы  user_visit.csv чтобы решить упражнение локально, перед отправкой его на проверку.
"""

import pandas as pd
import numpy as np
import random as rd

df = pd.read_csv('user_visit.csv')
df['week_num'] = df['date'].astype('datetime64[ns]').dt.isocalendar().week
wau = df[['user', 'week_num']].copy()
wau = wau.groupby('week_num', as_index=False, sort=False).agg(WAU=('user', 'nunique')).set_index('week_num')
#dau.rename(columns={'user': 'DAU'}, inplace=True)
print(wau)
