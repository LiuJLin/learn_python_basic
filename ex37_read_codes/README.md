Examples
======================
  [From:](http://www.pythonforbeginners.com/code-snippets-source-code/python-code-examples)
<br />

Command_line_IMDB_Scraper
---------------------------
# 准备工作：
##1. 下载
由于需要用到beautifulsoup，因此首先去下载。
  [官网](https://www.crummy.com/software/BeautifulSoup/bs4/download/4.5/)
<br />
##2. 安装
    然后解压缩到D:/python目录下，打开cmd窗口，进入到解压目录下，进入D:/python/beautifulsoup4-4.5.3/beautifulsoup4-4.5.3
    python setup.py build
    python setup.py install
    进行安装，一开始命令首部没有输入python，结果都不成功，后来尝试加上python，安装成功！
##3. 导入
    进入python，然后输入
    from bs4 import BeautifulSoup
    结果又报错：
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "D:\python\beautifulsoup4-4.5.3\beautifulsoup4-4.5.3\bs4\__init__.py", line 53
    'You are trying to run the Python 2 version of Beautiful Soup under Python 3. This will not work.'<>'You need to convert the code, either by installing it (`python setup.py install`) or by running 2to3 (`2to3 -w bs4`).'
    SyntaxError: invalid syntax
    通过错误提示发现是版本不对应造成的，因此推出python，在cmd中输入
    2to3 -w bs4
    再次尝试导入，成功！
