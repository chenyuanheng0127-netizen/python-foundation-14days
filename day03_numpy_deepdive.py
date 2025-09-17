import numpy as np
#numpy深度学习

np.random.seed(42)

a = np.array([1, 2, 3, 4, 5])
print("Array a:", a)
print("Type of a:", type(a)) # <class 'numpy.ndarray'>

# create a equally spaced array
b = np.arange(10, 21, 2) 
print("Array b:", b) # [10 12 14 16 18 20]

c = np.linspace(0, 1, 5)
print("Array c:", c) # [0.   0.25 0.5  0.75 1.  ]

M = np.arange(15).reshape(3, 5)
print("Matrix M:\n", M)
# [[ 0  1  2  3  4]
#  [ 5  6  7  8  9]    
#  [10 11 12 13 14]]
print("Shape of M:", M.shape) # (3, 5)
print(M.ndim) # 2
print(M.size) # 15
print(M.dtype) # int64
print(M.itemsize) # 8 bytes per element
print(M.nbytes) # 120 bytes total
print(M.T) # 转置
print(M[0:2, 1:5]) # 切片

A = np.arange(10)
print("Array A:", A) # [0 1 2 3 4 5 6 7 8 9]
print("A[0]:", A[0]) # 0

print(M+10) # 每个元素加10
print(M*2)  # 每个元素乘2

row = np.array([1, 0, 1, 0, 1])
print(M + row) # 广播机制
print(M * row) # 广播机制
col = np.array([[0], [1], [0]]).reshape(3, 1)
print(M + col) # 广播机制
print(M * col) # 广播机制

#boolean indexing
print(M[M > 10]) # [11 12 13 14]
MASK = A % 2 == 0
print(A[MASK]) # [0 2 4 6 8]
print(MASK) # [ True False  True False  True False  True False  True False]

A[A % 2 == 0] = -1
print(A) # [-1  1 -1  3 -1  5 -1  7 -1  9]

# axis=0 列方向操作，axis=1 行方向操作
print(M.sum(axis=0)) # 每列求和 [15 18 21 24 27]
print(M.sum(axis=1)) # 每行求和 [10 35 60]
print(M.mean())     # 所有元素的均值 6.

#reshape
R = M.ravel()# 展平为1D
R2 = M.flatten()#一定返回拷贝
print(R, R2) # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14] [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]

v = np.array([1, 2, 3, 4, 5])
v_row = v[np.newaxis, :] # 1x5
v_col = v[:, np.newaxis] # 5x1
print(v_row, v_col)

# 通用函数（ufunc）与向量化
x = np.array([-2.0, -0.5, 0.0, 0.5, 2.0])
print(np.abs(x))
print(np.exp(x))
print(np.maximum(x, 0.0))                # ReLU
print(np.where(x > 0, x, 0))             # 条件选择 → 与布尔索引搭配

#dtype 与“提升”（upcasting）
a = np.array([1, 2, 3], dtype=np.int32)
b = np.array([1.0, 2.0, 3.0], dtype=np.float64)
c = a + b  # a会被提升为float64
print(c, c.dtype)  # [2. 4. 6.] float64 

#就地(in-place) vs 非就地
A = np.arange(5, dtype=np.float64)
A *= 2          # 就地修改，省内存
B = A * 2       # 生成新数组（非就地）