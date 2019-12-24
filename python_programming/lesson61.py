# tarfile はMacやLinuxで使用する圧縮ファイル
import tarfile
# import os
# import pathlib


# os.mkdir('test_dir')
# os.mkdir('test_dir/sub_dir')
# pathlib.Path('test_dir/test.txt').touch()
# pathlib.Path('test_dir/sub_dir/sub_test.txt').touch()

# tar = ひとまとめ　gz = 圧縮
with tarfile.open('test.tar.gz', 'w:gz') as tr:
    tr.add('test_dir')

# コマンドでtarファイルを展開する際には、 tar zxvf ファイル名 -C 展開場所

# Pythonのコードで展開する場合
with tarfile.open('test.tar.gz', 'r:gz') as tr:
    # 展開する場合は以下の通り
    # tr.extractall(path='test_tar')
    # 展開しないで中身を見る場合は以下の通り
    with tr.extractfile('test_dir/sub_dir/sub_test.txt') as f:
        print(f.read())