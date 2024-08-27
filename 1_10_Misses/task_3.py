"""
В программе создан DataFrame и записан в переменную df. Удалите все столбцы имеющие пропуски.

Результат запишите в переменную new_df.

Примечание: импортировать библиотеку Pandas не нужно, она уже импортирована.
"""

import pandas as pd
import numpy as np
df = pd.DataFrame(data={
    'год рождения': range(88, 93),
    'стаж работы': [np.nan, 4.50, 5.75, np.nan, 7.50],
    'зарплата': range(60000, 110000, 10000)
})
new_df = df.dropna(axis=1)
print(new_df)