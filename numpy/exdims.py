import numpy as np

# 合并数组方法（仍为一维）
cars1 = np.array([1, 2, 3, 4])
cars2 = np.array([5, 6, 7])
cars = np.concatenate([cars1, cars2])
print(cars)

# 合并数组为二维
test1 = np.array([5, 10, 16, 26])
test2 = np.array([2.1, 5.4, 10.7, 11])
# 将二者均升维为二维数组
test1 = np.expand_dims(test1, 0)    # expand_dims()方法
test2 = test2[np.newaxis, :]        # newaxis方法，这里和expand_dims(, 0)一样
print(test1)
print(test2)
all_tests = np.concatenate([test1, test2])
print(all_tests)

# expand_dims()说明
test = np.array([5, 10, 16, 26])    # 一维
print(test.shape)                   # (4, )  一维且一维的长度是4
test = np.expand_dims(test, 0)      # (1, 4) 二维且一维长度是1，二维长度是4
print(test.shape)
print(test)
test = np.expand_dims(test, 1)      # (1, 1, 4) 三维且一维长度是4，二维长度是1，三维长度是1
print(test.shape)
print(test)

print(all_tests.shape)              # (2, 4) 换成all_tests来测试expand_dims()
all_tests = np.expand_dims(all_tests, 0)    # (1, 2, 4)  因为在shape下标为0的地方插入一维，
print(all_tests.shape)                      # 则一维长度为1，二维长度为4，三维长度为2，四维长度为1
print(all_tests)
all_tests = np.expand_dims(all_tests, 1)    # (1, 1, 2, 4)  在shape下标为1的地方插入一维
print(all_tests.shape)                      # 则一维长度为1，二维长度为1，三维长度为2，四维长度为4
print(all_tests)