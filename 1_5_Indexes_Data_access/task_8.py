"""
В программе создан DataFrame и записан в переменную df. Столбец с именем "name" присвойте переменной df_1.
В переменной df_1 должен быть  DataFrame, а не Series.

Примечание: импортировать библиотеку Pandas не нужно, она уже импортирована.
"""
import pandas as pd

df = pd.DataFrame(
    data={'data': [1, 2, 3], 'age': [4, 5, 6], 'name': [7, 8, 9]}
)
df_1 = df[['name']]
print(type(df_1), df_1)
