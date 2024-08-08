"""
В программе создан DataFrame и записан в переменную df.
Получите уникальные значения в индексах строк и столбцов
и запишите их в переменные unique_ind и unique_cols соответственно.

Примечание: импортировать библиотеку Pandas не нужно, она уже импортирована.
"""

import pandas as pd

df = pd.DataFrame(
    data={'col_1': [1, 2, 3], 'col_2': [4, 5, 6], 'col_3': [7, 8, 9]}
)
unique_ind = df.index.unique()
unique_cols = df.columns.unique()

print(unique_ind, unique_cols)
