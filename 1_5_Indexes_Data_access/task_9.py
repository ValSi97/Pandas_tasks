"""
В программе созданы DataFrame и Series и записаны в переменные df и ser.
Создайте новый столбец "new_col" и запишите в него ser.

Примечание: импортировать библиотеку Pandas не нужно, она уже импортирована.
"""
import pandas as pd

df = pd.DataFrame(
    data={'data': [1, 2, 3], 'age': [4, 5, 6], 'name': [7, 8, 9]}
)
ser = pd.Series([1, 2, 3])
df['new_col'] = ser
print(df)
