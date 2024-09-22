"""
В программе создан файл с данными - "stud.csv".

В столбце 'name' указано имя студента, столбцы с 1 до 50 - это номера задач.
Если значение в DF равно 1 - это значит, есть верное решение задачи, если 0,
есть только неверное решения, если Nan, то нет отправленных решений.

Импортируйте файл и подсчитайте сколько не правильных решений у каждого студента?

Результат представьте в виде Series, индексы которой это имена студентов, и запишите в переменную new_ser.
"""
import pandas as pd
import numpy as np


def summ(dataframe):
    res = 0
    for elem in dataframe:
        if elem == 0:
            res += 1
    return res


df = pd.read_csv('stud.csv')
new_ser = df.agg(summ, axis=1)
new_ser.index = df['name']
print(new_ser)
