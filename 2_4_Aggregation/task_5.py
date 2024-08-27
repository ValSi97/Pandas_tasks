"""
В программе создан DataFrame и записан в переменную df.
Подсчитайте сумму в каждой строке df.
Воспользуйтесь методом agg() и функцией Numpy - np.sum().

Результат запишите в переменную new_ser.

Примечание: импортировать библиотеки Pandas и Numpy не нужно, они уже импортированы.
"""

import pandas as pd
import numpy as np

df = pd.DataFrame(data={'age': ['Сергей', 'Маша', 'Ксюша', 'Аристарх', 'Соня'],
                        'name': [53, 37, 11, 18, 7],
                        'наличие авто': [True, True, False, True, False]},
                  index=['row_' + str(i) for i in range(5)]
                  )
new_ser = df.agg(np.sum, axis=1)
print(new_ser)
