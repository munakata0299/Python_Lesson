from termcolor import colored

print('test')
print(colored('test', 'red'))
print(colored('test', 'green'))

# print(help(colored))

# import は1行ずつ記述する、アルファベット順に記述する
import collections
import os
import sys

# 標準ライブラリは上に、サードパーティライブラリは1行開けて下に
import termcolor

# さらに自分たち他のチームが作ったパッケージ
import lesson_package

# 最後に自分が作ったパッケージ
import config

config.config()

print(collections.__file__)
print(termcolor.__file__)
print(lesson_package.__file__)
print(config.__file__)

print(sys.path)