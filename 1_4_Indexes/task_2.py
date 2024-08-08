"""
Создайте объект класса Index с 4-мя элементами и именем "my_index".

Результат запишите в переменную ind.
"""

import pandas as pd

ind = pd.Index(['a', 'b', 'c', 'd'], name='my_index')

print(ind)
