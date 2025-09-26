
import pandas as pd
import matplotlib.pyplot as plt
import random

df1=pd.read_csv('Oranges_Grapefruit_100.csv')

colors = {'orange':'orange', 'grapefruit':'blue'}
plt.scatter(df1['diameter'], df1['weight'], c=[colors[name] for name in df1['name']])
# 将每种颜色对应的种类，以标签的形式显示出来
for name, color in colors.items():
    plt.scatter([], [], c=color, label=name)
plt.legend()

plt.show()
