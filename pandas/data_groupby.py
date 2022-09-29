import pandas as pd
import numpy as np

df = pd.DataFrame(
    [
        ("小红", "哈利波特", 80),
        ("小明", "蜘蛛侠", 72),
        ("小红", "雷神", 83),
        ("小红", "蜘蛛侠", 45),
        ("小明", "超人", 57),
    ],
    columns=['人', '人物', '评价']
)

# 用groupby来对某列分组
grouped = df.groupby('人')
print(grouped)
# 查看分组情况
print(grouped.groups)
# 在df中查找某组
print(df.iloc[grouped.groups['小红']])
# 可以直接通过group.get_group()来获取
print(grouped.get_group(df.iloc[0, 0]))

# 调用分好的组
# 取每组的第一个first
print(grouped.first())
# 最后一个last
print(grouped.last())
# 对分组后的数字列进行sum()、mean()操作，还有统计个数count()
print(grouped.sum())
print(grouped.mean())
print(grouped.count())

for name, group in grouped:
    print('name:', name)
    print(group)

# 按照多个标签分组：groupby([s1, s2, ...])
df = pd.DataFrame(
    [
        ("小红", "哈利波特", 80, 4),
        ("小明", "蜘蛛侠", 72, 3),
        ("小红", "雷神", 83, 4),
        ("小红", "雷神", 90, 5),
        ("小红", "蜘蛛侠", 45, 2),
        ("小明", "超人", 57, 2),
    ],
    columns=("人", "人物", "评价", '分级'),
)
# df中有两组'小红'和'雷神'
print(df.groupby(['人', '人物']).get_group(('小红', '雷神')))

# 聚合计算：group.aggregate，或者group.agg
grouped = df.groupby('人')
print(grouped.aggregate(np.mean))
# 同时计算多个统计值：agg([mean, sum, std, ...])
print(grouped.agg([np.mean, np.sum, np.std]))
print(grouped['评价'].agg([np.mean, np.sum, np.std]))
# 可以给计算值重命名为中文：agg([]).rename([])
print(grouped['评价'].agg(
    [np.mean, np.sum, np.std]
).rename(
    columns = {
        'mean': '平均',
        'sum': '总和',
        'std': '标准差'
    }))