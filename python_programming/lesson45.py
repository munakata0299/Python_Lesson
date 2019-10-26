# コマンドライン引数
import sys

# print('test')
# コマンドラインから実行する際には
# python lesson45.py args1 args2 のように指定する
# pycharm の場合には、Run/Debug Configuration から Script parametersに指定する

for i in sys.argv:
    print(i)