"""
В программе создан DataFrame и записан в переменную df. Столбец с именем "name" присвойте переменной series.
В переменной series должна быть Series, а не DataFrame.

Примечание: импортировать библиотеку Pandas не нужно, она уже импортирована.
"""
import pandas as pd

df = pd.DataFrame(
    data={'data': [1, 2, 3], 'age': [4, 5, 6], 'name': [7, 8, 9]}
)
series = df['name']
print(type(series), series)
