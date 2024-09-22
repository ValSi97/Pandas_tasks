"""
В программе создан DataFrame и записан в переменную df.

В столбце 'buy' замените 'куплено' на True, а 'не куплено' на False.

Примечание: импортировать библиотеку Pandas не нужно, она уже импортирована.
"""

import pandas as pd
import numpy as np
import random as rd

df = pd.DataFrame(data={'product': ['Товар_' + str(rd.choice(range(1, 10))) for i in range(100)],
                        'product_price': [rd.choice(range(1000, 10000, 1000)) for i in range(100)],
                        'count': [rd.choice(range(1, 10)) for i in range(100)],
                        'buy': [rd.choice(['куплено', 'не куплено']) for i in range(100)]
                        }
                  )

df['product_price'] = df['product_price'].map(lambda x: str(x) + ' руб', na_action='ignore')
print(df)