import numpy as np

# 扩展维度：None, np.newaxis和expand_dims()
a = np.array([1, 2, 3, 4, 5, 6])
a_newaxis = a[np.newaxis, : ]   # (1, 6)
a_none = a[ : , None]           # (6, 1)
a_exdims = np.expand_dims(a, 1) # (6, 1)
print(a_newaxis.shape, a_none.shape, a_exdims.shape)

# 减少维度
# 减少shape上为1的维度
a_squeeze = np.squeeze(a_none)
a_squeeze_exdims = a_exdims.squeeze(axis=1)  # 如果axis为0，报错cannot select an axis to squeeze out which has size not equal to one
print(a_squeeze_exdims.shape, a_squeeze.shape)
print(a_squeeze_exdims, a_squeeze)

# 改变维度
a1 = a.reshape([2, 3])
a2 = a.reshape([3, 1, 2])
print('a1 shape = ', a1.shape)
print(a1)
print('a2.shape = ', a2.shape)
print(a2)

# 矩阵转置
a3 = a.reshape([2, 3])
aT1 = a3.T
aT2 = np.transpose(a3)
print(aT1)
print(aT2)

# 合并，前面学过的有：concatenate, hstack, vstack
feature_a = np.array([i for i in range(6)])
feature_b = np.array([i for i in range(11, 17)])
# column_stack：列合并
c_stack = np.column_stack([feature_a, feature_b])   # (6, 2)
print(c_stack.shape)
print(c_stack)
# row_stack：行合并
d_stack = np.row_stack([feature_a, feature_b])      # (2, 6)
print(d_stack.shape)
print(d_stack)

feature_c = np.array([i for i in range(6)])[ : , None]
feature_d = np.array([i for i in range(10, 16)])[ : , None]
print(feature_c)
print(feature_d)
concat_cd0 = np.concatenate([feature_c, feature_d], axis=0)
print(concat_cd0.shape) # (12, 1)
print(concat_cd0)
print(np.vstack([feature_c, feature_d]).shape)  # (12, 1)
concat_cd1 = np.concatenate([feature_c, feature_d], axis=1)
print(concat_cd1.shape) # (6, 2)
print(concat_cd1)
print(np.hstack([feature_c, feature_d]).shape)  # (6, 2)

# 拆解
a = np.array(
[[ 1, 11, 2, 22],
 [ 3, 33, 4, 44],
 [ 5, 55, 6, 66],
 [ 7, 77, 8, 88]]
)
# 削减垂直高度：vsplit；削减水平长度：hsplit
print(np.vsplit(a, indices_or_sections=2))  # 每两段切一次
print(np.vsplit(a, indices_or_sections=[2, 3])) # 即[ : 2]、[2 : 3]、[ : 3]分三段
print(np.hsplit(a, indices_or_sections=2))
print(np.hsplit(a, indices_or_sections=[2, 3]))