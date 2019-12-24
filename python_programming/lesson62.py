import glob
import zipfile

with zipfile.ZipFile('test.zip', 'w')as z:
    # z.write('test_dir')
    # z.write('test_dir/test.txt')
    # globを使えば以下のように書くことができる
    for f in glob.glob('test_dir/**', recursive=True):
        print(f)
        z.write(f)
# Macの場合、zipファイルを展開するときには以下の通り
# unzip ファイル名.zip -d ディレクトリ名

# zipファイルの読み込み
with zipfile.ZipFile('test.zip', 'r') as z:
    # すべて展開する時は以下の通り
    # z.extractall('zzz2')
    # 展開せずに読みたい時は以下の通り
    with z.open('test_dir/test.txt') as f:
        print(f.read())