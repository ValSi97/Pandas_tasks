"""
В программе создан DataFrame и записан в переменную df.

Подсчитайте сколько раз каждый клиент покупал "product_2" .
Данные представьте в виде DF.
Столбец с количеством покупок назовите "product_2". Результат запишите в переменную new_df.
"""

import pandas as pd
import numpy as np


def func(series):
    return series.count('product_2')


N_client = 10
N_product = 15

client = {i: f'client_{i}' for i in range(N_client)}
product = {i: f'product_{i}' for i in range(N_product )}
price = {i: (i+1)*1000 for i in range(N_product)}

client_list = np.random.randint(0, N_client, 100)
product_list = np.random.randint(0, N_product , 100)

df = pd.DataFrame({'client': client_list,
                   'product': product_list,
                   'price': product_list}).replace({'client': client, 'product': product, 'price': price})

new_df = df.groupby(['client'])['product'].apply(list).apply(func)
new_df = pd.DataFrame({'product_2': new_df.values}, index=new_df.index)
print(new_df)
