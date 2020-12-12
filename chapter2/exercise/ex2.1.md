#目录
[2.1-1](#2.1-1)

# 2.1-1
> 以图2-2为模型，说明 `INSERTTION-SORT` 在数组 `A=<31, 41, 59, 26, 41, 58>`上的执行过程

## 回答
图示更清楚
![image.png](http://ww1.sinaimg.cn/large/d1bc6e1egy1glkwvn8o63j20u0140nlb.jpg)



# 2.1-2
> 重写过程`INSERTION-SORT`，使之按非升序（而不是降序）排序。

## 回答
伪代码如下
```
for j = 2 to A.length
    key = A[j]
    i = j -1
    
    while(i > 0 && A[i] < key)
        A[i+1] = A[i]
        i = i -1
        
    A[i+1] = key
```

[python 实现](./code/code2.1-2.py)


# 2.1-3
> 考虑以下查找问题

输入：n个数的一个序列A=<a<sub>1</sub>， a<sub>2</sub>, ... a<sub>n</sub>> 和一个是v  
输出：下标i使得`v=A[i]`或者当v不再A中出现时，v 为特殊值null
写出线性查找的伪代码。它扫描整个序列来查找v。使用一个循环不变式来证明你的算法是正确的。确保你的循环不变式满足三条必要的性质

## 回答

### 伪代码
```
for i = 0 to A.length
    if v=A[i]
        return i
        
```