import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "time": ["2022/03/12", "2022/03/13", "2022/03/14"],
    "value": [1,2,3]
})
print(df)
print('\ntime:\n', df['time'])

# 将其转换为time类型：pd.to_datetime(s)
print(pd.to_datetime(df['time']))
# pd.to_datetime(s)的智能识别
pd.to_datetime(
    ["2022/03/12", "2022.03.13", "14/03/2022"]      # 其中格式不一，但是常见的格式
)
print(pd.to_datetime(df['time']))
# 按照特定规则解析时间：pd.to_datetime(s, format)
# format: %m：月，%d：日，%Y：年的全称；%%：匹配'%'；%S：秒；%H：时；%M：分
print(pd.to_datetime(
    [
        "1@21@2022%%11|11|32",
        "12@01@2022%%44|02|2",
        "4@01@2022%%14|22|2"
    ],
    format="%m@%d@%Y%%%%%S|%H|%M"
))

# 生成时间序列：pd.data_range(start, end, freq, periods)，类似range()
start = datetime.datetime(2022, 9, 27)
end = datetime.datetime(2022, 10, 1)
index = pd.date_range(start, end)
print(index)
# 使用freq参数控制步长
index = pd.date_range(start, end, freq='48h')
print(index)
# 使用periods参数平均分，类似linspace()
print(pd.date_range(start, end, periods=6))

# 选取时间，用时间做索引绘图
start = datetime.datetime(2022, 3, 20)
end = datetime.datetime(2022, 5, 20)

rng = pd.date_range(start, end)
df = pd.Series(np.random.randn(len(rng)), index = rng)  # 用时间作为series的索引
print(df.index)
# 绘图，横坐标为时间
df.plot()
plt.show()
# 按照时间区间绘图
t1 = datetime.datetime(2022, 3, 20)
t2 = datetime.datetime(2022, 3, 27)
df[t1 : t2].plot()
plt.show()
# 直接用日期串做索引绘图
df['2022-03-20' : '2022-03-27'].plot()
plt.show()
# 直接绘制某月
df['2022-05'].plot()
plt.show()

# 时间运算
# 加减乘除：pd.Timedelta()；参数有：weeks, days, hours, minutes, seconds,
# milliseconds, microseconds, nanoseconds
rng = pd.date_range('2022-01-01', '2022-01-07')
print(rng + pd.Timedelta(weeks = 1))
print(rng + 2 * pd.Timedelta(days = 7))

# 从datetime中取出日/月等：dt.dayofyear/dayofweek/rng.weekofyear/weekday
print(rng.dayofyear)
print(rng.dayofweek)
# print(rng.weekofyear)     # weekofyear已被遗弃
print(rng.weekday)

# 按规则输出日期形式
print(rng.strftime('%m/%d/%Y'))

# 获取当日/月的名字
print(rng.day_name())       # 以星期表示
print(rng.month_name())     # 月份名

# 时区
rng = pd.date_range('2022-01-08', '2022-02-21')
print(rng.tz is None)   # True, 默认不设定时区

# 设定时区：dt.tz_localize()
s = pd.to_datetime(
    ["2022/03/12 22:11", "2022/03/12 12:11", "2022/03/12 2:11"]
)
s_us = s.tz_localize('America/New_York')
print(s_us)

# 更换时区：dt.tz_convert()
s_cn = s_us.tz_convert('Asia/Shanghai')     # import pytz 在pytz里可以查看每个时区的名称
print(s_cn)

# 生成带时区的时间
rng = pd.date_range('2022-01-10', '2022-01-31', tz = 'Asia/Shanghai')
print(rng)