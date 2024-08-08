"""dict_in = {'col_1': [1, 2, 3],
           'col_2': [4, 5, 6],
           'col_3': [7, 8, 9],
           'col_4': [10, 11, 12]}
На основе данного словаря создайте DataFrame состоящий только из col_1 и col_3.

Результат запишите в переменную df."""

# Импортируйте библиотеку Pandas.
import pandas as pd

dict_in = {'col_1': [1, 2, 3],
           'col_2': [4, 5, 6],
           'col_3': [7, 8, 9],
           'col_4': [10, 11, 12]}
df = pd.DataFrame(
    data=dict_in,
    columns=['col_1', 'col_3']
)

print(df)
