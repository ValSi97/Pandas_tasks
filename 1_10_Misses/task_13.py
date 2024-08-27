"""
В программе создан DataFrame и записан в переменную df.

Получите список со студентами курса "Pandas для анализа данных", у которых нет решенных задач.

1 - задача решена, Nan - задача не решена.

Результат запишите в переменную stud_list.

Примечание: импортировать библиотеку Pandas не нужно, она уже импортирована.
"""
import pandas as pd
import numpy as np
import random

#df = pd.DataFrame(data=random.choices(range(200), k=100), index=['Имя_'+str(iter) for iter in range(100)], columns=['Решено'])

df = pd.DataFrame(columns=['Упр_' + str(i) for i in range(1, 121)],
                  data=[[random.choice([1.0, np.nan]) for i in range(1, 121)] for j in range(100)],
                  index=['Имя_' + str(i) for i in range(100)]
                  )
temp = {'Упр_0': [1, np.nan, 1],
        'Упр_1': [np.nan, np.nan, np.nan],
        'Упр_2':[1, np.nan, np.nan]}

df = pd.DataFrame(data=temp, index=[f'Имя_{i}' for i in range(3)], columns=[f'Упр_{i}' for i in range(3)])

stud_list = df[df.isna().all(axis=1)].index.to_list()
#stud_list = df[df.notna()].index.to_list()
print(df)
print(stud_list)