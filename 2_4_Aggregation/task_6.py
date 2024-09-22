"""
В программе создан DataFrame и записан в переменную df.
Подсчитайте минимальное значение, максимальное значение и сумму в столбце "price".
Используйте функции Numpy np.min, np.max, np.sum.

Результат запишите в переменную new_ser.

Примечание: импортировать библиотеки Pandas и Numpy не нужно, они уже импортированы.
"""

import pandas as pd
import numpy as np
import random as rd

df = pd.DataFrame(data={'product': ['Товар_' + str(rd.choice(range(1, 10))) for i in range(100)],
                        'price': [rd.choice(range(1000, 10000, 1000)) for i in range(100)],
                        'count': [rd.choice(range(1, 10)) for i in range(100)],
                        'buy': [rd.choice(['куплено', 'не куплено']) for i in range(100)]
                        }
                  )

new_ser = df['price'].agg([np.min, np.max, np.sum])
print(new_ser)
