"""
В программе создан DataFrame и записан в переменную df.
С помощью специального свойства определите есть ли пропуски в индексах строк.

В переменную nan_in_indx запишите True если пропуски есть и False если пропусков нет.

Примечание: импортировать библиотеку Pandas не нужно, она уже импортирована.
"""

import pandas as pd

df = pd.DataFrame(
    data={'col_1': [1, 2, 3], 'col_2': [4, 5, 6], 'col_3': [7, 8, 9]}
)
nan_in_indx = df.index.hasnans

print(nan_in_indx)
