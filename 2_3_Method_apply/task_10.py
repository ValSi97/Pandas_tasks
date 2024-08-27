"""
В программе создан DataFrame и записан в переменную df.


В DF содержится 'product' - имя товара, 'product_price' - цена товара,
'count' - количество товаров в корзине, 'buy' - произведена покупка или нет.
Если цена товара меньше 1500, то заменить ее на строку 'Покупать', если от 1500 до 3000 включительно,
то заменить на строку 'Есть над чем подумать', а если больше 3000, то заменить на строку ''.


Порядок столбцов в DF для проверки может отличатся от DF на картинке.
"""

import pandas as pd
import numpy as np
import random as rd


def mapper(dataframe):
    if dataframe['product_price'] < 1500:
        return 'Покупать'
    elif dataframe['product_price'] > 3000:
        return 'И думать нечего, не брать'
    else:
        return 'Есть над чем подумать'


df = pd.DataFrame(data={'product': ['товар_' + str(rd.choice(range(1, 10))) for i in range(100)],
                        'product_price': [(rd.choice(range(1000, 10000, 1000))) for i in range(100)],
                        'count': [rd.choice(range(1, 10)) for i in range(100)],
                        'buy': [rd.choice([True, False]) for i in range(100)]
                        }
                  )
df['product_price'] = df.apply(mapper, axis=1)
print(df)
