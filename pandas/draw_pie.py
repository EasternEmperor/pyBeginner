import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 饼图：df.plot.pie(y, subplots, figsize, legend)
# y：饼图展示的数据列；subplots(bool)：是否要子图；figsize：画布大小；lengend(bool)：图例
df = pd.DataFrame({
    'boss': np.random.rand(4)},
    index = ['meeting', 'supervising', 'coding', 'pua']
)
df.plot.pie(y = 'boss')
plt.show()
df = pd.DataFrame(
    {
        'bigboss': np.random.rand(4),
        'smallboss': np.random.rand(4)
    },
    index = ['meeting', 'supervising', 'coding', 'pua']
)
df.plot.pie(subplots=True, figsize = (9, 9), legend = False)

plt.show()