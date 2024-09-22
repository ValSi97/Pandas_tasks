"""
В программе создан DataFrame и записан в переменную df.
Удалите строки в которых в столбцах "name" и "age" есть пропуски.
Примените изменения к df с помощью специального аргумента.

Примечание: импортировать библиотеку Pandas не нужно, она уже импортирована.
"""
import pandas as pd
import numpy as np

df = pd.DataFrame(data={
    'name': [np.nan, 1, 2, np.nan, 3],
    'age': [np.nan, 4.50, 5.75, np.nan, 7.50],
    'зарплата': range(60000, 110000, 10000)
})
df.dropna(subset=['name', 'age'], axis=0, inplace=True)
print(df)