#目录
[2.1-1](#2.1-1)
[2.1-2](#2.1-2)
[2.1-3](#2.1-3)
[2.1-4](#2.1-4)

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
    if v==A[i]
        return i
        
```

[python实现](./code/code2.1-3.py)

### 证明

* 初始化
    在循环之前，显然成立，即列中不包含这个元素，打印 None
* 保持
    每一步循环，都是对一个元素的值与 v 相比较，如果相同时，就返回i，否则就进行下一个元素的比较
* 终止
    导致for 终止的条件有两个
    1. i >= A.length，这个时候，还没匹配到元素，则返回 None
    2. v==A[i] 这个时候说明已经查找到对应数值


# 2.1.4
> 考虑把两个n 位二进制整数加起来的问题，这两个整数分别存储在两个n 元数组A和B中。这两个整数的和应按二进制形式存储在一个(n+1)元数组C中。请给出该问题的形式化描述，并写出伪代码。

## 回答

### 形式化描述
本题就是在求两个数的和，只是说这两个数，是以二进制形式保存在数组中的。我们要做的事情是，实现基础的加法运算，并注意进位问题

### 伪代码
```
carray = 0
for i=A.length -1 to 0
    r= A[i] + B[i] + carray
    carray = r /2 
    C[i+1] = r %2
if carray > 0
    C[0]=1
```

[python实现](./code/code2.1-4.py)


# 如果本系列文章对您有用，欢迎小额赞助
![image.png](http://ww1.sinaimg.cn/large/d1bc6e1ely1gll5hqkm3uj20880akjsz.jpg)