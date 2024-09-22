"""
Упражнение 2.

В программе создан DataFrame и записан в переменную df.
Получите серию, содержащую сумму значений каждого столбца df.

Результат запишите в переменную new_ser.

Примечание: импортировать библиотеку Pandas не нужно, она уже импортирована.
"""

import pandas as pd
import numpy as np
import random as rd


df = pd.DataFrame(data={'product': ['товар_' + str(rd.choice(range(1, 10))) for i in range(100)],
                        'product_price': [(rd.choice(range(1000, 10000, 1000))) for i in range(100)],
                        'count': [rd.choice(range(1, 10)) for i in range(100)],
                        'buy': [rd.choice([True, False]) for i in range(100)]
                        }
                  )
new_ser = df.agg(sum)
print(new_ser)
