"""
В прошлом задании вы создали столбец "new_col". Он явно там лишний, удалите его.

Примечание:

DataFrame записан в переменную df
импортировать библиотеку Pandas не нужно, она уже импортирована.
"""
import pandas as pd

df = pd.DataFrame(
    data={'data': [1, 2, 3], 'age': [4, 5, 6], 'name': [7, 8, 9]}
)

df['new_col'] = df['age']
print(df)

del df['new_col']
print(df)
