import numpy as np

a = np.array([
    [1, 2],
    [3, 4]
])
b = np.array([
    [5, 6],
    [7, 8]
])

# 水平合并
c = np.hstack([a, b])
print(c)        # shape (2, 4)
d = np.vstack([a, b])
print(d)        # shape (4, 2)

# 观察形态
# 维数
print(c.ndim, d.ndim)
# 元素个数
print(c.size)
# 行列数
print(c.shape[0])   # 行数2
print(c.shape[1])   # 列数4
print(c.shape)      # (2, 4)