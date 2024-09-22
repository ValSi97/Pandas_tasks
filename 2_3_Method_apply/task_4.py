"""
В программе создан DataFrame и записан в переменную df.


Получите серию, в которой значения 'city_1' замените на 0, а все остальные на 1. Используйте метод apply() и lambda функцию.

Результат запишите в переменную new_ser.
"""

import pandas as pd
import numpy as np
import random as rd

df = pd.DataFrame(data={'city': ['city_' + str(rd.choice(range(1, 3))) for i in range(5)]
                        }
                  )

new_ser = df['city'].apply(lambda value: 0 if value == 'city_1' else 1)
print(df)
