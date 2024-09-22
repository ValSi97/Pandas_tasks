"""
В программе создан DataFrame и записан в переменную df.
Получите только те строки в которых в столбце "age" нет пропусков,
а в столбце "count" число меньше или равно 5.

Результат запишите в переменную new_df.

Примечание: импортировать библиотеку Pandas не нужно, она уже импортирована.
"""
import pandas as pd
import numpy as np

df = pd.DataFrame(data={
    'name': [np.nan, 1, 2, np.nan, 3],
    'age': [np.nan, 4.50, 5.75, np.nan, 7.50],
    'count': range(5)
})
new_df = df[(~ df['age'].isna()) & (df['count'] <= 5)]
print(new_df)