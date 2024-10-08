"""
В программе создан DataFrame и записан в переменную df.

Получите только те строки в которых сотрудники старше 91 года рождения и зарплата равна 80000. При фильтрации используйте метод query().

Результат запишите в переменную new_df.

Примечание: импортировать библиотеку Pandas не нужно, она уже импортирована.
"""
import pandas as pd

df = pd.DataFrame(data={
    'год рождения': range(88, 93),
    'стаж работы': [3.25, 4.50, 5.75, 6.25, 7.50],
    'зарплата': range(60000, 110000, 10000)
})
new_df = df.query('`год рождения` < 91 and `зарплата` == 80000')
print(new_df)
