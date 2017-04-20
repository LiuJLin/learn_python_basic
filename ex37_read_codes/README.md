# Examples
  [From:](http://www.pythonforbeginners.com/code-snippets-source-code/python-code-examples)
<br />

## 1. Command_line_IMDB_Scraper
---------------------------
### 准备工作：
#### 下载
由于需要用到beautifulsoup，因此首先去下载。<br />
  [官网](https://www.crummy.com/software/BeautifulSoup/bs4/download/4.5/)
<br />
#### 安装
然后解压缩到D:/python目录下，打开cmd窗口，进入到解压目录下，进入D:/python/beautifulsoup4-4.5.3/beautifulsoup4-4.5.3
    python setup.py build
    python setup.py install
进行安装，一开始命令首部没有输入python，结果都不成功，后来尝试加上python，安装成功！
#### 导入
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
### Tips：
1. python3不再有urllib2，取而代之的是urllib.request，因此将在Python2中使用urllib2的全部替代为urllib.request即可
2. from BeautifulSoup import BeautifulSoup 总是会出错，替换为from bs4 import BeautifulSoup即可
### error:  尚未解决 :(
    "Traceback (most recent call last):
    File ".\Command_line_IMDB_Scraper.py", line 29, in <module>
    response = json.load(urllib.request.urlopen(request))
    File "D:\ProgramData\Anaconda3\lib\json\__init__.py", line 299, in load parse_constant=parse_constant, object_pairs_hook=object_pairs_hook, **kw)
    File "D:\ProgramData\Anaconda3\lib\json\__init__.py", line 354, in loads
    return _default_decoder.decode(s)
    File "D:\ProgramData\Anaconda3\lib\json\decoder.py", line 339, in decode obj, end = self.raw_decode(s, idx=_w(s, 0).end())
    File "D:\ProgramData\Anaconda3\lib\json\decoder.py", line 357, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)"
