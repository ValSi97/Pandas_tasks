"""
В программе создан DataFrame и записан в переменную df.
В столбце "зарплата" нужно подсчитать сумму и среднее значение,
а в столбце "стаж работы" только среднее значение. Используйте функции Numpy np.sum, np.mean.

Результат запишите в переменную new_df.

Примечание: импортировать библиотеки Pandas и Numpy не нужно, они уже импортированы.
"""


import pandas as pd
import numpy as np

df = pd.DataFrame(data={'год рождения': [i for i in range(88, 93)],
                        'стаж работы': [3.25, 4.50, 5.75, 6.25, 7.50],
                        'зарплата': [60, 70, np.nan, np.nan, 100]},
                  index=[i for i in range(3, 8)]
                  )
new_df = df.agg({'зарплата': [np.sum, np.mean],
                 'стаж работы': [np.mean]})
print(new_df)