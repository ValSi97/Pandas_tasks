"""
В программе создан DataFrame и записан в переменную df.

В столбце "name" находятся имена студентов. Нужно получить серию,
показывающую сколько раз каждое имя встречается в столбце "name".


Результат запишите в переменную new_ser.

Примечание: импортировать библиотеку Pandas не нужно, она уже импортирована.
"""

import pandas as pd
import numpy as np
import random as rd

df = pd.DataFrame(data={'city': ['Город_' + str(rd.choice(range(10))) for i in range(100)],
                        'name': ['Имя_' + str(rd.choice(range(10))) for i in range(100)]}
                  )
new_ser = df['name'].value_counts()
print(new_ser)
