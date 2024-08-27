"""
В программе создан DataFrame и записан в переменную df.

Получите только те строки в которых стаж работы сотрудников меньше или равен 4.
При фильтрации используйте метод query().

Результат запишите в переменную new_df.

Примечание: импортировать библиотеку Pandas не нужно, она уже импортирована.
"""
import pandas as pd

df = pd.DataFrame(data={
    'год рождения': range(88, 93),
    'стаж работы': [3.25, 4.50, 5.75, 6.25, 7.50],
    'зарплата': range(60000, 110000, 10000)
})
new_df = df.query('`стаж работы` <= 4')
print(new_df)