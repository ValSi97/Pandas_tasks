"""
В программе создан DataFrame и записан в переменную df.

Получите количество уникальных значений в столбце "name" и уникальные значения в столбце "age".
Запишите их в переменные count и value соответственно.

Примечание: импортировать библиотеку Pandas не нужно, она уже импортирована.
"""

import pandas as pd
import numpy as np

df = pd.DataFrame(data={'name': ['Сергей', 'Сергей', 'Ксюша', 'Аристарх', 'Соня'],
                        'age': [53, 37, 11, 18, 7],
                        'наличие авто': [True, True, False, True, False]},
                  index=['row_' + str(i) for i in range(5)]
                  )
count = int(len(df['name'].unique()))
value = df['age'].unique()


print(count, value)
