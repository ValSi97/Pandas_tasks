"""
В программе создан DataFrame и записан в переменную df.

Получите элементы, которые находятся на пересечении столбца с индексом 1 и строк с индексами 2 и 4.

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
new_ser = df.iloc[[2, 4], 1]
print(type(new_ser))
print(new_ser)
