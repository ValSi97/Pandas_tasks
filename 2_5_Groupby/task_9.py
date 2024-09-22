"""
В программе создан файл с данными - "users.csv".

Файл содержит три столбца:
'user' - содержит имена пользователей приложения,
'device' - устройство, с которого пользователи заходили в приложение
    ('PC' - компьютер, 'laptop' - ноутбук, 'phone' - смартфон),
'date' - дата когда пользователи заходили в приложение.

Получите список\массив пользователей, которые заходили в приложение только с персонального компьютера('PC').

Результат запишите в переменную user_list.

Скачайте файл users.csv, чтобы решить упражнение локально, перед отправкой его на проверку.

Примечание: импортировать библиотеку Pandas не нужно, она уже импортирована.
"""
import pandas as pd
import numpy as np
import random
import datetime

# df = pd.DataFrame(
#     {'user': [f'user_{random.choice([1, 2, 3, 4])}' for i in range(10)],
#      'device': [random.choice(['PC', 'laptop', 'phone']) for i in range(10)],
#      'date': [datetime.date.today() + datetime.timedelta(days=i) for i in range(10)]
#      }
# )
# df.to_csv('users.csv', encoding='utf-8', index=False)
df = pd.read_csv('users.csv')
user_list_pc = df.query('`device` not in ["laptop", "phone"]')['user'].unique()
user_list_other = df.query('`device` in ["laptop", "phone"]')['user'].unique()
#user_list = df[df['device'] == 'PC']['user'].unique()
user_list = df[df['user'].apply(lambda x: x in user_list_pc and x not in user_list_other)]['user'].unique()
print(user_list_pc, user_list_other)
print(user_list)
