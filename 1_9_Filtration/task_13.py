"""
В программе создан DataFrame и записан в переменную df.


Получите список студентов решивших больше 100 задач на курсе "Pandas для анализа данных"

Результат запишите в переменную stud_list.

Примечание: импортировать библиотеку Pandas не нужно, она уже импортирована.
"""
import pandas as pd
import random

df = pd.DataFrame(data=random.choices(range(200), k=100), index=['Имя_'+str(iter) for iter in range(100)], columns=['Решено'])
stud_list = df.query("`Решено` > 100").index.to_list()
print(stud_list)
