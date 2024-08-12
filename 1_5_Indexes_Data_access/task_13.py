"""
В программе создан DataFrame и две серии Series и записаны в переменные df, ser_1, ser_2.
В df создайте новые столбцы "new_col_1" и "new_col_2", запишите в них ser_1 и ser_2 соответственно.
Столбец "date" установите в качестве индексов строк.

Примечание: импортировать библиотеку Pandas не нужно, она уже импортирована.
"""

import pandas as pd

df = pd.DataFrame(
    data={'date': [1, 2, 3], 'age': [4, 5, 6], 'name': [7, 8, 9]}
)
ser_1 = pd.Series([11, 12, 13])
ser_2 = pd.Series([111, 112, 113])
df['new_col_1'], df['new_col_2'] = ser_1, ser_2
df.set_index('date', inplace=True)
print(df)