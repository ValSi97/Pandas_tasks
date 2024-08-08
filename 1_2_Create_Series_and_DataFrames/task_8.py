"""Создайте DataFrame содержащий 3 столбца и 3 строки, индексы строк должны иметь следующие имена: row_1, row_2, row_3.

Результат запишите в переменную df."""

# Импортируйте библиотеку Pandas.
import pandas as pd

df = pd.DataFrame(
    data={'col_1': [1, 2, 3], 'col_2': [4, 5, 6], 'col_3': [7, 8, 9]},
    index='row_1, row_2, row_3'.split(', ')
)

print(df)
