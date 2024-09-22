"""
В программе создан файл с данными - "users_action.csv".

Файл содержит четыре столбца:
    'user' - содержит имена пользователей приложения,
    'device' - устройство, с которого пользователи заходили в приложение
    ('PC' - компьютер, 'laptop' - ноутбук, 'phone' - смартфон),
    'action' - совершил пользователь целевое действие или нет(True - совершил, False - не совершил),
    'date' - дата когда пользователи заходили в приложение.

Получите DF, показывающий, сколько раз пользователи совершали целевое действие, зайдя в приложение со смартфона.

Результат запишите в переменную new_df.
"""
import pandas as pd
import numpy as np
import random
import datetime

# df = pd.DataFrame(
#     {'user': [f'user_{random.choice([1, 2, 3, 4])}' for i in range(25)],
#      'device': [random.choice(['PC', 'laptop', 'phone']) for i in range(25)],
#      'action': [random.choice([True, False]) for i in range(25)],
#      'date': [datetime.date.today() + datetime.timedelta(days=i) for i in range(25)]
#      }
# )
# df.to_csv('users_action.csv', encoding='utf-8', index=False)

#не проходит
# df = pd.read_csv('users_action.csv')
# new_df = df.groupby('user').apply(lambda x: ((x['device'] == 'phone') & (x['action'])).to_frame('action_True'))
#new_df = df.groupby('user', as_index=True)[['device', 'action']].apply(lambda x: ((x['device'] == 'phone') & (x['action'])).to_frame('action_True'))
#new_df = new_df.groupby('user').agg('sum')

df = pd.read_csv('users_action.csv')
new_df = (df[df['device'] == 'phone'].groupby('user', as_index=True)
          .apply(lambda x: ((x['action']).agg('sum')))
          .to_frame('action_True'))
# new_df=df.groupby(['user']).apply(lambda x: (x['device']=='PC').agg('mean').astype(int)).to_frame().reset_index()
# df = pd.read_csv('users_action.csv')
# new_df = df[df['device'] == 'phone']
print(new_df)
