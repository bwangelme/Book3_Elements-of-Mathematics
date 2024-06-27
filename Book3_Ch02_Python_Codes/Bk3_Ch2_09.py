
###############
# Authored by Weisheng Jiang
# Book 3  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk3_Ch2_09

import numpy as np

A = np.array([[1, 3],
              [5, 7]])

B = np.array([[2, 4],
              [6, 8]])

"""
C00: [1,3] * [2,6] = 20
C01: [1,3] * [4,8] = 28
C10: [5,7] * [2,6] = 52
C11: [5,7] * [4,8] = 76

C:
[
    [20, 28],
    [52, 76]
]
"""

# calculate matrix multiplication
C = A@B
print(C)
