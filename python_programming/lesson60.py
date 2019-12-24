import os
import pathlib
import glob
import shutil

# ファイルやフォルダが存在するかどうか確認するには以下の通り
# print(os.path.exists('test.txt'))
# ファイルかどうか確認するためには以下の通り
# print(os.path.isfile('test.txt'))
# ディレクトリかどうか確認するためには以下の通り
# print(os.path.isdir('design'))
# ファイル名を変更する場合
# os.rename('test.txt', 'renamed.txt')
# symlink
# os.symlink('test.txt', 'symlink.txt')
# ディレクトリを作成する
# os.mkdir('test_dir')
# ディレクトリを削除する
# os.rmdir('test_dir')
# 空のファイルを作成する
# pathlib.Path('empty.txt').touch()
# ファイルを削除する
# os.remove('empty.txt')

# ディレクトリの中にディレクトリを作成し、中身を表示する
# os.mkdir('test_dir')
# os.mkdir('test_dir/test_dir2')
# print(os.listdir('test_dir'))

# ディレクトリの中にファイルを作成し、コピーする
# pathlib.Path('test_dir/test_dir2/empty.txt').touch()
# shutil.copy('test_dir/test_dir2/empty.txt',
#             'test_dir/test_dir2/empty2.txt')
# print(glob.glob('test_dir/test_dir2/*'))

# os.rmdir は中身が空の時だけ削除することができる
# フォルダの中身も含めてすべて削除したいときは以下の通りである
# shutil.rmtree('test_dir')

# 現在のファイルの位置が知りたいとき
print(os.getcwd())