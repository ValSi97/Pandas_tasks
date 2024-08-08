"""Создайте DataFrame из указанного словаря dict_in = {'col_1': [1, 2, 3], 'col_2': [4, 5, 6]}

Результат запишите в переменную df."""

# Импортируйте библиотеку Pandas.
import pandas as pd

dict_in = {'col_1': [1, 2, 3], 'col_2': [4, 5, 6]}
df = pd.DataFrame(
    dict_in
)

print(df)

