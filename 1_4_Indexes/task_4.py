"""
В программе создан DataFrame и записан в переменную df. Получите список с индексами строк и список
с индексами столбцов и запишите их переменные list_ind и list_cols.

Примечание: импортировать библиотеку Pandas не нужно, она уже импортирована.
"""
import pandas as pd

df = pd.DataFrame(
    data={'col_1': [1, 2, 3], 'col_2': [4, 5, 6], 'col_3': [7, 8, 9]}
)
list_ind = list(df.index)
list_cols = list(df.columns)

print(list_ind, list_cols)
