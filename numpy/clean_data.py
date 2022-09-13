import numpy as np
import pandas as pd

# 创建有脏数据的列表
raw_data = [
["Name", "StudentID", "Age", "AttendClass", "Score"],
["小明", 20131, 10, 1, 67],
["小花", 20132, 11, 1, 88],
["小菜", 20133, None, 1, "98"],
["小七", 20134, 8, 1, 110],
["花菜", 20134, 98, 0, None],
["刘欣", 20136, 12, 0, 12]
]
print(raw_data, end = '\n\n')

data = np.array(raw_data)   # dtype = object
print(data)

# 数据预处理
# 仅将其中数字部分取出
data_process = []
for i in range(len(raw_data)):
    if i == 0:
        continue
    data_process.append(raw_data[i][1 : ])      # 去除第一列的名字
data = np.array(data_process, dtype = np.float64)
print('data.type = ', data.dtype)
print(data, end = '\n\n')

# 查看是否有重复学号
sid = data[ : , 0]      #取出学号
unique, counts = np.unique(sid, return_counts=True)
print(unique, 'repeat', counts, 'times')
print(unique[counts > 1], end = '\n\n')   # 查看重复出现的学号
data[4, 0] = 20135      # 改正学号

# 查看年龄缺失值
print('age:', data[ : , 1])
is_nan = np.isnan(data[ : , 1])
print('is_nan:', is_nan)        # 为bool类型的数组，true代表是nan
nan_idx = np.argwhere(is_nan)   # argwhere()返回输入数组中非0元素的索引
print(nan_idx)                  # nan元素的索引
# 计算所有学生的平均年龄。下式中：~可以对bool取反，因此不会取中nan元素
avg_age = data[~np.isnan(data[ : , 1]), 1].mean()
print('average age:', avg_age)
# avg_age为27.8，不符合学生的年龄。回看数据可知有一个学生为98，为错误数据，需剔除
# 给错误年龄和nan赋值平均年龄
normal_age_idx = ~np.isnan(data[ : , 1]) & (data[ : , 1] < 20)  # 正常年龄应 < 20
print('normal_age_idx:', normal_age_idx)
avg_age2 = data[normal_age_idx, 1].mean()
print('average age:', avg_age2)
data[~normal_age_idx, 1] = avg_age2
print('ages:', data[ : , 1], end = '\n\n')

# 选课和成绩的脏数据处理，未选课则成绩应为nan
print(data[ : , 2 : ])      # 最后一位未选课但有成绩，倒数第三位成绩超出满分
data[data[ : , 2] == 0, 3] = np.nan     # 将未选课的成绩均赋为nan
data[ : , 3] = np.clip(data[ : , 3], 0, 100)    # clip(a, min, max)将a中的数字限定在min和max之间，小于的置为min，大于置为max
print('score:', data[ : , 2 : ])

# 将该data存入csv
save = np.array(data[ : 4], dtype=np.int64)
pd.DataFrame(save).to_csv('data.csv')
# 将data存入txt
np.savetxt('data.txt', save, fmt = '%d', delimiter = ',')