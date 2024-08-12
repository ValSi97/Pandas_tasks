"""
В программе создан DataFrame и записан в переменную df. В данном DataFrame "сбросьте" индексы строк,
представив их в виде столбца df.

Примечание: импортировать библиотеку Pandas не нужно, она уже импортирована.
"""
import pandas as pd

df = pd.DataFrame(
    data={'data': [1, 2, 3], 'age': [4, 5, 6], 'col_3': [7, 8, 9]}
)
df.reset_index(inplace=True)
print(df)
