# coding:utf-8

# 实现n位二进制数的相加问题，本实现进对二进制长度相同有效，对于长度不相同的，可以简单修改后兼容

A = [0, 0, 1, 0]
B = [1, 0, 0, 1]
C = [0, 0, 0, 0, 0]

carray = 0
for i in range(len(A) - 1, -1, -1):
    r = A[i] + B[i] + carray
    carray = r // 2
    C[i + 1] = r % 2
if carray > 0:
    C[0] = carray

print(C)
