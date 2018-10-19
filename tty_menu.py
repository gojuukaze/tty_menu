# -*- coding:utf-8 -*-

import os, time, sys
import tty, termios

CREL_C = '\x03'
DIRECTIION_PREFIX = '\x1b'
UP = '\x1b[A'
DOWN = '\x1b[B'
ENTER = '\r'


def show_choose(choose, pos):
    i = 0
    s = ''
    while i < len(choose):
        if i == pos:
            temp = '\033[32;1m >  '
        else:
            temp = '    '
        temp += str(choose[i]) + '\033[0m\n'
        i += 1
        s += temp
    s += '\n'
    sys.stdout.write(s)
    sys.stdout.flush()


def clear_choose(choose):
    sys.stdout.write('\033[%dA\033[K' % (len(choose) + 1,))
    sys.stdout.flush()


def get_input():
    ch = sys.stdin.read(1)
    # 方向键的开头
    if ch == DIRECTIION_PREFIX:
        ch += sys.stdin.read(2)
    return ch


def show_menu(choose, title=None, pos=0, is_first=True):
    if title and is_first:
        sys.stdout.write(title + '\n')
        sys.stdout.flush()
    if not is_first:
        clear_choose(choose)

    show_choose(choose, pos)


def tty_menu(choose, title=None):
    pos = 0

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
        show_menu(choose, title, pos, False)


if __name__ == '__main__':
    l = ['a', 'b', 'c', 'd']
    pos = tty_menu(l, title='What is your word?')
    print("Your word is %s" % (l[pos]))
