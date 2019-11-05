# import lesson_package.utils
# from lesson_package import utils
# 以下のように書くと関数のみimportできるが、どこから持ってきた関数なのか分からないのでNG
# from lesson_package.utils import say_twice
# もしも関数のみのimportだと 関数名が被る可能性がある

# モジュール名が長い場合は短くできるが、あまり短すぎると分からなくなるのでNG

# from lesson_package.talk import humans
# from lesson_package.talk import animal
# 以下のように書くと、__init__に書いてあるものが全て読み込まれるが、どんなものが読み込まれるか分からないので推奨されていない
# from lesson_package.talk import *

# print(animal.sing())
# print(animal.cry())


# r = lesson_package.utils.say_twice('hello')
# r = utils.say_twice('hello')
# r = say_twice('hello')
# r = u.say_twice('hello')
# print(r)

# print(human.sing())
# print(human.cry())

# 古いパッケージがあれば使用して、ない場合には新しいパッケージをimportする際には、ImportErrorが使える
try:
    from lesson_package import utils
except ImportError:
    from lesson_package.tools import utils

print(utils.say_twice('word'))