"""
В программе создан DataFrame и записан в переменную df. С помощью специальных свойств DataFrame получите индексы строк
и столбцов и запишите их в соответствующие переменные ind и cols.

Примечание: импортировать библиотеку Pandas не нужно, она уже импортирована.
"""

import pandas as pd

df = pd.DataFrame(
    data={'col_1': [1, 2, 3], 'col_2': [4, 5, 6], 'col_3': [7, 8, 9]}
)
ind = df.index
cols = df.columns

print(ind, cols)
