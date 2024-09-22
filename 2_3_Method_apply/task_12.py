"""
В программе создан DataFrame и записан в переменную df.


В DF содержится 'product' - имя товара, 'product_price' - цена товара,
'count' - количество товаров в корзине, 'buy' - произведена покупка или нет.
Добавьте еще один столбец 'price',
который содержит сумму всей покупки, если она совершена, и np.nan, если покупка не совершена.

Реализуйте функционал, при котором можно выбирать товар для которого будет подсчитываться значение в столбце 'price'.
Если товар не указывать , значения в столбце 'price' будет посчитано как указано выше.

Пример:

def func(...):
    ...
    ...
    ...

df['price'] = df.apply(func, ..., prod='товар_1')


В переменную prod запишите df дополнительно не указывая товар.
В переменную prod_3 запишите df дополнительно указав 'товар_3'.

Порядок столбцов в DF для проверки может отличатся от DF на картинке.
"""

import pandas as pd
import numpy as np
import random as rd


def mapper(dataframe, product_name=''):
    if dataframe['buy']:
        if product_name != '':
            if dataframe['product'] == product_name:
                return dataframe['product_price'] * dataframe['count']
            else:
                return np.nan
        else:
            return dataframe['product_price'] * dataframe['count']
    else:
        return np.nan


df = pd.DataFrame(data={'product': ['товар_' + str(rd.choice(range(1, 10))) for i in range(100)],
                        'product_price': [(rd.choice(range(1000, 10000, 1000))) for i in range(100)],
                        'count': [rd.choice(range(1, 10)) for i in range(100)],
                        'buy': [rd.choice([True, False]) for i in range(100)]
                        }
                  )
prod = df.copy()
prod_3 = df.copy()
df['price'] = df.apply(mapper, product_name='товар_1', axis=1)
prod['price'] = prod_3.apply(mapper, axis=1)
prod_3['price'] = prod_3.apply(mapper, product_name='товар_3', axis=1)
print(prod_3)
print(prod)

