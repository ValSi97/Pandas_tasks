"""
dict_in = {'col_1': [1, 2, 3, 4, 5],
           'col_2': [1, 2, 3, 4, 5],
           'col_3': [1, 2, 3, 4, 5]}
 На основе данного словаря создайте DataFrame и запишите его в переменную df.
 После чего поменяйте индексы строк на row_1, row_2, row_3, row_4, row_5.
"""

import pandas as pd

dict_in = {'col_1': [1, 2, 3, 4, 5],
           'col_2': [1, 2, 3, 4, 5],
           'col_3': [1, 2, 3, 4, 5]}
df = pd.DataFrame(
    data=dict_in
)
df.index = ('row_1, row_2, row_3, row_4, row_5'.split(', '))

print(df)
