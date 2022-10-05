import pandas as pd
import matplotlib.pyplot as plt

# 读取数据
columns = ["sepal length", "sepal width", "petal length", "petal width", "class"]
df = pd.read_csv('iris.csv', names = columns)
print(df)

# 1、处理空值
print(df.isna())        # 数据太多难以判断
print(df.isna().any())  # 使用any()判断哪些列存在na数据
print(df.loc[pd.isna(df['petal width'])])   # 找出存在na的数据
df1 = df.dropna(axis = 0, how = 'any')  # how参数：'any'含有na的维度，'all'全为na的维度
print(df1.isna().any())

# 2、处理异常值
df1.plot()
plt.show()
df1['sepal length'].plot(title = 'sepal length')
plt.show()
df1['sepal width'].plot(title = 'sepal width')
plt.show()
df1['petal length'].plot(title = 'petal length')    # 绘图未发现异常
plt.show()
df1['petal width'].plot(title = 'petal width')
plt.show()
# sepal length 出现小于0的值
index = df1[df1['sepal length'] < 0].index
print(index)
df2 = df1.drop(index)   # 删除小于0的行
df2['sepal length'].plot(title = 'modified sepal length')
plt.show()
# sepal width 出现大于5的数
index = df2[df2['sepal width'] > 5].index
print(index)
df3 = df2.drop(index)   # 删除过于大的行
df3['sepal width'].plot(title = 'modified sepal width')
plt.show()
# petal width 出现大于5的数
index = df3[df3['petal width'] > 5].index
print(index)
df4 = df3.drop(index)   # 删除过于大的行
df4['petal width'].plot(title = 'modified petal width')
plt.show()

# 3、切分训练和测试数据：可能需要打乱原数据
# 对于本数据集，由于同一类的数据都在相邻的行，所有应打乱后再取：df.sample(frac, replace, weights, axis)
# frac：返回数据占比
df5 = df4.sample(frac=1)
print(df5)
t_prop = int(len(df5) * 0.8)     # 训练数据占80%
train_data = df5.iloc[ : t_prop]
test_data = df5.iloc[t_prop : ]
print('train data:\n', train_data)
print('test_data:\n', test_data)

# 4、切分标签数据
print()
def get_xy(df):
    return df[['sepal length', 'sepal width', 'petal length', 'petal width']], df[['class']]

train_x, train_y = get_xy(train_data)
print(train_x)
print(train_y)
test_x, test_y = get_xy(test_data)
print(test_x)
print(test_y)
# 将df数据转为numpy
train_x_value, train_y_value = train_x.values, train_y.values
print(train_x_value[ : 3])
print(train_y_value[ : 3])