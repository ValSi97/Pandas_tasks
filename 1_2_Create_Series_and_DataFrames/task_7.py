"""Создайте DataFrame содержащий 3 столбца и 3 строки.

Результат запишите в переменную df."""

# Импортируйте библиотеку Pandas.
import pandas as pd

df = pd.DataFrame(
    {'col_1': [1, 2, 3], 'col_2': [4, 5, 6], 'col_3': [7, 8, 9]}
)

print(df)
