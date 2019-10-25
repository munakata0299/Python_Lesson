my_friends = {'A', 'C', 'D'}
A_friends = {'B', 'D', 'E', 'F'}

# 自分とAさんの共通の友達
print(my_friends & A_friends)

# 買ったフルーツのリスト
f = ['apple', 'banana', 'apple', 'banana']

# 重複削除
kind = set(f)
print(kind)

# コメントについて
print('XXXXX')
# test
"""
複数行のコメント
複数行のコメント
複数行のコメント
複数行のコメント
複数行のコメント
"""
print('XXXXX')

#Apple price
some_value = 100

#コメントは右じゃなくて上に書く（暗黙のルール）

#1行が長くなる時はバックスラッシュをつける
s = 'aaaaaaaaaaaaaa'\
    + 'bbbbbbbbbbb'
print(s)

x = 1 + 1 + 1 + 1 + 1 + 1 \
    + 1 + 1 + 1 + 1 + 1 + 1
print(x)

#バックスラッシュが嫌な場合は（）でもOK
x = (1 + 1 + 1 + 1 + 1 + 1
    + 1 + 1 + 1 + 1 + 1 + 1)
print(x)

#Pythonでは80文字を超える場合は次の行へ