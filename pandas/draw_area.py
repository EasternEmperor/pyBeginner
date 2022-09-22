import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 绘制面积图，通过面积展示各部分数值变化：df.plot.area()
df = pd.DataFrame(
    np.random.rand(10, 4),
    columns=['a', 'b', 'c', 'd']
)
print(df)
df.plot.area()
plt.show()
# 不重叠
df.plot.area(stacked = False)
plt.show()