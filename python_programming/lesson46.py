# import lesson_package.utils
# from lesson_package import utils
# 以下のように書くと関数のみimportできるが、どこから持ってきた関数なのか分からないのでNG
# from lesson_package.utils import say_twice
# もしも関数のみのimportだと 関数名が被る可能性がある

# モジュール名が長い場合は短くできるが、あまり短すぎると分からなくなるのでNG
from lesson_package import utils as u


# r = lesson_package.utils.say_twice('hello')
# r = utils.say_twice('hello')
# r = say_twice('hello')
r = u.say_twice('hello')
print(r)