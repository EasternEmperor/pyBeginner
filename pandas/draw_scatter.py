import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 散点图：df.plot.scatter(x, y, c, s, alpha, cmap)
# x, y：绘图x轴和y轴；c：指定点的颜色，也可以传入一个column name（df中其余列）来指定点的颜色，也可以自制列（如下）
# s：点的大小；alpha：点的透明度；cmap：colormap，配合c指定点颜色
n = 1024
df = pd.DataFrame({
    'x': np.random.normal(0, 1, n),
    'y': np.random.normal(0, 1, n)
})      # 创建两列：x和y
print(df)
color = np.arctan2(df['x'], df['y'])
df.plot.scatter(x = 'x', y = 'y', c = color, s = 60, alpha = .5, cmap = 'rainbow')
plt.show()