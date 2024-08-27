"""
В программе создан DataFrame и записан в переменную df.

К значениям в столбцах ['year_1', 'year_2', 'year_3', 'year_4', 'year_5', 'year_6', 'year_7', 'year_8'] прибавьте 2000.

Результат запишите в переменную new_df.

В DF могут быть не все указанные столбцы.
"""

import pandas as pd
import numpy as np
import random

columns = ['year_1', 'year_2', 'year_3', 'year_4', 'year_5', 'year_6', 'year_7', 'year_8']


def mapper(series):
    if series.name in columns:
        return series + 2000
    else:
        return series


df = pd.DataFrame(columns=([f'col_{i}' for i in range(100)]),
                  data=[[random.choice(range(100)) if j % 2 == 0
                         else random.choice(range(11, 50)) / 10.0 for j in range(100)]
                        for j in range(100)],
                  )
new_df = df.apply(mapper)
print(new_df)
