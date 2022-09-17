import pandas as pd

# read_excel(filename, index_col=)：index_col设为0可使读取时将excel中的第一列作为索引，而不额外添加索引
df = pd.read_excel('体检数据.xlsx', index_col=0)
print(df)

# 修改并保存
df.loc[2, '体重'] = 1
print(df)
df.to_excel('体检数据_修改.xlsx')
df2 = pd.read_excel('体检数据_修改.xlsx', index_col=0)
print(df2)

# 用open打开csv文件
with open('体检数据.csv', 'r', encoding='utf-8') as f:
    print(f.read())
# 用read_csv打开
df = pd.read_csv('体检数据.csv', index_col=0)
print(df)

# 读取剪切板的内容：df.read_clipboard()
df = pd.read_clipboard()
print(df)

# 读取网页html：df.read_html()
df = pd.read_html('https://mofanpy.com/tutorials/data-manipulation/pandas/read-save/')
print(df)