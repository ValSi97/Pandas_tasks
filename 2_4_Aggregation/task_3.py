"""
Упражнение 3.

В программе создан DataFrame и записан в переменную df. В столбце "age" подсчитайте средний возраст.

Результат запишите в переменную mean_age.

Примечание: импортировать библиотеку Pandas не нужно, она уже импортирована.
"""

import pandas as pd
import numpy as np

df = pd.DataFrame(data={'name': ['Сергей', 'Маша', 'Ксюша', 'Аристарх', 'Соня'],
                        'age': [53, 37, 11, 18, 7],
                        'наличие авто': [True, True, False, True, False]},
                  index=['row_' + str(i) for i in range(5)]
                  )
mean_age = df['age'].agg('mean')
print(mean_age)
