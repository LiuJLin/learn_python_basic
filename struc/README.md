Python 内置类型
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

    >>>import math
    >>>math.pi
    >>>nath.sqrt(9)

    >>>import random
    >>>random.random()
    >>>random.choice([1,2,3,4])

## 序列的操作
包括 **字符串、列表、元组**
### 索引
以"China"为例：

    >>> s = "China"
    >>> len(s)      

- 索引是按照 **偏移量** 进行的，自然是从0开始的
>   >>> s[0]
    'C'

- **分片** 操作
>   >>>s[1:4]
    'hin'   
    >>> s[:]
    'China'


- 也可以通过 **负偏移量** 进行索引，例如-1则是指最后一项

    >>>s[-1]
    'a'
    >>>s[:-1]
    'Chin'

- **+ 合并**
## 不可变性
 表示一旦创建后，不能随意更改。比如，不能通过对其某一位置赋值而改变该字符串，但是可以以原来的变量名创建一个新的字符串，因为会覆盖掉原来的对象。

 **不可变**：数字、字符串、元组
 **可变**： 列表、字典
