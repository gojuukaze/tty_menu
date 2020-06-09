<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Note</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>
<p>This repo is no longer maintained</p>
<p>My New repo support Windows, Linux, OSX at <a href="https://github.com/gojuukaze/terminal_layout/tree/master/terminal_layout/extensions/choice">terminal_layout</a></p>
  
<p>这个库不再维护，新的库支持Windows, Linux, OSX。链接 -> <a href="https://github.com/gojuukaze/terminal_layout/tree/master/terminal_layout/extensions/choice">terminal_layout</a></p>
</td>
</tr>
</tbody>
</table>


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
