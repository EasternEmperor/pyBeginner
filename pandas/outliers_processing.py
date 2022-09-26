import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame([[1, None], [np.nan, 2]])
a = np.array([[1, None], [np.nan, 2]])
print(df)

# 判断空数据：df.isna()
print(df.isna())
# 判断非空数据：df.notna()
print(df.notna())
# 也可以通过~来取反
print(~df.notna())

# 计算跳过na数据：pd运算函数中的skipna(bool)
df = pd.DataFrame({
    "a": [1, None, 1],
    "b": [np.nan, 4, 4]
})
print(df)
print('\nskip na:\n', df.mean(axis = 0))        # 默认skipna为True
print('\nnot skip:\n', df.mean(axis = 0, skipna = False))

# 丢弃na数据：drop(axis)：axis表明在哪个维度上进行操作，若有na值则抛弃（减少该维度的维数）
df = pd.DataFrame({
    "a": [1, None, 3],
    "b": [4, 5, 6]
})
print(df.dropna(axis=0))        # 操作行，则抛弃行
print(df.dropna(axis=1))        # 操作列，则抛弃列

# 填充na：fillna()
# 下例中用均值填充
df = pd.DataFrame({
    "a": [1, None, 3],
    "b": [4, 5, 6]
})
amean = df['a'].mean()
fill_col = df['a'].fillna(amean)
df['a'] = fill_col
print(df)
# 下例中有规律：b列为a列的2倍
df = pd.DataFrame({
    'a': [1, None, np.nan],
    'b': [2, 4, 6]
})
ana = df['a'].isna()
new_value = df['b'][ana] / 2
fill_col = df['a'].fillna(new_value)
df['a'] = fill_col
print(df)

# 不合范围的值：clip(lower, upper)：设定数据范围，超出范围的将被修正为lower/upper
df = pd.DataFrame({
    "a": [1, 1, 2, 1, 2, 40, 1, 2, 1],  # 40为异常值
})
df.plot()
plt.show()
df['a'] = df['a'].clip(lower = 0, upper = 3)
print(df)
df.plot()
plt.show()