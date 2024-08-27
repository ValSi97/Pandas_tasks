"""
В программе создан DataFrame и записан в переменную df.

Значение элемента, который находится на пересечении столбца 'name' и строки 'row_2', поменяйте на значение 'new_name'.

Примечание: импортировать библиотеку Pandas не нужно, она уже импортирована.
"""

import pandas as pd
import numpy as np

df = pd.DataFrame(data={'age': ['Сергей', 'Маша', 'Ксюша', 'Аристарх', 'Соня'],
                        'name': [53, 37, 11, 18, 7],
                        'наличие авто': [True, True, False, True, False]},
                  index=['row_' + str(i) for i in range(5)]
                  )
df.at["row_2", 'name'] = 'new_name'
print(df)