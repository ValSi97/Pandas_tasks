"""
В программе создан DataFrame и записан в переменную df.

В индексах строк "weekday" дни недели идут по порядку, 0 - Пн, 6 - Вс. Получите среднее значение в каждых выходных (Сб + Вс).

Результат запишите в переменную new_df.
"""
import pandas as pd
import numpy as np
import random as rd

df = pd.DataFrame(
    {
        'weekday': [rd.choice(range(7)) for i in range(100)],
        'sum':  [float(rd.choice(range(1, 200))) for i in range(100)]
    }
)
df.set_index('weekday', inplace=True)
new_df = df.loc[((df.index == 5) | (df.index == 6))].rolling(window=2, min_periods=1).agg('mean')
new_df = new_df.loc[(new_df.index == 6)]
print(new_df)
