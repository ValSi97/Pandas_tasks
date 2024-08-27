"""
В программе создан DataFrame и записан в переменную df.

Отсортируйте DF по столбцу "зарплата". Изменения должны коснуться исходного DF.

Примечание: импортировать библиотеку Pandas не нужно, она уже импортирована.
"""

import pandas as pd
import numpy as np

df = pd.DataFrame(data={'год рождения': [i for i in range(88, 93)],
                        'стаж работы': [3.25, 4.50, 5.75, 6.25, 7.50],
                        'зарплата': [60, 70, np.nan, np.nan, 100]},
                  index=[i for i in range(3, 8)]
                  )
df.sort_values('зарплата', inplace=True)

print(df)
