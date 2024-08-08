"""
В программе создан DataFrame и записан в переменную df.
С помощью метода rename() получите новый DataFrame
с измененными метками столбцов col_2 и col_3 на new_col_2 и new_col_3 соответственно.

Результат запишите в переменную new_df.

Примечание: импортировать библиотеку Pandas не нужно, она уже импортирована.
"""

import pandas as pd

df = pd.DataFrame(
    data={'col_1': [1, 2, 3], 'col_2': [4, 5, 6], 'col_3': [7, 8, 9]}
)
new_df = df.rename(columns={'col_2': 'new_col_2', 'col_3': 'new_col_3'})

print(new_df)
