
# 加载数据
import numpy as np
import matplotlib.pyplot as plt

with open('covid19_day_wise.csv', 'r', encoding='utf-8') as f:
    data = f.readlines()

print(data[0])
covid = {
    'date': [],
    'data': [],
    'head': [h for h in data[0].strip().split(',')[1 : ]]
}
print(covid['head'])
for row in data[1 : ]:
    split_row = row.strip().split(',')
    covid['date'].append(split_row[0])
    covid['data'].append([float(n) for n in split_row[1 : ]])
print(covid['date'])
print(covid['data'][ : 5])

# 1、获取2020年 2 月 3 日的所有数据
idx1 = covid['date'].index('2020-02-03')
print('data of 2020-02-03:')
for number, header in zip(covid['data'][idx1], covid['head']):
    print(header + ':', number)
print()

# 2、2020 年 1 月 24 日之前的累积确诊病例有多少个？
idx2 = covid['date'].index('2020-01-24')
print('Confirmed before 2020-01-24:')
print(covid['data'][idx2][0], end = '\n\n')

# 3、2020 年 7 月 23 日的新增死亡数是多少？
idx3 = covid['date'].index('2020-07-23')
print('New cases in 2020-07-23:')
print(covid['data'][idx3][5], end = '\n\n')

# 4、从 1 月 25 日到 7 月 22 日，一共增长了多少确诊病例？
idx4 = covid['date'].index('2020-01-25')
idx5 = covid['date'].index('2020-07-22')
increase = covid['data'][idx5][0] - covid['data'][idx4][0]
print('increasing cases from 2020-02-25 to 2020-07-22:')
print(increase, end = '\n\n')

# 每天新增确诊数和新恢复数的比例？平均比例，标准差各是多少？
newCases = []
newRecovers = []
for i in range(1, len(covid['date'])):
    newCases.append(covid['data'][i][4])
    newRecovers.append(covid['data'][i][6])
newCases = np.array(newCases)
newRecovers = np.array(newRecovers)
rate = newCases / newRecovers
print('new cases / new recovers = ', rate)
avgRate = rate.sum() / len(rate)
print('average rate = ', avgRate)
print('std rate = ', rate.std(), end = '\n\n')


def draw_line(x):
    plt.plot(x)
    plt.show()

# 6、画图展示新增确诊的变化曲线
idx6 = covid['head'].index('New cases')
data = np.array(covid['data'])
draw_line(data[ : , idx6])

# 7、画图展示死亡率的变化曲线
confirmed7 = data[1 : , 0]
deaths7 = data[1 : , 1]
deathRate = deaths7 / confirmed7
draw_line(deathRate)