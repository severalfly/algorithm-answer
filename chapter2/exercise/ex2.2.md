#目录
[2.2-1](#2.2-1)  
[2.2-2](#2.2-2)  
[2.2-3](#2.2-3)  
[2.2-4](#2.2-4)  

# 2.2-1
> 用Ø记号表示函数 n<sup>3</sup>/1000 - 100n<sup>2</sup> - 100n +3

## 回答
因为只有3次方，所以答案为  
Ø(n<sup>3</sup>)


# 2.2-2

> 考虑交换潘旭存储在数组A中的n个数：首先找出A中的最小元素并将其余A[1]中的元素进行交换。接着，找出A中的次小元素并将其与A[2]中的元素进行交换。对A中前n-1个元素按该方式继续。该算法称为选择算法。写出其伪代码。改算法维持的循环不变式是什么？为什么它只需要对前n-1个元素，而不是对所有n个元素进行？用Ø记号给出选择排序的最好情况与最坏情况运行时间。

## 回答

1. 该算法的循环不变式
    * 每进行一步操作，都是把后面最小的数值放到当前位置，也就是说，操作完，后面已经没有比这个值更小的元素了。
    * 并且每一步操作，前面都没有比当前元素更大的元素，也就保证了排序的操作时完整的
2. 因为选择到n-1时，最后只剩一位了，即使再执行一次选择，也没有比 n 号元素更大的值了，也就不会再进行交换操作，所以只要比较到 n-1 就行了
3. 由于每次都会去查询一遍最小值，所以最坏情况与最好情况是一样的，都是 Ø(n<sup>2</sup>)


# 2.2-3
> 再次考虑线性查找问题（参见联系2.1-3）。假定要查找的元素等可能地位数组中的任意元素，平均需要检查输入序列的多少元素？最坏情况又如何呢？用Ø记号给出线性查找的平均情况和最坏情况运行时间。证明你的答案

## 回答
1. 平均要检查 n/2 个元素
2. 最坏情况 要检查 n 个元素
3. Ø(n)
4. 如何证明？
    因为在平均情况与最坏情况都是 n 的线性关系，所以结论成立
    
# 2.2-4

> 应如何修改任何一个算法，才能使之具有良好的最好情况运行时间？

## 回答
这个需要依据具体的工程来选择不同的算法去实现不同的功能。比如，都知道快速排序很快，但是，在数据量较少时，插入排序和选择排序都是很好的排序算法，而且少量数据，运行时间几乎是一样的。而且，插入排序这些，因为不占用堆栈，速度可能还会更快一些，这个时候，就需要依赖数据量选择具体的排序算法。

比如，在1.8的jdk中的排序，就是会依赖数组的大小，小于8个时，会默认使用插入排序，超过时，才使用快速排序


# 如果本系列文章对您有用，欢迎小额赞助
![image.png](http://ww1.sinaimg.cn/large/d1bc6e1ely1gll5hqkm3uj20880akjsz.jpg)
