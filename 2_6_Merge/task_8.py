"""
В программе созданы два DataFrame и записаны в переменные shop_1 и shop_2.

Клиент "client_1" покупал товары в первом магазине.
Сколько бы он сэкономил, если бы купил товары во втором магазине.

Результат запишите в переменную sale.
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

shop_1_cl_1 = shop_1.query('`client` == "client_1"')[['product', 'price']]
shop_2_cl_1 = shop_2[['product', 'price']].drop_duplicates().merge(shop_1_cl_1, on='product', how='right')[['product', 'price_x']]
shop_1_cl_1_cost = shop_1_cl_1['price'].agg('sum')
shop_2_cl_1_cost = shop_2_cl_1['price_x'].agg('sum')
sale = shop_1_cl_1_cost - shop_2_cl_1_cost
print(shop_1_cl_1)
print(shop_2_cl_1)
print(shop_1_cl_1_cost, shop_2_cl_1_cost)
