import pandas as pd
import datetime
import matplotlib.pyplot as plt

df = pd.read_csv('../numpy/covid19_day_wise.csv')
print(df.head())

# 1、获取2020.2.3的所有数据
print('\nQuestion1:\n')
res1 = df[df['Date'] == '2020-02-03']
print(res1)

# 2、2020.1.24之前的累计病例
print('\nQuestion2:\n')
mask2 = pd.to_datetime((df['Date'])) == datetime.datetime(2020, 1, 24)
res2 = df.loc[mask2, : ]
print(res2.columns)
print(res2['Confirmed'])
# res2 = df.loc[df['Date'] == '2020-01-24', 'Confirmed']

# 3、2020.7.23的新增死亡数
print('\nQuestion3:\n')
mask3 = pd.to_datetime(df['Date']) == datetime.datetime(2020, 7, 23)
res3 = df.loc[mask3, : ]
print(res3['New deaths'])
# res3 = df.loc[df['Date'] == '2020-07-23', 'New Deaths']

# 4、从1月25到7月22日一共增长了多少确诊病例
print('\nQuestion4:\n')
mask4_1 = pd.to_datetime(df['Date']) == datetime.datetime(2020, 1, 25)
mask4_2 = pd.to_datetime(df['Date']) == datetime.datetime(2020, 7, 22)
index = df.columns.get_indexer(['Confirmed'])
print(index)
res4_1 = df.loc[mask4_1, : ].to_numpy()
res4_2 = df.loc[mask4_2, : ].to_numpy()
print('Increase confirmed: ', res4_2[0][1] - res4_1[0][1])

# 5、每天新增确诊数和新恢复数的比例？平均比例，标准差各是多少？
print('\nQuestion5:\n')
not_zero = df['New recovered'] != 0     # 被除数不能为0
new_cases = df.loc[not_zero, 'New cases']
new_recover = df.loc[not_zero, 'New recovered']
res5 = df.loc[not_zero, 'Date'].copy(deep = True).to_frame()
res5['New cases / New recovered'] = new_cases / new_recover
print(res5)
print('Average proportion:', res5['New cases / New recovered'].mean())
print('Std: ', res5['New cases / New recovered'].std())

# 6、新增确诊的变化曲线
df['New cases'].plot(title = 'Change of New cases')
plt.show()

# 7、死亡率的变化曲线
df['Deaths / 100 Cases'].plot(title = 'Change of death rate')
plt.show()