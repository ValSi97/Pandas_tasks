"""
В программе создан DataFrame и записан в переменную df. Удалите столбцы с именами "id" и "product".

Результат запишите в переменную new_df.

Примечание: импортировать библиотеку Pandas не нужно, она уже импортирована.
"""
import pandas as pd
import numpy as np
import random

#df = pd.DataFrame(data=random.choices(range(200), k=100), index=['Имя_'+str(iter) for iter in range(100)], columns=['Решено'])

df = pd.DataFrame(columns=(['Упр_' + str(i) for i in range(1, 119)]+['id', 'product']),
                  data=[[random.choice([1.0, np.nan]) for i in range(1, 121)] for j in range(100)],
                  index=[i for i in range(100)]
                  )
new_df = df.drop(columns=['id', 'product'])
print(new_df)