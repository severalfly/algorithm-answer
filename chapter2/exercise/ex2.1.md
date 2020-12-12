#目录
[2.1-1](#2.1-1)

##### 2.1-1
> 以图2-2为模型，说明 `INSERTTION-SORT` 在数组 `A=<31, 41, 59, 26, 41, 58>`上的执行过程

# 回答
图示更清楚
![image.png](http://ww1.sinaimg.cn/large/d1bc6e1egy1glkwvn8o63j20u0140nlb.jpg)



##### 2.1-2
> 重写过程`INSERTION-SORT`，使之按非升序（而不是降序）排序。

# 回答
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

[python 实现](#./code/code2.1-2.py)