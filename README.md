# learn_python_basic
==============================
通过https://learnpythonthehardway.org/ 从零学习


Notes
-----------------------
##  ex25.py
    原名为25ex.py，运行时报错为语法错误，于是将其改为ex25.py，因此命名时首字母应为字母。但是不     
    明白为什么前面的其他程序可以正常运行

##  ex35.py
![Map of the game](https://github.com/LiuJLin/learn_python_basic/blob/master/MakeChoice_ex35.png?raw=true)    

##  ex36.py
###  Tips of if-statements
    1. 每个if 都配有一个 else
    2. 如果这个else由于没有实质意义而本应从不运行，那么你应该在该else下使用一个die函数，打印出错误提示并die（结束程序运行），类似于上个例子中的dead函数。
    3. 不要使用if-statements嵌套两层以上，尽量不要嵌套，而仅用一层

### Tips of Loops
    1. 在python中，仅将while-loop应用于无限循环。
    2. 在其它所有循环情况下使用for-loop，尤其是有一个确定的或限定的范围需要遍历时。

### Tips for debugging
    1. 不要使用调试器。调试器就像是对一个病人进行全身检查。你无法得到详细且有用的信息。
    2. 最好的调试方法是使用print来打印出程序中某处变量的值，从而来判断是否出错。
    3. 确定你的部分程序确实可以正常运行。在你运行之前不要写大量的代码，写一点，运行一点，修改一点。
