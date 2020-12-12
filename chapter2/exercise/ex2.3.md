#目录
[2.3-1](#2.3-1)  
[2.3-2](#2.3-2)  
[2.3-3](#2.3-3)  
[2.3-4](#2.3-4)  

# 2.3-1
> 使用图2-4作为模型，说明归并排序在数组A=<3,41, 52, 26, 38, 57, 9, 49>上的操作
直接上图，
![image.png](http://ww1.sinaimg.cn/large/d1bc6e1ely1gll6lvww91j21960pu1kx.jpg)


# 2.3-2
> 重写过程 MERGE ，使之不使用哨兵，而是一旦数组L或R的所有元素均被复制回A就立刻停止，然后把另一个数组的剩余部分复制回A

## 思考
读了几遍这个题目，才理解这个题目到底是要我们做什么。

正文中的 MERGE(A, p ,q, r) ，有一个简化的步骤，就是说加一个∞ 作为哨兵，这个题目要求我们把这个哨兵干掉，去实现其伪代码

相比书中所言，本方法需要处理结束的问题，以及提前结束后，剩余数据处理的问题，这些已经在下面伪代码中的后面三个for中展示

### 伪代码
```
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
```

# 如果本系列文章对您有用，欢迎小额赞助
![image.png](http://ww1.sinaimg.cn/large/d1bc6e1ely1gll5hqkm3uj20880akjsz.jpg)
