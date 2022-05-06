import numpy as np
from enum import Enum

N_States = 13

# 奖励
#    0   1  2  3  4  5  6  7  8  9  10 11 12
R = [-4, 0, 1, 3, 0, 1, 3, 0, 1, 3, 0, 1, 3]

P = np.array(
    [   # 0     1     2     3    4     5      6     7     8     9     10    11    12
        [0.00, 0.56, 0.38, 0.06, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], # 0
        [0.00, 0.00, 0.00, 0.00, 0.56, 0.38, 0.06, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], # 1
        [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.50, 0.42, 0.08, 0.00, 0.00, 0.00], # 2
        [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.40, 0.50, 0.10], # 3
        [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], # 4
        [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], # 5
        [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], # 6
        [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], # 7
        [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], # 8
        [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], # 9
        [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], # 10
        [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], # 11
        [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], # 12
    ]
)


def SolveMatrix(gamma):
    # 在对角矩阵上增加一个微小的值来解决奇异矩阵不可求逆的问题
    #I = np.eye(dataModel.N) * (1+1e-7)
    I = np.eye(N_States)
    factor = I - gamma * P
    inv_factor = np.linalg.inv(factor)
    vs = np.dot(inv_factor, R)
    return vs

if __name__=="__main__":
    v = SolveMatrix(1.0)
    print(v)
