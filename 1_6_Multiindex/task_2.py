"""
Создайте мультииндекс на основе данных списков: ['a', 's', 'd', 'f'] и [1, 2, 3, 4]. Используйте метод from_arrays().

Результат запишите в переменную ind.
"""

import pandas as pd

ind = pd.MultiIndex.from_arrays([['a', 's', 'd', 'f'], [1, 2, 3, 4]])
print(ind)
