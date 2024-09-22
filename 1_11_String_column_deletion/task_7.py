"""
В программе создан DataFrame и записан в переменную df.

Измените тип данных в столбцах, чтобы уменьшить объем занимаемой памяти и увеличить скорость
работы с некоторыми столбцами.
Столбец "col_3" содержит всего 10 уникальных значений.

Результат запишите в переменную new_df.

Примечание: импортировать библиотеки Pandas и Numpy не нужно, они уже импортированы.
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
new_df = df.astype({'col_1': np.int16,
                    'col_2': np.float16,
                    'col_3': 'category'})
print(new_df.dtypes)
print(new_df)