"""
В программе создан DataFrame и записан в переменную df.
Получите количество уникальных значений в индексах строк
и столбцов и запишите их в переменные nunique_ind и nunique_cols соответственно.

Примечание: импортировать библиотеку Pandas не нужно, она уже импортирована.
"""

import pandas as pd

df = pd.DataFrame(
    data={'col_1': [1, 2, 3], 'col_2': [4, 5, 6], 'col_3': [7, 8, 9]}
)
nunique_ind = df.index.nunique()
nunique_cols = df.columns.nunique()

print(nunique_ind, nunique_cols)
