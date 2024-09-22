"""
В программе создан файл с данными - "users.csv".

Файл содержит три столбца: 'user' - содержит имена пользователей приложения,
'device' - устройство, с которого пользователи заходили в приложение
    ('PC' - компьютер, 'laptop' - ноутбук, 'phone' - смартфон),
'date' - дата когда пользователи заходили в приложение.

Получите список\массив пользователей, которые заходили в приложение со всех устройств.

Результат запишите в переменную user_list.
"""
import pandas as pd
import numpy as np
import random
import datetime

# df = pd.DataFrame(
#     {'user': [f'user_{random.choice([1, 2, 3, 4])}' for i in range(25)],
#      'device': [random.choice(['PC', 'laptop', 'phone']) for i in range(25)],
#      'date': [datetime.date.today() + datetime.timedelta(days=i) for i in range(25)]
#      }
# )
# df.to_csv('users.csv', encoding='utf-8', index=False)

df = pd.read_csv('users.csv')
# такое решение не хавает...
user_device_ser = df.groupby('user')['device'].unique()
user_device_df = pd.DataFrame({'user': user_device_ser.index, 'device': user_device_ser.values})
user_list = user_device_df[user_device_df['device'].apply(lambda x: sorted(x) == sorted(['PC', 'laptop', 'phone']))]['user'].unique()
print(df)
print(user_device_df)
print(user_list)
