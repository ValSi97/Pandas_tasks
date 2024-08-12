"""
В программе создан DataFrame и записан в переменную df. Выполните следующие действия с мультииндексом строк:

получите количество уровней, результат запишите в переменную nlev,
получите кортеж с количеством элементов на каждом уровне, результат запишите в переменную lev_sh,
получите имена уровней, результат запишите в переменную name_lev,
получите объект, содержащий элементы мультииндекса, результат запишите в переменную lev,
Примечание: импортировать библиотеку Pandas не нужно, она уже импортирована.
"""

import pandas as pd

models = ['юпитер', 'восход']
colors = ['черный', 'оранжевый', 'красный']
ind = pd.MultiIndex.from_product([models, colors], names=['модель', 'цвет'])

df = pd.DataFrame(
    data={'date': [1, 2, 3, 4, 5, 6]},
    index=ind
)
nlev = df.index.nlevels
lev_sh = df.index.levshape
name_lev = df.index.names
lev = df.index.levels
print(nlev, lev_sh, name_lev, lev)