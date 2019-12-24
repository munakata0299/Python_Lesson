# Pythonがioバッファ上に作ってくれる一時ファイル　処理が終わったら消える
import tempfile

# 一時ファイルを作成して使用する方法は以下の通り
with tempfile.TemporaryFile(mode='w+') as t:
    t.write('hello')
    t.seek(0)
    print(t.read())

#　一時ファイルを残したい場合には以下の通り
with tempfile.NamedTemporaryFile(delete=False) as t:
    print(t.name)
    with open(t.name, 'w+') as f:
        f.write('test\n')
        f.seek(0)
        print(f.read())

# ウィンドウズの場合は以下の場所に作成される
# C:\Users\user\AppData\Local\Temp\tmp・・・

# Mac = cat Windows = type

#　一時フォルダを残したい場合には以下の通り
with tempfile.TemporaryDirectory() as td:
    print(td)

temp_dir = tempfile.mkdtemp()
print(temp_dir)