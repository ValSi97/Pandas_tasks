"""
В программе создан DataFrame и записан в переменную df.

Подсчитайте какое количество разных товаров купил каждый клиент.
Результат запишите в переменную new_ser
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

new_ser = df.groupby('client')['product'].nunique()
print(new_ser)
