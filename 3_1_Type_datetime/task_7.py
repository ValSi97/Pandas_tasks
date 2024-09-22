"""
В программе создан DataFrame и записан в переменную df.

Поменяйте тип данных в столбце "date" на "datetime",
а также добавьте столбец с годом "year" и столбец с днем недели в виде числа "weekday".
"""
import pandas as pd
import numpy as np
import random as rd

df = pd.DataFrame(
    {
        'id': [i for i in range(10000, 10020)],
        'date': [rd.choice(pd.date_range('2016-03-14', '2018-03-14')) for i in range(20)]
    }
)
df['date'] = df['date'].astype('datetime64[ns]')
df['year'] = df['date'].dt.year
df['weekday'] = df['date'].dt.weekday
print(df)
