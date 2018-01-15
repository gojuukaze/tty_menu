# -*- coding:utf-8 -*-

import os, time, sys
import tty, termios

CREL_C = '\x03'
DIRECTIION_PREFIX = '\x1b'
UP = '\x1b[A'
DOWN = '\x1b[B'
ENTER = '\r'


def show_choose(choose, start_line, pos):
    i = 0
    s = ''
    while i < len(choose):
        if i == pos:
            temp = '\033[%s;0H\033[32;1m > ' % (start_line + i)
        else:
            temp = '\033[%s;0H\033[0m   ' % (start_line + i)
        temp += str(choose[i])
        i += 1
        s += temp
    s += '\n'
    with open('aa.log', 'w')as f:
        f.write(s)
    sys.stdout.write(s)
    sys.stdout.flush()


def get_input():
    ch = sys.stdin.read(1)
    # 方向键的开头
    if ch == DIRECTIION_PREFIX:
        ch += sys.stdin.read(2)
    return ch


def show_menu(choose, title=None, pos=0):
    start_line = 0 if not title else 2
    if title:
        sys.stdout.write('\033[0;0H\033[0m' + title)
        sys.stdout.flush()

    show_choose(choose, start_line, pos)


def tty_menu(choose, title=None):
    pos = 0

    os.system('clear')
    show_menu(choose, title, pos)

    while True:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            key = get_input()
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

        if key == CREL_C:
            break
        elif key == ENTER:
            return pos
        elif key == UP:
            pos -= 1
        elif key == DOWN:
            pos += 1

        if pos < 0:
            pos = len(choose) - 1
        elif pos >= len(choose):
            pos = 0

        show_menu(choose, title, pos)
