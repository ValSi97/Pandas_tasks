"""
В программе создан DataFrame и записан в переменную df.
Подсчитайте количество элементов в каждом столбце df без учета пропусков.

Результат запишите в переменную new_ser.

Примечание: импортировать библиотеку Pandas не нужно, она уже импортирована.
"""


import pandas as pd
import numpy as np

df = pd.DataFrame(data={'age': ['Сергей', 'Маша', 'Ксюша', 'Аристарх', 'Соня'],
                        'name': [53, 37, 11, 18, 7],
                        'наличие авто': [True, True, False, True, False]},
                  index=['row_' + str(i) for i in range(5)]
                  )
new_ser = df.agg('count')
print(new_ser)