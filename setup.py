# -*- coding:utf-8 -*-

__author__ = 'gojuukaze'

from setuptools import setup, find_packages

setup(
    name="tty_menu",
    version="1.0.3",
    description="terminal menu(一个命令行上下选择菜单)",
    long_description=open("README.rst").read(),
    license="GUN V3.0",

    url="https://github.com/gojuukaze/tty_menu",
    author="gojuukaze",
    author_email="i@ikaze.uu.me",

    py_modules=['tty_menu'],
    include_package_data=True,
    platforms="OSX, Linux",
    install_requires=[],

    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: MacOS',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Development Status :: 5 - Production/Stable',
    ],

)
