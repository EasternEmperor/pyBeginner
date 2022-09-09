import numpy as np

a = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

# 条件
condition = a > 7
print(condition)
print(a[condition])     # 挑选出大于7的元素组成一维数组打印
# numpy.where(condition, x, y)：满足条件的输出x，不满足的输出y
b = -a - 1
print(b)
print(np.where(condition, a, b))