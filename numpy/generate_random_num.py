import random
import numpy as np

# python自带的random
print(random.random())
print(random.randint(1, 10))

# 生成array类型的[0, 1)之间的随机数：np.random.rand(dim1, dim2, ...)：可以指定维数
dim1, dim2 = 3, 2
print(np.random.rand(dim1, dim2))
# 与之功能相同的：np.random.random([shape])
print(np.random.random([dim1, dim2]))

# 生成指定维数的标准正态分布：np.random.randn(dim1, dim2, ...)
print(np.random.randn(dim1, dim2))

# 生成随机整数：np.random.randint(low, high, size)：[low, high)左闭右开
print(np.random.randint(-5, 5, 10))

# 从已有数据中随机挑选：np.random.choice(data, size, replace=True/False, 权重)
# data：为待挑选的数据；size：挑选出来的个数；replace：是否放回地取；权重：按权重来取
data = np.arange(0, 10, 2)
print(np.random.choice(data))   # 默认取1个
print(np.random.choice(data, 4))    # 取3个
print(np.random.choice(data, 4, replace=False)) # 不放回地取，即取出数不重复
print(np.random.choice(data, 10, p = [0, 0, 0, 0.2, 0.8]))

# 打乱数组：np.random.shuffle(data)，仅用于一维
data_cp = np.copy(data)
np.random.shuffle(data_cp)
print(data_cp)
print(data)

# np.random.permutation()，可以对多维数组在第一个维度上打乱（注意第一个维度，即shape的第一个数字代表的维度
# 对二维数组来说就是打乱行
print('乱序序列（可用作打乱的下标）：', np.random.permutation(10))
data = np.arange(10).reshape([5, 2])
print('第一维（行）的打乱：\n', np.random.permutation(data))

# 按照特定的统计学分布来生成随机数：正态分布：np.random.normal(loc, scale, size)：
# loc：分布的均值，scale：分布的标准差，size：个数，或者shape
# np.random.uniform(low, high, size)：[low, high)
# low：最小值，high：最大值，size：个数，或者shape
print(np.random.normal(1, 0.2, 10))
print(np.random.normal(1, 0.2, [2, 3]))
print(np.random.uniform(0, 5, 10))
print(np.random.uniform(0, 5, [2, 3]))

# 设定随机种子：可以让两次运行产生的随机数一样，以便比较算法优劣
np.random.seed(1)
print(np.random.randint(2, 10, 5))
print(np.random.randint(2, 10, 5))