"""
В программе создан DataFrame и записан в переменную df.

В DF содержится 'product' - имя товара,
'product_price' - цена товара,
'count' - количество товаров в корзине,
'buy' - произведена покупка или нет.
Добавьте еще один столбец 'price',
который содержит сумму всей покупки, если она совершена, и np.nan, если покупка не совершена.

Порядок столбцов в DF для проверки может отличатся от DF на картинке.
"""

import pandas as pd
import numpy as np
import random as rd


def mapper(dataframe):
    if dataframe['buy']:
        return dataframe['product_price'] * dataframe['count']
    else:
        return np.nan


df = pd.DataFrame(data={'product': ['товар_' + str(rd.choice(range(1, 10))) for i in range(100)],
                        'product_price': [(rd.choice(range(1000, 10000, 1000))) for i in range(100)],
                        'count': [rd.choice(range(1, 10)) for i in range(100)],
                        'buy': [rd.choice([True, False]) for i in range(100)]
                        }
                  )
df['price'] = df.apply(mapper, axis=1)
print(df)
