"""
В программе созданы две серии и записаны в переменные ser_1 и ser_2.

Series ser_1 содержит количество нерешенных упражнений каждым студентом курса "Pandas для анализа данных",
а ser_2 содержит количество решенных упражнений каждым студентом курса.
Получите Series/маску показывающую у каких студентов решенных задач меньше, чем не решенных.

Результат запишите в переменную mask.

Примечание: импортировать библиотеку Pandas не нужно, она уже импортирована.
"""
import pandas as pd
import random

ser_1 = pd.Series(data=random.choices(range(101), k=100), index=['Имя_'+str(iter) for iter in range(100)])
ser_2 = pd.Series(data=random.choices(range(101), k=100), index=['Имя_'+str(iter) for iter in range(100)])

mask = ser_2.lt(ser_1)
print(mask)