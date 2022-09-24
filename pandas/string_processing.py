import pandas as pd
# 对比python自带的字符处理函数
# 注意：要使用pandas的文字处理函数，需确保df和series中为string类型
#      如果不能保证，则需要通过astype('string')将其转化为string再处理

# upper()
py_s = "A,B,C,Aaba,Baca,CABA,dog,cat"
pd_s = pd.Series(["A", "B", "C", "Aaba", "Baca", "CABA", "dog", "cat"], dtype='string')
print('\npython upper:\n', py_s.upper())
print('\npandas upper:\n', pd_s.str.upper())

# lower()
print('\npython lower:\n', py_s.lower())
print('\npandas lower:\n', pd_s.str.lower())

# len()
print('\npython len:\n', [len(s) for s in py_s.split(',')])
print('\npandas len:\n', pd_s.str.len())

# strip(), lstrip(), rstrip()
py_s = ["   jack", "jill ", "    jesse    ", "frank"]
pd_s = pd.Series(py_s, dtype='string')
print('\npython strip():\n', [s.strip() for s in py_s])
print('\npandas strip():\n', pd_s.str.strip())
print('\npython lstrip():\n', [s.lstrip() for s in py_s])
print('\npandas lstrip():\n', pd_s.str.lstrip())
print('\npython rstrip():\n', [s.rstrip() for s in py_s])
print('\npandas rstrip():\n', pd_s.str.rstrip())

# split()
py_s = ["a_b_c", "jill_jesse", "frank"]
pd_s = pd.Series(py_s, dtype='string')
print('\npython split():\n', [s.split('_') for s in py_s])
print('\npandas split():\n', pd_s.str.split('_'))       # 会将切分后的字符串作为同一列输出
# 可使用参数expand(bool)使切分后的字符串作为不同列
print('\npandas split(expand = True)\n', pd_s.str.split('_', expand = True))

# 注意对dataframe类型做字符处理时，也是取其中的一行/列Series出来
df = pd.DataFrame([["a", "b"], ["C", "D"]])
print('\nDataFrame lower():\n', df.iloc[ : , 1].str.lower())


# 正则运算
# 正则匹配：contains()，只要字符串中包含了传入的pattern就为True，而不用完全匹配
pattern = r'[0-9][a-z]'
s = pd.Series(["1", "1a", "11c", "abc"], dtype="string")
print(s.str.contains(pattern))

# 正则完全匹配：match()
print(s.str.match(pattern))

# 字符替换：replace(ori, des)，将ori替换为des
py_s = ["1", "1a", "21c", "abc"]
pd_s = pd.Series(py_s, dtype='string')
print('\npython replace():\n', [s.replace('1', '9') for s in py_s])
print('\npandas repalce():\n', pd_s.str.replace('1', '9'))
# pandas的replace可以用正则替换
print('\npandas replace(reg, str):\n', pd_s.str.replace(r'[1-9]', 'NUM'))

# 查找特定字符：extract(reg)，从原字符串中查找符合模式的子字符串，若未找到则返回NaN
s = pd.Series(['a1', 'b2', 'c3'])
print('\npandas extract():\n', s.str.extract(r'([ab])(\d)'))
# r'([ab])(\d)'含义：匹配两种规则，第一种是[ab]即仅匹配'a'或'b'，第二种则是匹配'\d'即数字

# 拼接字符串：cat()，将对应列拼接
s1 = pd.Series(["A", "B", "C", "D"], dtype='string')
s2 = pd.Series(["1", "2", "3", "4"], dtype='string')
print(s1.str.cat(s2))