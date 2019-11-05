# from lesson_package.tools import utils
# 以下のようにもかけるが、推奨されていない（現在のpathを確認しなくてはならないため）
from ..tools import utils

def sing():
    return 'sing'

def cry():
    return utils.say_twice('cry')