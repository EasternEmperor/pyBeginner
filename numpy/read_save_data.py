import numpy as np
import os

# 读取csv
with open('data.csv', 'r') as f:
    print('\n', f.read())

# 自定义读取数据np.loadtxt(filename, delimiter, skiprows, comments, dtype)
# delimiter：文件的分隔符；skiprows：跳过头几行；comments：忽略以设定字符开头的行，dtype：以该数据格式读取
data = np.loadtxt('data.csv', delimiter=',', skiprows=1, dtype=np.int64)[ : , 1 : ]
print(data)
data = np.loadtxt('data.txt', delimiter=',', dtype=np.int64)
print(data)

# 从字符串中读取
row_string = "20131, 10, 67, 20132, 11, 88, 20133, 12, 98, 20134, 8, 100, 20135, 9, 75, 20136, 12, 78"
data = np.fromstring(row_string, dtype=np.int64, sep=',')
print(data)
data = data.reshape(6, 3)       # reshape()重塑维度
print(data)

# 存储数据
# np.savetxt(filename, data, delimiter, fmt)
# data：待储存的数组；fmt：保存的数据形式，如'%f'
print('data: ', data)
np.savetxt('read_save_data.csv', data, delimiter=',', fmt='%s', encoding='utf-8')
with open('read_save_data.csv', 'r', encoding='utf-8') as f:
    print('\n', f.read())

# 二进制存储：np.save(filename, data)
# 二进制读取：np.load(filename)
np.save('save_data.npy', data)
npy_data = np.load('save_data.npy')
print(npy_data)

# 二进制存储，并且存储多个array到一个文件：np.savez(filename, **kwds, **args)
# kwds：用于给保存的数组一个代称，之后读取时可以根据这个来使用数据；args：数组
data1 = np.array([1, 2, 3])
data2 = np.array([12, 13, 23, 23])
np.savez('save_data.npz', first = data1, second = data2)
data = np.load('save_data.npz')
print('data1: ', data['first'])
print('data2: ', data['second'])

# savez更节省空间的：savez_compressed(filename, **kwds, **args)
np.savez_compressed('save_data_compressed.npz', first = data1, second = data2)
# 对比空间：os.path.getsize(filename)
print('save_data.npz size:', os.path.getsize('save_data.npz'))
print('save_data_compressed.npz size:', os.path.getsize('save_data_compressed.npz'))