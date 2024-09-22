"""
В программе создан DataFrame и записан в переменную df.

Поменяйте тип данных в столбце "date" на "datetime".
Получите только те строки, которые в столбце "date" содержат конец месяца.

Результат запишите в переменную new_df.

Подсказка: воспользуйтесь свойством is_month_end.
"""
import pandas as pd
import numpy as np
import random as rd

df = pd.DataFrame(
    {
        'id': [i for i in range(10000, 10020)],
        'date': [rd.choice(pd.date_range('2016-03-14', '2018-03-14')) for i in range(20)]
    }
)
new_df = df.copy()
new_df['date'] = new_df['date'].astype('datetime64[ns]')
new_df = new_df[new_df['date'].dt.is_month_end]
print(new_df)
