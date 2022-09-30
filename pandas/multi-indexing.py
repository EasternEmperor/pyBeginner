import pandas as pd

s = pd.Series(
  ["小米", "小明",      # 一年一班
   "小命", "小勉",      # 一年二班
   "小牛", "小鸟",      # 二年一班
   "小南", "小妮"       # 二年二班
   ], name="name")

# 从元组设置索引：pd.MultiIndex.from_tuples(tps, names=[])
print('from_tuples:')
tuples = [
    # 年级，班级
    ('one', '1'),
    ("one", "1"),
    ("one", "2"),
    ("one", "2"),
    ("two", "1"),
    ("two", "1"),
    ("two", "2"),
    ("two", "2"),
]
index1 = pd.MultiIndex.from_tuples(tuples, names = ['grade', 'class'])
print(index1)
# 可以直接通过s.index = index1赋值index
s.index = index1
print(s)
# 也可以在创建时加上
s = pd.Series(
  ["小米", "小明",      # 一年一班
   "小命", "小勉",      # 一年二班
   "小牛", "小鸟",      # 二年一班
   "小南", "小妮"       # 二年二班
   ],
    index=index1,
    name="name")
print(s)
print(s.index)

# 分级构建，用iter来创建，一级为年级，二级为班级：pd.MultiIndex.from_product()
print('from_product:')
iterables = [
    ['one', 'two'],
    ['1', '1', '2', '2']
]
index2 = pd.MultiIndex.from_product(iterables, names=['grade', 'class'])
s = pd.Series(
  ["小米", "小明",      # 一年一班
   "小命", "小勉",      # 一年二班
   "小牛", "小鸟",      # 二年一班
   "小南", "小妮"       # 二年二班
   ],
    index=index2,
    name="name")
print(s)
print(s.index)

# 从DataFrame创建：pd.MultiIndex.from_frame(df, names = [])
print('from_frame:')
df = pd.DataFrame(
    [
        # 年级，班级
        ("one", "1"),
        ("one", "1"),
        ("one", "2"),
        ("one", "2"),
        ("two", "1"),
        ("two", "1"),
        ("two", "2"),
        ("two", "2"),
    ],
    columns=['grade', 'class']
)
index3 = pd.MultiIndex.from_frame(df)
s.index = index3
print(s)
print(s.index)

# 前面都是对Seires添加多重索引，对DataFrame也是一样的
print('\nMultiIndex on DataFrame:')
df = pd.DataFrame(
    {
        "id": [11,12,13,14,15,16,17,18],
        "name": [
             "小米", "小明",      # 一年一班
             "小命", "小勉",      # 一年二班
             "小牛", "小鸟",      # 二年一班
             "小南", "小妮"       # 二年二班
        ]
    },
    index=index1,
)
print(df)
print(df.index)

# 给列加多索引是一样的，在创建时将columns赋值即可。
df2 = pd.DataFrame(
    [[11,12,13,14,15,16,17,18],
     ["小米", "小明",      # 一年一班
     "小命", "小勉",      # 一年二班
     "小牛", "小鸟",      # 二年一班
     "小南", "小妮"       # 二年二班
     ]],
    columns=index1,
    index=['id', 'name']
)
print(df2)
# 或者df.columns赋值
df2 = pd.DataFrame(
    [[11,12,13,14,15,16,17,18],
     ["小米", "小明",      # 一年一班
     "小命", "小勉",      # 一年二班
     "小牛", "小鸟",      # 二年一班
     "小南", "小妮"       # 二年二班
     ]],
    index=['id', 'name']
)
df2.columns = index2
print(df2)
print(df2.columns)

# 选择多重索引下的数据
# 列多重索引，和正常读取数据一样通过df['col1']['col2']
print(df2)
print('col MultiIndex:')
print(df2['one'])
print(df2['one']['1'])
# 行多重索引，用loc锁定
print(df)
print('row MultiIndex:')
print(df.loc['one'])
print(df.loc['one'].loc['1'])
