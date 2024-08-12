"""
В программе создан DataFrame и записан в переменную df.

Поменяйте мультииндекс столбцов на индекс с элементами ["age_max", "age_min", "age_mean", "last_name", "first_name"]

Примечание: импортировать библиотеку Pandas не нужно, она уже импортирована.


"""

import pandas as pd

tuples = [('age', 'max'), ('age', 'min'), ('age', 'mean'), ('name', 'last_name'), ('name', 'first_name')]
lst = [[i for j in range(5)] for i in range(6, 0, -1)]
ind = pd.MultiIndex.from_tuples(tuples)
df = pd.DataFrame(
     data=lst,
     columns=ind
)
ind = ["age_max", "age_min", "age_mean", "last_name", "first_name"]
df.columns = ind

print(df)
# df.columns = df.columns.droplevel(0)
# print(df)