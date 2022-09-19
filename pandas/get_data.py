import pandas as pd
import numpy as np

data = np.arange(-12, 12).reshape((6, 4))
df = pd.DataFrame(
  data,
  index=list("abcdef"),
  columns=list("ABCD"))
print(df)

# datafram分col和row
print(df['B'])   # 取一列
print('\nnumpy cols:\n', data[ : , [2, 1]])   # np取第2列和第1列
print('\ndataframe cols:\n', df[['C', 'B']])    # df取C和B索引列

# dataframe取行列组合：df.loc()
print(df.loc['b' : 'd', 'C' : 'D'])   # 注意，与np不同之处在于，df.loc是左闭右闭的闭区间
# 对比
print(data[1 : 2, : ])
print(df.loc['b' : 'c', : ])

# 和np一样左闭右开取值：df.iloc()
print('\nnumpy:\n', data[2 : 4, 1 : 3])
print('\ndf.iloc():\n', df.iloc[2 : 4, 1 : 3])

# 索引和行列标签的转换：（注意：为左闭右开）
# df.index[]：将行转换为label
# df.columns[]：将列转换为label
row_labels = df.index[1 : 3]
print('\n', row_labels)
print('df.loc:\n', df.loc[row_labels, 'B' : 'D'])

col_labels = df.columns[[0, 3]]
print(col_labels)
print('df.loc:\n', df.loc[row_labels, col_labels])

# 从label到下标索引：
# df.index.get_indexer([]): 行标签到下标
# df.columns.get_indexer([]): 列标签到下标
col_index = df.columns.get_indexer(['B', 'D'])
row_index = df.index.get_indexer(['a', 'd'])
print('\n', col_index, '\n', row_index)
print('\n', df.iloc[row_index, col_index])

# 条件筛选过滤
# 筛选某列符合比较某个数的值
print('\n', df['A'] < -3)   # true/false mask
print(df[df['A'] < -3])     # 注意：直接将mask放入取数，会取到所有列在mask中为true的元素

# 选第1行中数据不小于-10的数：
print('\n>=:\n', df.loc[df.index[1], df.iloc[1, : ] >= -10])
print('\n~:\n', df.loc[df.index[1], ~(df.iloc[1, : ] < -10)])
# 同时，可以使用 | 来表示条件或，用 & 表示条件与
# 选第5行中数据不小于0且不大于5的数
i4 = df.iloc[4]
print('\n&:\n', df.loc[df.index[4], (i4 >= 0) & (i4 <= 5)])

print()
# Series的筛选
list_data = list(range(-4, 4))
s = pd.Series(
  list_data,
  index=list("abcdefgh"))
print(s)

# 按标签筛选：s.loc
print(s.loc[['a', 'b', 'g']])
print(s.loc['a' : 'g'])
# 按索引筛选：s.iloc
print(s.iloc[[0, 1, 5]])
print(s.iloc[1 : 5])      # 左闭右开
# 标签和下标的转换
print()
print(s.loc[s.index[[0, 5]]])
print(s.loc[s.index[0 : 3]])
#print(s.iloc[s.index.get_indexer('a' : 'f']))  # 无法用 : 取之间的
print(s.iloc[s.index.get_indexer(['a', 'f'])])