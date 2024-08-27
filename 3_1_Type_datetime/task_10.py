"""
Создайте объект DatetimeIndex, который содержит 20 элементов, начинающихся с "2023-05-05" и частотой в один день.

Результат запишите в переменную date_range.
"""
import pandas as pd
date_range = pd.date_range("2023-05-05", periods=20)
print(date_range)
