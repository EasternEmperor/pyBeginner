import numpy as np

# 用于检测函数运行速度
import timeit
from functools import partial
def get_run_time(func, *args):
    repeat = 3
    number = 200
    return min(timeit.Timer(partial(func, *args)).repeat(repeat=repeat, number=number)) / number

# 将多维数组展成一维
# np.ravel()：返回视图view，在返回值上修改会影响原数组
# np.flatten()：返回copy
a = np.random.rand(1000, 1000)
b = np.random.rand(1000, 1000)
def f1():
    a.flatten()
def f2():
    b.ravel()
print('time : %.6f - flatten', get_run_time(f1))
print('time : %.6f - ravel', get_run_time(f2))

# 使用到view的array取值方式：切片和ravel
# 使用到copy的array取值方式：mask和index

# 提升速度的方法：
# 用np.take(data, index, axis=)代替用index选数据
a = np.random.rand(1000000, 10)
index = np.random.randint(0, len(a), size=10000)
def f3():
    _ = a[index]
def f4():
    _ = np.take(a, index, axis=0)
print('time : %.6f - index', get_run_time(f3))
print('time : %.6f - take', get_run_time(f4))

# 用np.compress(mask, data, axis=)替代mask选数据
a = np.random.rand(10000, 10)
mask = a[ : , 0] < 0.5
def f5():
    _ = a[mask]
def f6():
    _ = np.compress(mask, a, axis=0)
print('time : %.6f - mask', get_run_time(f5))
print('time : %.6f - compress', get_run_time(f6))
