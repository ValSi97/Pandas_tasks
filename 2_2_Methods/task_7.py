"""
В программе создан DataFrame и записан в переменную df.

В столбце 'name' указано имя студента, столбцы с 1 до 50 - это номера задач.

Получите DF/маску, в которой вместо элементов со значением 1, стоит значение True,
а  все остальные элементы равны False. Значения в столбце 'name' не должны быть изменены.

Результат запишите в переменную new_df.

Примечание: импортировать библиотеки Pandas и Numpy не нужно, они уже импортированы.
"""

import pandas as pd
import numpy as np
import random


df = pd.DataFrame(columns=(['name']+[i for i in range(1, 51)]),
                  data=[['Имя_'+str(j)]+[random.choice([1.0, np.nan, 0.0]) for i in range(1, 51)] for j in range(10)],
                  index=[i for i in range(10)]
                  )

#new_df = pd.concat([df['name'], df.iloc[:, 1:50].isin([1])], axis=1, ignore_index=False)
new_df = pd.concat([df['name'], df.iloc[:, 1:].isin([1])], axis=1)
print(new_df)
