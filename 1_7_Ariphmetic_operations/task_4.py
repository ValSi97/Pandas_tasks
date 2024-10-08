"""
В программе создан DF и записан в переменную df.

В столбце "стаж работы" вместо количества месяцев стоит количество лет. В столбце "зарплата" указаны тысячи рублей, а не рубли (пример: вместо 60000 рублей стоит 60 т.р.)

Поменяйте значения так, чтобы:

в столбце "стаж работы" стояли месяцы, а не года,
в столбце "зарплата" стояли числа в тысячу раз больше.
Решите упражнение не меняя исходный DF. Результат запишите в переменную new_df.

Примечание: импортировать библиотеку Pandas не нужно, она уже импортирована.
"""
import pandas as pd

df = pd.DataFrame(data={'стаж работы': [3.25, 4.50, 5.75, 6.25, 7.50],
                        'зарплата': [60, 70, 80, 90, 100]})
new_df = df.copy()
new_df['стаж работы'] *= 12
new_df['зарплата'] *= 1000
print(new_df)
