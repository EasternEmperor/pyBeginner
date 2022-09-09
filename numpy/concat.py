import numpy as np

test1 = np.array([5, 10, 13, 14])
test2 = np.array([6.9, 1.2, 5.3, 199.8])
all_tests = np.concatenate([test1, test2], 0)   # 在shape坐标0处将二者合并，all_tests的shape为(1, 4)
print(all_tests.shape)
print(all_tests)

test1 = np.expand_dims(test1, 0)    # shape (1, 4)
test2 = test2[np.newaxis, :]        # shape (1, 4)
all_tests = np.concatenate([test1, test2], 1)   # shape 1处合并，shape为(1, 8)
print(all_tests.shape)
print(all_tests)
all_tests = np.concatenate([test1, test2], 0)   # shape 0处合并，shape为(2, 4)
print(all_tests.shape)
print(all_tests)