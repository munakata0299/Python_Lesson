# ファイルの生成について
# test.txt を作成する 'w'書き込みモード 'a'追記モード 'r'読み込みモード
# f = open('test.txt', 'w')
# f.write('Test\n')
# print('I am print', file=f)
# print('My', 'name', 'is', 'Mike', sep='#', end='!', file=f)
# f.close()

# ファイルは必ずクローズしなければならないが忘れてしまうことがある
# 必ずファイルを閉じる場合は以下のように withステートメントを使用する

s = """\
AAA
BBB
CCC
DDD
"""

# with open('test.txt', 'w') as f:
#     f.write(s)

# with open('test.txt', 'r') as f:
    # print(f.read())
    # while True:
        # chunk = 2   # chunk使いどころはネットワークでパケットを取得するときなど
        # # line = f.readline()
        # line = f.read(chunk) # chunkで指定した文字ずつ出力
        # # print(line, end='') //改行しないで出力する場合
        # print(line)
        # if not line:
        #     break
    # print(f.tell())
    # print(f.read(1))
    # f.seek(5)
    # print(f.read(1))
    # f.seek(14)
    # print(f.read(1))
    # f.seek(15)
    # print(f.read(1))
    # f.seek(5)
    # print(f.read(1))

# 読み書きする場合(書きが最初なので、新しいファイルが作られてしまう。上書きされてしまう）
# with open('test.txt', 'w+') as f:
#     f.write(s)
#     f.seek(0)
#     print(f.read())

# 読み書きする場合（読み優先）事前にファイルがないとエラーになる
with open('test.txt', 'r+') as f:
    print(f.read())
    f.seek(0)
    f.write(s)



