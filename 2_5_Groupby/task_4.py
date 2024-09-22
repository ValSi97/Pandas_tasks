"""
В программе создан DataFrame и записан в переменную df.

Подсчитайте для каждого клиента какие товары и сколько раз он их покупал.
Столбец с количеством покупок назовите "count".
Результат запишите в переменную new_df.
"""

import pandas as pd
import numpy as np

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

new_df = df.groupby(['client', 'product'], as_index=False).agg(count=('product', 'count'))
print(new_df)
