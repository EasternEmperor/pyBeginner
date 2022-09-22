import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 柱状图：df.plot.bar(x, y, stacked)
# x、y：要绘制的df中的列（不填则默认df中所有列）；stacked(bool)：是否将柱形堆叠
df = pd.DataFrame(np.random.rand(4, 3), columns=['a', 'b', 'c'])
df.plot.bar()
# 堆叠柱状图
df.plot.bar(stacked = True)
plt.show()
# 横着的柱状图：df.plot.barh(x, y, stacked)
df.plot.barh()
df.plot.barh(stacked = True)
plt.show()