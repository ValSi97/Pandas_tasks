"""
В программе создан DataFrame и записан в переменную df. З
амените пропуски в столбцах "name" и "count" на "No_name" и число 10 соответственно.
Примените изменения к df с помощью специального аргумента.

Примечание: импортировать библиотеку Pandas не нужно, она уже импортирована.
"""
import pandas as pd
import numpy as np

df = pd.DataFrame(data={
    'name': [np.nan, 1, 2, np.nan, 3],
    'age': [np.nan, 4.50, 5.75, np.nan, 7.50],
    'count': range(60000, 110000, 10000)
})
df.fillna({'name': 'No_name', 'count': 10}, inplace=True)
print(df)