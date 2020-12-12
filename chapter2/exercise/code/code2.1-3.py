# coding:utf-8

# 实现查找问题

A = [1, 2, 3]

v = 3
for i in range(len(A)):
    if v == A[i]:
        print(i)
        break
else:
    print('none')
