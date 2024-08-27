"""
Строку "1961-04-12" представьте в виде объекта Timestemp.

Результат запишите в переменную date.
"""
import pandas as pd

str_date = "1961-04-12"
date = pd.to_datetime(str_date)
print(date)
