import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 折线图：df.plot
n = 20
x = np.linspace(0, 2, n)
y = x + 0.4 + np.random.normal(0, 1, n)
df = pd.DataFrame({
    'x': x,
    'y': y
})
print(df)
df.plot(x = 'x', y = 'y', alpha = .5, c = 'green')
plt.show()
# 多条线的折线图
y1 = y
y2 = -x - 0.1 - np.random.normal(-1, 1, n)
df = pd.DataFrame({
    'x': x,
    'y1': y1,
    'y2': y2
})
print(df)
df.plot(x = 'x', y = ['y1', 'y2'], alpha = .5)
plt.show()
