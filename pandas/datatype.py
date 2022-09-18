import numpy.random
import pandas as pd
import numpy as np

#一维的Series

l = [11, 22, 33]
s = pd.Series(l)
print(l, '\n', s)       # 打印可知，pd额外维护了一份索引，且记录了数据类型

s = pd.Series(l, index = ['a', 'b', 'c'])   # 可以自定义索引
print(s)
print(s['a'])   # 11

# 由字典创建Series
s = pd.Series({'a': 11, 'b': 22, 'c': 33})
print(s)

# 由numpy.array创建Series
s = pd.Series(numpy.random.rand(3), index=['a', 'b', 'c'])
print(s)

# 由Series创建numpy.array和list
print('array:', s.to_numpy())
print('list:', s.to_list())

# 二维的dataframe
df = pd.DataFrame([[1, 2], [3, 4]])
print(df)       # 也会打印出行列索引
print(df.at[0, 1]) # 2

# 字典创建dataframe，字典的索引会变成列名
df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
print(df)

# 取df其中一行的数据，实际上为Seires类型
print('type:', type(df['col1']))

# 将两个Seires拼接
df = pd.DataFrame({'col1': pd.Series([1, 2]), 'col2': pd.Series([3, 4])})
print(df)

# df创建索引
s = pd.Series(numpy.random.randint(0, 3, 3), index=['a', 'b', 'c'])
df = pd.DataFrame({'col1': [1, 2, 7], 'col2': [3, 4, 8], 'col3': [5, 6, 9]}, index=['a', 'b', 'c'])
print(s, end = '\n')
print(df)

# 获取df的行列标签
print(df.index, '\n')
print(df.columns)

# 给json数据加行标签；json自带的标签会转换为df的列标签
my_json_data = [
  {"age": 12, "height": 111},
  {"age": 13, "height": 123}
]
df = pd.DataFrame(my_json_data, index=['Jack', 'Tom'])
print(df)

# df转换为numpy.array
print(df.to_numpy())