"""
В программе создан DataFrame и записан в переменную df. В текущем DataFrame поменяйте индексы строк на столбец "data".

Примечание: импортировать библиотеку Pandas не нужно, она уже импортирована.
"""
import pandas as pd

df = pd.DataFrame(
    data={'data': [1, 2, 3], 'age': [4, 5, 6], 'col_3': [7, 8, 9]}
)
df.index = df['data']
print(df)
