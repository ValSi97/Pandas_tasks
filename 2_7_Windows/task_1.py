"""
В программе создан DataFrame и записан в переменную df.

Получите скользящее среднее с шириной окна 7.

Результат запишите в переменную new_df
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
new_df = df.rolling(window=7, min_periods=1).agg('mean')
print(new_df)
print(df)
