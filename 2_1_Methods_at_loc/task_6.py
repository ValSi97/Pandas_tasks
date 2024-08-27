"""
В программе создан DataFrame и записан в переменную df.

Получите элемент, который находится на пересечении столбца 'age' и строки 'row_3'.

Результат запишите в переменную value.

Примечание: импортировать библиотеку Pandas не нужно, она уже импортирована.
"""
import pandas as pd
import numpy as np

df = pd.DataFrame(data={'age': ['Сергей', 'Маша', 'Ксюша', 'Аристарх', 'Соня'],
                        'name': [53, 37, 11, 18, 7],
                        'наличие авто': [True, True, False, True, False]},
                  index=['row_' + str(i) for i in range(5)]
                  )
value = df.at["row_3", 'age']
print(value)
