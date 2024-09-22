"""
В программе создан DataFrame, содержащий название города и количество жителей, и записан в переменную df.

Населенный пункт приобретает статус: "город" - если число жителей больше 30000;
"поселок городского типа" - если не больше 30000.
Поставьте (через пробел) соответствующий статус у названия города.

Результат должен коснуться исходного DF.
"""

import pandas as pd
import numpy as np
import random as rd


def mapper(series):
    cnt = series['кол-во жителей']
    result = series['city']
    if cnt > 30000:
        result = f'город {result}'
    else:
        result = f'поселок городского типа {result}'
    return result




df = pd.DataFrame(data={'кол-во жителей': [rd.choice(range(1000, 300000, 1000)) for i in range(1, 6)],
                        'city': [f'Name_{i}' for i in range(1, 6)]
                        }
                  )
df['city'] = df.apply(mapper, axis=1)
print(df)
