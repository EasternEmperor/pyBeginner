import numpy as np

# 创建全部为0/1的数组
zeros = np.zeros([2, 3])
ones = np.ones([3, 2])
print('zeros:\n', zeros)
print('\nones:\n', ones)

# 创建指定数字的统一数组：np.full([shape], num)
nines = np.full([2, 3], 9)
print('\nnines:\n', nines)

# 创建维度和数据类型与给定数组一致的数组：np.xxx_like([])
# np.ones_like(), np.zeros_like(), np.full_like( , )
data = np.array([
[1,2,3],
[4,5,6]
], dtype=np.int64)

ones = np.ones(data.shape, dtype=data.dtype)
ones_like = np.ones_like(data)

nines = np.full(data.shape, 9, dtype=data.dtype)
nines_like = np.full_like(data, 9)

print('\ndata:', data.shape, data.dtype)
print('ones:', ones.shape, data.dtype)
print('ones_like:', ones_like.shape, ones_like.dtype)
print('nines:', nines.shape, nines.dtype)
print('nines_like:', nines_like.shape, nines_like.dtype)

# 创建规律数组：np.arange()，类似range()
print('\npython range: ', list(range(5)))
print('numpy arange: ', np.arange(5))
# 也可像range()一样创建有限制的
print('python range: ', list(range(5, 15, 2)))
print('numpy arange: ', np.arange(5, 15, 2))

# linspace(start, end, num, endpoint = True/False)：从start到end取间隔一致的num个点，endpoint代表end处取不取
print('\nlinspace: ', np.linspace(-1, 1, 5))
print('linspace:(end处不取): ', np.linspace(-1, 1, 5, endpoint=False))

# 其他生成特殊数据的方式：np.identity(n, dtype=)：生成主对角线为1，其余元素为0的单位矩阵
print('\nnp.identity: \n', np.identity(2, dtype=np.int64))

# np.eye(N, M, k, dtype)：生成shape为[N, M]的二维数组，k设定为1的对角线，其中主对角线k为0，负数为低对角，正数为高对角
print('\nnp.eye:\n', np.eye(3, 2, 1))

# np.empty([shape], dtype=)：初始化shape状的数组，其中的数值是乱的
# 可用于快速生成一个同样shape的数组，来根据它赋值新的值
print('\nnp.empty: \n', np.empty([3, 2], dtype=np.int64))
print('\nnp.empty_like: \n', np.empty_like(data))