"""
В программе созданы серия  и DF и записаны в переменные ser и df соответственно.
Ко всем столбцам DF прибавьте значения из серии.

Воспользуйтесь специальным методом и аргументом axis.

Результат запишите в переменную new_df.

Примечание: импортировать библиотеку Pandas не нужно, она уже импортирована.
"""

import pandas as pd

ser = pd.Series(data=[1, 2, 3, 4, 5])
df = pd.DataFrame(data={
    'age': [19, 20, 23, 24, 25],
    'стаж работы': range(3, 8),
    'зарплата': range(60000, 110000, 10000)
})
new_df = df.reindex(columns=['стаж работы', 'age', 'зарплата']).add(ser.to_list(), axis=0)
print(new_df)
