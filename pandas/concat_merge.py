import pandas as pd

df1 = pd.DataFrame({
    "A": ["A0", "A1", "A2", "A3"],
    "B": ["B0", "B1", "B2", "B3"],
    "C": ["C0", "C1", "C2", "C3"],
    "D": ["D0", "D1", "D2", "D3"],
}, index=[0, 1, 2, 3],)

df2 = pd.DataFrame({
    "A": ["A4", "A5", "A6", "A7"],
    "B": ["B4", "B5", "B6", "B7"],
    "C": ["C4", "C5", "C6", "C7"],
    "D": ["D4", "D5", "D6", "D7"],
}, index=[4, 5, 6, 7],)

df3 = pd.DataFrame({
    "A": ["A8", "A9", "A10", "A11"],
    "B": ["B8", "B9", "B10", "B11"],
    "C": ["C8", "C9", "C10", "C11"],
    "D": ["D8", "D9", "D10", "D11"],
}, index=[8, 9, 10, 11],)

# 将三者上下拼接：concat(df1, df2, ...)     默认是按列上下拼接
print(pd.concat([df1, df2, df3]))
# 如果想要拼接后仍能按key索引拼接起来的df1、df2、df3，可加上一个keys参数
# 注意：用loc()来查询key
all_classes = pd.concat([df1, df2, df3], keys = ['class1', 'class2', 'class3'])
print(all_classes)
print(all_classes.loc['class1'])

# concat()默认是上下拼接，但也可以左右拼接（增加列），只需将axis改为对应维度上操作
# 行(index)可以不对齐，pd会将空缺的行填为na数据：类似与mysql的外连接（并集）
df = pd.DataFrame({
    'B': ['b1', 'b2', 'b3'],
    'C': ['c1', 'c2', 'c3'],
    'F': ['f1', 'f2', 'f3']
}, index = [2, 4, 5])
print(df1)
print(df)
print(pd.concat([df1, df], axis=1))

# 如果只要拼接后对齐的那部分，则将join参数改为'inner'即可。类似于mysql的内连接（交集）
print(pd.concat([df1, df], axis = 1, join = 'inner'))

# 如果不在乎拼接前的index，可以用参数ignore_index设置。
# 这里axsi默认为0，所以操作的是行，会将列名相同的行放在一起
print(pd.concat([df1, df], ignore_index=True, sort=False))

# 为df添加新列/行，也用concat即可
# 下面作为新列添加进df，直接添加即可
s = pd.Series(['x1', 'x2', 'x3', 'x4'], name = 'X') # name在to_frame里也可以重新设置
print(pd.concat([df1, s], axis=1))    # axis为1，添加新列

# 但是注意，Series作为新行添加进df要先用to_frame转换为df
s = pd.Series(['A5', 'B6', 'C4', 'Y9'], index=['A', 'B', 'C', 'Y'])
# 还需转置，ignore_index为忽略行上的列标签，会将列名相同的列合并
print(pd.concat([df1, s.to_frame().T], ignore_index=True))

# 更精细的操作可用merge：concat可以同时上下/左右拼接多张表，但是merge只能同时左右拼接两张
# merge的拼接种类类似于mysql，有内连接、外连接、左外连接、右外连接和笛卡尔积形式
left = pd.DataFrame({
    "key": ["K0", "K1", "K2", "K4"],
    "A": ["A0", "A1", "A2", "A3"],
    "B": ["B0", "B1", "B2", "B3"],
})
right = pd.DataFrame({
    "key": ["K0", "K1", "K2", "K3"],
    "C": ["C0", "C1", "C2", "C3"],
    "D": ["D0", "D1", "D2", "D3"],
})
print(pd.merge(left, right, on='key'))  # 按'key'连接，how默认是inner（内连接，并）

# 也可以指定多个拼接列
left = pd.DataFrame({
    "key1": ["K0", "K0", "K1", "K2"],
    "key2": ["K0", "K1", "K0", "K1"],
    "A": ["A0", "A1", "A2", "A3"],
    "B": ["B0", "B1", "B2", "B3"],
})


right = pd.DataFrame({
    "key1": ["K0", "K1", "K1", "K2"],
    "key2": ["K0", "K0", "K0", "K0"],
    "C": ["C0", "C1", "C2", "C3"],
    "D": ["D0", "D1", "D2", "D3"],
})

print(pd.merge(left, right, on=['key1', 'key2']))   # 内连接

# 内连接
print('内连接：')
print(pd.merge(left, right, how='inner', on=['key1', 'key2']))
# 左外连接
print('左外连接：')
print(pd.merge(left, right, how='left', on=['key1', 'key2']))
# 右外连接
print('右外连接：')
print(pd.merge(left, right, how='right', on=['key1', 'key2']))
# 外连接（并）
print(pd.merge(left, right, how='outer', on=['key1', 'key2']))
# 全连接（笛卡尔积）
print('全连接：')
print(pd.merge(left, right, how='cross'))

# df.join()：类似于concat和merge的结合体
# 可以像concat一样用索引连接，也可以像merge一样用某列作为连接标准
left = pd.DataFrame({
    "A": ["A0", "A1", "A2"],
    "B": ["B0", "B1", "B2"]
}, index=['x1', 'x2', 'x3'])
right = pd.DataFrame({
    "C": ["C0", "C2", "C3"],
    "D": ["D0", "D2", "D3"]
}, index=['x1', 'x2', 'x3'])

# 直接连接，默认为左连接(how='left')
print('join:')
print(left.join(right))
print('concat:')
print(pd.concat([left, right], axis=1))
# 用index连接无法通过merge实现

left = pd.DataFrame({
    "A": ["A0", "A1", "A2", "A3"],
    "B": ["B0", "B1", "B2", "B3"],
    "key": ["K0", "K1", "K0", "K1"],
})


right = pd.DataFrame({
    "C": ["C0", "C1"],
    "D": ["D0", "D1"]
}, index=["K0", "K1"])

# 使用key作为连接依据
print(left)
print(right)
print('join:')
# 注意right的index和left的'key'相同的部分也会连接，merge是做不到的
print(left.join(right, on='key'))