"""dict_in = {'col_1': [1, 2, 3],
           'col_2': [4, 5, 6],
           'col_3': [7, 8, 9],
           'col_4': [10, 11, 12]}
На основе данного словаря создайте DataFrame состоящий только из col_2 и col_3, индексы строк должны иметь следующие имена: row_1, row_2, row_3.

Результат запишите в переменную df."""

# Импортируйте библиотеку Pandas.
import pandas as pd

dict_in = {'col_1': [1, 2, 3],
           'col_2': [4, 5, 6],
           'col_3': [7, 8, 9],
           'col_4': [10, 11, 12]}
df = pd.DataFrame(
    data=dict_in,
    columns=['col_2', 'col_3'],
    index='row_1, row_2, row_3'.split(', ')
)

print(df)
