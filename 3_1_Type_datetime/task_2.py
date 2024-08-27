"""
В программе создана серия со строковыми значениями и записана в переменную ser.

Представьте эту серию в виде серии с типом данных "datetime".

Результат запишите в переменную new_ser.
"""
import pandas as pd
import numpy as np
import random as rd

ser = pd.Series([rd.choice(pd.date_range('2016-03-14', '2018-03-14')) for i in range(100)])
new_ser = ser.astype('datetime64[ns]')
print(ser)
