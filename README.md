# trans

用 googletrans 模块 + Python 内置的 GUI 模块 tkinter 做的一个简单谷歌翻译

**Python 文件打包方式**

- 安装 pyinstaller：`pip3 install pyinstaller`
- 打包：`pyinstaller -i xx.ico -w -F xx.py`

参数：
- i：程序图标，必须是 .ico 格式
- w：加上这个参数，程序运行时就不会有命令窗口弹出
- F：打包时不会生成很多文件，后面跟要打包的 py 文件

![](https://raw.githubusercontent.com/hj1933/img/master/iimg/12.gif)

