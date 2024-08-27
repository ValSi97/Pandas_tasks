"""
В программе создан DataFrame и записан в переменную df.

Измените тип данных в столбце 'col_2' на 'int'.

Результат запишите в переменную new_df.

Примечание: импортировать библиотеку Pandas не нужно, она уже импортирована.
"""

import pandas as pd
import numpy as np
import random
import datetime

datetime.datetime
letters = 'abcdefghijklmnopqrstuvwxyz'
df = pd.DataFrame(columns=(['col_' + str(i) for i in range(1, 5)]),
                  data=[[i,
                         float(i),
                         random.choice(letters),
                         (datetime.datetime.strptime('01-01-2000', "%m-%d-%Y").date() +
                          datetime.timedelta(days=i)).strftime("%m-%d-%Y")
                         ]
                        #*pd.date_range(start='01-01-2000', periods=1000).strftime("%m-%d-%y")
                        for i in range(1000)
                        ],
                  index=[i for i in range(1000)]
                  )
new_df = df.astype({'col_2': int})
print(new_df.dtypes)
print(new_df)
