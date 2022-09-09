import numpy as np
import random

# 矩阵点积
a = np.array([
[1, 2],
[3, 4]
])
b = np.array([
[5, 6],
[7, 8]
])

print(a.dot(b))
print(np.dot(a, b))

# 最大最小值
a = np.array([150, 166, 183, 170])
print(np.max(a))
print(a.min())

# 加和
print(a.sum())

# 累乘
print(a.prod())

# 非零总数
b = np.array([0, 1, 2])
print(np.count_nonzero(b))      # 非0总数

# 标准差
print(a.std())

# 取最高/低值的下标
a = np.array([150, 166, 183, 170])
name = ["小米", "OPPO", "Huawei", "诺基亚"]
min_idx = np.argmax(a)
max_idx = np.argmin(a)
print(a)
print("{} 最高".format(name[max_idx]))
print("{} 最低".format(name[min_idx]))

# 向上/下取整
a = np.array([150.1, 242.32, 132.89, 121.3])
print('ceil: ', np.ceil(a))
print('floor: ', np.floor((a)))

# 指定上下界限的截取
print('clip: ', a.clip(160, 180))
