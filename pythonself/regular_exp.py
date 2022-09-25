import re
import time

# 匹配邮箱
ptn = re.compile(r'\w+?@\w+?\.com')

# 匹配正则：search(reg, string)
matched = ptn.search('zql@qq.com')
print('zql@qq.com is a valid email:', matched)      # 匹配成功返回值中有匹配子串在母串的下标范围（左闭右开）
matched = ptn.search('zql@qq+com')
print('zql@qq+com is a valid email:', matched)
# 返回匹配的子串：group()
matched = re.search(r'run', 'I run to you')
print(matched)
print(matched.group())      # 返回匹配的子串

# 正则多个判断在一个表达式中：'|'
print(re.search(r'run|ran', 'I run to you'))
# 用[]表示该位置多个符合正则的字符
print(re.search(r'r[ua]n', 'I run to you'))
# 用( | )表示多个字符的不同匹配：即()里可以放|、[]等运算
print(re.search(r'f(ou|i)nd', 'I find you'))
print(re.search(r'f(ou|i)nd', 'I found you'))

# 匹配电话：\d{n}
print(re.search(r'138\d{8}', '13853447890'))    # 匹配以138开头的号码

# 对汉字的匹配：以下用到?：前面的模式可有可无；*：前面的模式0次或者多次；.：匹配单个字符
print(re.search(r'不?爱', '我爱你'))         # '爱'
print(re.search(r'不?爱', '我不爱你'))        # '不爱'
print(re.search(r'不.*?爱', '我不是很爱你'))    # '不是很爱'
# 汉字unicode码范围：\u4e00-\u9fa5
print(re.search(r'[\u4e00-\u9fa5]+', '钟起龙'))
# 加上标点
print(re.search(r'[\u4e00-\u9fa5！？。、，￥【】……]+', '钟起龙……不是。'))

# re func：re.search()：扫描整个字符串，找到第一个匹配的子串；
# re.match()：从字符串开头开始匹配，即只从起始位置往后匹配，成功返回match object
# re.findall()：返回一个不重复的pattern的匹配串
# re.finditer()：和findall一样，但是用迭代器的方式返回值
# re.split()：用正则拆分字符串
# re.sub(reg, rep)：将匹配的字符串用输入的替换
# re.subn()：和sub一样，但会返回替换的次数
print('search:', re.search(r'run', 'I run to you'))
print('match:', re.match(r'run', 'I run to you'))
print('findall:', re.findall(r'r[au]n', 'I run to you. you ran to him.'))
print('finditer:', [i for i in re.finditer(r'r[au]n', 'I run to you. you ran to him.')])
print('split:', re.split(r'r[au]n', 'I run to you. you ran to him'))
print('sub:', re.sub(r'r[au]n', 'jump', 'I run to you. you ran to him'))
print('subn:', re.subn(r'r[au]n', 'jump', 'I run to you, you ran to him'))

# 获取正则串匹配到的信息
# 下面例子中去除.jpg后缀，用()将要取出的正则匹配括起即可达成
string = "I have 2021-02-01.jpg, 2021-02-02.jpg, 2021-02-03.jpg"
print('without ():', re.findall(r'[\w-]+\.jpg', string))
print('with ():', re.findall(r'([\w-]+)\.jpg', string))
# 将年月日分开获取，可以多用几个括号()
# finditer()的迭代器遍历用group()来取
match = re.finditer(r'(\d+)-(\d+)-(\d+)\.jpg', string)
for i in match:
    print('match string:', i.group(0), 'year:', i.group(1), 'month:', i.group(2), 'day:', i.group(3))
# findall()直接为列表，但是不能像finditer()一样group(0)上是全匹配的子串
match = re.findall(r'(\d+)-(\d+)-(\d+)\.jpg', string)
for i in match:
    print('year:', i[0], 'month:', i[1], 'day:', i[2])
# finditer()还能通过在括号内()加?P<索引名>，然后通过group('索引名')来取
match = re.finditer(r'(?P<year>\d+)-(?P<month>\d+)-(?P<day>\d+)\.jpg', string)
for i in match:
    print('match string:', i.group(0),
          'year:', i.group('year'),
          'month:', i.group('month'),
          'day:', i.group('day'))

# 匹配模式：flags
# re.I：忽略大小写；
ptn, string = r'r[ua]n', 'I Run to you'
print('without re.I:', re.search(ptn, string))
print('with re.I:', re.search(ptn, string, flags=re.I))
# re.M：多行模式，可改变^和$的行为，即原来^是文件/字符的顶行开头，儿用re.M后则是每行的开头都会匹配
# 下例中，我们需要匹配第二行的run，但仅用^是匹配不到的，加上re.M就可以。
# 同时注意，由于match是从开头开始匹配，因此就算加了re.M，match也匹配不到
ptn = r'^run'
string = 'I \nrun to you'
print('search without re.M:', re.search(ptn, string))
print('search with re.M:', re.search(ptn, string, flags=re.M))
print('match with re.M:', re.match(ptn, string, flags=re.M))
# 多个flag混合用：|
string = 'I \nRun to you'
print('search with re.M | re.I:', re.search(ptn ,string, flags=re.I | re.M))
# 也可以直接在正则串中加：(?im)
ptn = r'(?im)^run'
print('search ptn (?im):', re.search(ptn, string))

# 在需要重复用到一个正则串时，可以先编译好再匹配
n = 1000000
# 不做compile
t0 = time.time()
for i in range(n):
    re.search(r'run', 'I run to you')
t1 = time.time()
print('不提前compile正则串耗时：', t1 - t0)
# 先做compile
t0 = time.time()
ptn = re.compile(r'run')
for i in range(n):
    ptn.search('I run to you')
t1 = time.time()
print('提前compile耗时：', t1 - t0)