import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 绘制分布图：df.plot.hist(x, y, bins)
# bins：控制每个柱子的间隔
df = pd.DataFrame({'a': np.random.randn(1000)})
print(df)
df.plot.hist()
plt.show()
# 多个分布图
df = pd.DataFrame({
    'a': np.random.rand(50),
    'b': np.random.random(50),
    'c': np.random.normal(1, 0.3, 50)
})
print(df)
df.plot.hist(alpha = .5, bins = 50)
plt.show()