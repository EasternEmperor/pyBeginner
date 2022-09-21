import pandas as pd
import numpy as np

data = np.array([
    [1.39, 1.77, None],
    [0.34, 1.91, -0.05],
    [0.34, 1.47, 1.22],
    [None, 0.27, -0.61]
])
df = pd.DataFrame(data, index=["r0", "r1", "r2", "r3"], columns=["c0", "c1", "c2"])

# 描述dataframe：以列统计，剔除NaN的数据类型
# count：数据个数（剔除None/NaN类型），unique：不重复数据个数
# top：出现最多次的数据
# freq：出现频率最高的数出现次数
print(df.describe())
# 纯数据df会展示更多信息
df1 = pd.DataFrame(np.random.random([4, 3]), columns = ['c0', 'c1', 'c2'])
print(df1)
print(df1.describe())

# 平均值
print(df.mean())
print(df.mean(axis = 0))    # 操作第0个维度，即shape的第一位。将其压缩成1维
print(df.mean(axis = 1, skipna = True)) # 操作第1个维度，且跳过na值（即计个数时不算入na项）

# 中位数
print(df.median())
print(df.median(axis = 1))

# (4,3)dataframe定义
df = pd.DataFrame(np.arange(1, 13).reshape(4, 3), index = ['r1', 'r2', 'r3', 'r4'],
                                                  columns=['c1', 'c2', 'c3'])
print(df)

# 其他函数：
# sum()
print('\neach col sum:\n', df.sum(axis = 0))     # 列和
print('\neach row sum:\n', df.sum(axis = 1))     # 行和
# prod()：累乘
print('\neach col prod:\n', df.prod(axis = 0))
print('\neach row prod:\n', df.prod(axis = 1))

# 最大最小
# 注意：直接使用min和max求的是一个维度上的，不是全局
# 和numpy不同：numpy.max()是求全局最大，但是可以通过axis参数指定求某个维度上所有的最大值（0则是压缩行，即求每列的最大值）
print('\nmax:\n', df.max())
print('\nmin:\n', df.min())
# 求全局最大最小值：
# 1、 求两次；2、变为numpy再求
print(df.max().max())
print(df.to_numpy().max())

# 处理空值
df = pd.DataFrame([[1, 2, 3, 0],
                   [3, 4, None, 1],
                   [None, None, None, None],
                   [None, 3, None, 4]],
                  columns=list("ABCD"))
print(df)

# 首先查找空值：isnull()，notnull()
print(df.isnull())
print(df.notnull())

# 清理空值：dropna()，可通过axis参数控制操作的维度
print(df.dropna())          # 操作行，即显示各列未被删除的行
print(df.dropna(axis=1))    # 操作列

# 参数how，默认为'any'，表示只要该操作维度上有na元素，就删除；可设置为'all'，可保留不全为na的维度
print(df.dropna(how='all'))     # 可以看到仅删除了第3行

# 填充na：fillna()，可以指定填充值
print(df.fillna(123))       # 用123填充所有na
# 对不同列进行差异化填充：指定一个字典，每个列对应该列的na填充值
col_fill = {}
keys = ''.join(df.columns.to_list())
for i in range(len(df.columns)):
    col_fill[keys[i]] = i
print(df.fillna(value=col_fill))
# 用其他的df来填充该df：对应位置填充
df_fill = pd.DataFrame(np.arange(5, 21).reshape(len(df.index), len(df.columns)),
                       columns=df.columns.to_list())
print('\nfill num:\n', df_fill[df.isnull()])        # 可以将一个同shape的df mask放入取值
print('\ndf filled:\n', df.fillna(value=df_fill))

# pd取出最大/最小值的索引：idxmax(), idxmin()
# 参数：skipna:bool，表示是否跳过na值；axis：要操作的维度
df = pd.DataFrame([[1, 2, 3, 0],
                   [3, 4, None, 1],
                   [3, 5, 2, 1],
                   [3, 2, 2, 3]],
                  columns=list("ABCD"))
print(df)
print('\n col max index:\n', df.idxmax())
print('\nraw max index:\n', df.idxmax(axis=1))
print('\ncol max index(no skip na):\n', df.idxmax(skipna=False))
# idxmin()与idxmax()用法一致，这里看看是否不跳过na时，max和min均会取到na所在位置
print('\ncol min index(no skip na):\n', df.idxmin(skipna=False))        # min也取na，表示未知该值的下标