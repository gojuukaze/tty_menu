tty_menu
==========================

This project is used to create menu command-line
一个快速创建命令行菜单的工具

![demo](https://raw.githubusercontent.com/gojuukaze/tty_menu/master/ex.gif)

Install
----------------------

```bash
pip install tty_menu
```
Example
----------------------
```python

from tty_menu import tty_menu

l = ['a', 'b', 'c']
pos = tty_menu(l, "What is your word?")

print("Your word is %s" % (l[pos]))
```

chang_log
----------------

* 1.0.2 : rm log (移除无用log)

* 1.0.3 : change way (更改显示菜单的方式，不在需要清屏了)
