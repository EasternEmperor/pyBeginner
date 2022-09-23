import numpy as np
import pandas as pd

data = np.arange(-12, 12).reshape(6, 4)
df = pd.DataFrame(
    data,
    index = list('abcdef'),
    columns = list('ABCD')
)
print(df)

# 行列可直接乘数
df['A'] *= 0
print(df)

# iloc、loc也可进行计算
# iloc搜索下标索引；loc搜索标签
df.iloc[1, 0] += 100
df.loc['a', 'A'] += 200
print(df)
df.loc['a', : ] *= 2
print(df)

# 条件运算
df['A'][df['A'] == 0] = 5
print(df)
df.loc['a', df.iloc[0, : ] < 0] *= -1
print(df)

# 调用外部函数对df进行运算：df.apply(func, axis, result_type)
# func：传入的函数；axis：要操作的维度；result_type：结果返回形式，'expand'：输出的结果可以生成多个columns
#                                                        'broadcast'：输出结果保持原df的标签
df = pd.DataFrame(np.arange(0, 6).reshape(3, 2), columns=list('AB'))
print(df)
# 做平方根：np.sqrt(df)
print(np.sqrt(df))
print(df.apply(np.sqrt))

# 自己编写的数据处理函数调用

def func(x):
    return x[0] * 2, x[1] * -1
print(df.apply(func, axis=1, result_type='expand'))

# 测试：若func只输出一列，result_type='expand'会如何输出
def func(x):
    return x[0] ** 2
print(df.apply(func, axis=1, result_type='expand'))     # 仅输出一列

# result_type = 'broadcast'
def func(x):
    return x[0] ** 2, x[1] * -1
print(df.apply(func, axis=1, result_type='broadcast'))

def func(x):
    return x[0] * 2
# broadcast会将输出结果结合df标签输出，这里输出了两列相同的结果
print(df.apply(func, axis=1, result_type='broadcast'))

# 只改一个column
def func(x):
    return x['A'] * -1
print(df.apply(func, axis=1))

# 修改两个column
def func(x):
    return x['A'] * -1, x['B'] ** 2
print(df.apply(func, axis=1))       # 没有expand会输出元组

# 修改原df中的一列
def func(x):
    return x['A'] * -1
df['B'] = df.apply(func, axis=1)
print(df)

# 修改行
def func(x):
    return x[1] ** 2
new_row = df.apply(func, axis=0)
print('\nnew_row:\n', new_row)
# 修改原df的行
df.iloc[1, : ] = new_row
print(df)