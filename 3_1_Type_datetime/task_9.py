"""
В программе создан DataFrame, содержащий данные о доходах, и записан в переменную df.

Получите данные о доходах в каждом месяце.

Результат запишите в переменную new_df.

Подсказка: добавьте дополнительный столбец, по которому можно будет сгруппировать данные.
"""
import pandas as pd
import numpy as np
import random as rd

df = pd.DataFrame(
    {
        'date': [rd.choice(pd.date_range('2016-03-14', '2018-03-14')) for i in range(100)],
        'salary': [rd.choice(range(100, 200)) for i in range(100)],
    }
)
new_df = df.copy()
new_df['month'] = new_df['date'].dt.month
new_df = new_df.groupby('month', as_index=False).agg({'salary': 'sum'})
print(new_df)
