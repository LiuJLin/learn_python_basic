Python 内置类型简述
==========================
本目录下的学习内容来自于 **《Python学习手册》** 和[https://learnpythonthehardway.org/book/](https://learnpythonthehardway.org/book/)<br />


## for lelp
之所以把这一项放在开头，是提醒自己多查看[python手册](https://docs.python.org/3/tutorial/index.html)<br />，或是"help(struc.method)"

## 核心数据类型
**内置对象类型**：

- 数字：1234, 3.1415,  3+4j, Decimal, Fraction
- 字符串：'spam', "guido's", b'a\xolc'
- 列表：[1,[2,'three'],4]
- 字典：{'food':'spam','taste':'yum'}
- 元组：(1,'spam',4,'U')
- 文件：myfile=open('eggs','r')
- 集合：set('abc'),{'a','b','c'}
- 其它类型：None, bool
- 编程单元类型：函数、模块、类

## 数字
类似于其他编程语言，Python也包括常见的：**整数** 、**浮点数**、**其它（有虚部的复数、固定精度的十进制数、有分子和分母的有理分数）**、**集合**。

除了表达式，还有一些常用的 **数学模块**，里面包括高级的数学工具、如函数。**random** 可生成随机数也可作随机选择器
```python
import math
math.pi
nath.sqrt(9)

import random
random.random()
random.choice([1,2,3,4])
```
## 序列
### 含义
一个“序列”是一个对位置进行排序的对象的集合。包括 **字符串、列表、元组**。
### 操作
它们共同拥有一般的序列操作，包括 **索引、分片、合并**,但是也有其各自特定的操作方法。
#### 索引
以"China"为例：
```python
s = "China"
len(s)      
```
索引是按照 **偏移量** 进行的，自然是从0开始的，比如：
```python
s[0]
'C'
```
#### 分片
```python
s[1:4]
'hin'   
>>> s[:]
'China'
```
也可以通过 **负偏移量** 进行索引，例如-1则是指最后一项，比如：
```python
>>> s[-1]
'a'
>>> s[:-1]
'Chin'
```
#### 合并
"+" 用以合并
```python
>>> s + ", I love you!"
'China, I love you!'
```

## 不可变性
 表示一旦创建后，不能随意更改。比如，不能通过对其某一位置赋值而改变该字符串，但是可以以原来的变量名创建一个新的字符串，因为会覆盖掉原来的对象。

 **不可变**：数字、字符串、元组
 **可变**： 列表、字典

## 列表
### 特定的操作，方法
![methods](https://github.com/LiuJLin/learn_python_basic/blob/master/struc/list_methods.png?raw=true "github")
### 边界检查
若是给超出列表边界外的元素赋值，会出错。
### 嵌套
列表可支持 **任意嵌套**。一个直接应用就是实现 **矩阵**，或是 **多维数组**。
### 列表解析
列表解析源自集合的概念。列表解析是写在 **方括号** 中的，且由使用了同一个变量名的表达式和 **循环结构** 组成。它是一种通过 *对序列中的每一项运行一个表达式来创建一个新列表的方法，每次一个，从左至右*。  

解析可以用来创建 **列表、集合和字典**

## 字典
不是序列，而是一种 **映射(Mapping)**,映射，是通过 **键** 而不是相对位置来存储的。没有从左至右的顺序，只是将 **键** 映射到值。具有 **可变性**  
### 创建方法
写在 **大括号{ }** 内，包含一系列的 **"键：值"** 对。  
##### 常量
```python
>>> d = {'food':'pizza', 'quantity':'2', 'flavor':'bacon'}
```
##### 创建空字典，然后再逐个填充   
```python
>>> d = {}  
>>> d['food'] = 'pizza'  
>>> d['quantity'] = '2'  
>>> d['flavor'] = 'bacon'  
```
### 索引
**索引** 操作，与序列的索引语法相同，只是语句中方括号内是“键”，而不再是相对位置。字典，侧重的是内容上的 **关联性**。  

字典也可以用来进行搜索，通过键索引一个字典是python中编写搜索的最快方法。
### 嵌套
例如：  
```python
>>> info = {'name':{'first': 'Lin', 'last': 'Liu'},  
           'age': 23,  
           'interests':['photography', 'reading']}  
>>> info['name']['first']  
'Liu'  
>>> info['interests'][-1]  
'reading'  
>>> info['interests'].append('travel')  
>>> info  
{'name':{'first': 'Lin', 'last': 'Liu'}, 'age': 23, 'interests':['photography', 'reading', 'travel']}   
```
可以看出python数据类型的灵活性。  
### for循环，键排序
前面提到，字典不像序列一样，它并没有从左到右的顺序。但是有时又需要强调某种顺序，该怎么办？  
在较新版本的Python中，可以直接使用sorted()函数完成：  
![sorted()](https://github.com/LiuJLin/learn_python_basic/blob/master/struc/dict_sorted.png?raw=true "github")

## 元组
元组是序列，但是类似字符串 具有 **不可变性**，不可以更改，不可以增长或缩短。  
写在 **圆括号()** 内，支持任意类型、任意嵌套以及常见的序列操作：  
```Python
>>> num = (1, 2, 3, 4)
>>> len(num)              # length
4
>>> num + (5, 6)          # 合并
(1, 2, 3, 4, 5, 6)
>>> num[0]
1
```
元组还有 **专用的调用方法** ：  
```Python
>>> num.index(4)         # 返回4所在位置
3
>>> num.count(4)         # 返回4出现的次数
1
```
**那么问题来了：  
既然它不能随意改变，都不灵活，我们为什么要用元组呢？  
正是因为它的不可变性，合适的情况下，劣势便是优势，所以说要辩证地看待问题^_^**
