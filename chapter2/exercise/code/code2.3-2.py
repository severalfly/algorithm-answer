# coding:utf-8

'''
MERGE(A, p, q, r)
n1 = q-p+1
n2 = r-q
L[n1], R[n2] 初始化
for i=0 to n1-1
L[i] = A[p+i]
for j = 0 to n2-1
R[j] = A[q+j]

i = 0
j = 0
k=p
for ;i<L.length && j < R.length; k++
if L[i] <=R[j]
    A[k] = L[i]
    i++
else
    A[k] = R[j]
    j++

for i to L.length
A[k++] = L[i]
for j to R.length
A[k++] = R[j]
'''

