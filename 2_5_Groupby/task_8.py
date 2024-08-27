"""
В программе создан DataFrame и записан в переменную df.

Подсчитайте сколько раз каждый клиент покупал "product_3"  и сколько он потратил денег на этот товар.
Данные представьте в виде DF.
Столбец с количеством покупок назовите "product_3", а столбец с суммой потраченных денег "sum_price".
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

#df['product_3'] = df['product'].apply(lambda x: 1 if x == 'product_3' else 0)
#df['price_product_3'] = df['price']*df['product_3']
#new_df = df.groupby('client')[['product_3']].sum()
#new_df = df.groupby('client')[['product_3', 'price_product_3']].agg(product_3=('product_3', 'sum'), sum_price=('price_product_3', 'sum'))
new_df = (df.groupby('client').apply(lambda x: x[x['product'] == "product_3"]
          .agg({'product': 'count', 'price': 'sum'}))
          .rename(columns={'product': 'product_3', 'price': 'sum_price'})
          )
print(new_df)
