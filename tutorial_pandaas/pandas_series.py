import pandas as pd

colors = pd.Series(
    ['red', 'green', 'blue', 'violet', 'yellow', 'brown'],
    index=[1, 2, 3, 5, 8, 13]
)
colors1 = ['red', 'green', 'blue', 'violet', 'yellow']

print(colors.loc[1:9])
'''
loc - ищет индекс метки
iloc - ищет поцизионный индекс
'''
print(colors.iloc[-2])
