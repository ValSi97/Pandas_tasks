"""
В программе создан DataFrame и записан в переменную df.


В столбцах с типом данных 'int64' измените тип данных на 'int32'.

Результат запишите в переменную new_df.

Примечание: импортировать библиотеку Pandas не нужно, она уже импортирована.
"""

import pandas as pd
import numpy as np
import random


def mapper(series):
    if series.dtypes == 'int64':
        return series.astype('int32')
    else:
        return series


df = pd.DataFrame(columns=([f'col_{i}' for i in range(100)]),
                  data=[[random.choice(range(100)) if j % 2 == 0
                         else random.choice(range(11, 50)) / 10.0 for j in range(100)]
                        for j in range(100)],
                  )
new_df = df.apply(mapper)
print(df)
