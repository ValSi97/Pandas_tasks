"""
В программе созданы DF и серия и записаны в переменные df и ser соответственно.
Элементы каждого столбца DF сравните с элементами серии.
Воспользуйтесь специальным методом для сравнения, операция сравнения >=(больше или равно).

Результат запишите в переменную new_df.

Примечание: импортировать библиотеку Pandas не нужно, она уже импортирована.
"""
import pandas as pd

ser = pd.Series(data=[5, 22.2, 80000, 15, 2])
df = pd.DataFrame(data={
    'age': [19, 20, 23, 24, 25],
    'стаж работы': range(3, 8),
    'зарплата': range(60000, 110000, 10000)
})

new_df = df.ge(other=ser, axis=0)

print(new_df)