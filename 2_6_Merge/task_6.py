"""
В программе созданы два DataFrame и записаны в переменные shop_1 и shop_2.

Получите DF, в котором цене на товар в первом магазине сопоставлена цена из второго.
"""
import pandas as pd
import numpy as np

N_client = 10
N_product = 15

client_1 = {i: f'client_{i}' for i in range(N_client)}
client_2 = {i: f'client_{i}' for i in range(3, N_client + 3)}

data_product = {i: f'product_{i}' for i in range(N_product)}
price_1 = {i: (i + 1) * 1000 for i in range(15)}
price_2 = {i: (i + 1) * 900 for i in range(15)}

client_list_1 = np.random.randint(0, N_client, 100)
client_list_2 = np.random.randint(3, N_client + 3, 100)

product_list = np.random.randint(0, N_product, 100)

shop_1 = pd.DataFrame({'client': client_list_1,
                       'product': product_list,
                       'price': product_list}).replace({'client': client_1, 'product': data_product, 'price': price_1})
shop_2 = pd.DataFrame({'client': client_list_2,
                       'product': product_list,
                       'price': product_list}).replace({'client': client_2, 'product': data_product, 'price': price_2})
product = pd.DataFrame({'product': data_product.values(),
                        'color': np.random.choice(['black', 'red', 'green', 'white', 'blue'], 15),
                        'weight': np.random.randint(10, 20, 15) * 10})

#shop_2 = shop_2[['product', 'price']].drop_duplicates()
new_df = (shop_1[['product', 'price']].drop_duplicates().merge(shop_2[['product', 'price']]
                                                               .drop_duplicates(), how='left', on='product',
                                                               suffixes=['_shop_1', '_shop_2'])
          .astype({'price_shop_2': float}).astype({'price_shop_1': float}))

#new_df = new_df.reindex(columns=['client', 'product', 'price_y', 'price_x']).astype({'price_y': float})
#new_df.rename(inplace=True, columns={'price_y': 'price_x', 'price_x': 'price_y'})
print(new_df)
