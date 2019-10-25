# リスト内包表記
t = (1, 2, 3, 4, 5)
t2 = (5, 6, 7, 8, 9)

# タプルを一つずつ取り出してリストに入れる
r = []
for i in t:
    # 偶数のみ追加
    if i % 2 == 0:
        r.append(i)

print(r)

# 別方法 (リスト内包表記) メモリ消費が少なく　スピードが速い

# r = [i for i in t]
# print(r)

r = [i for i in t if i % 2 == 0]
print(r)

r = []
for i in t:
    for j in t2:
        r.append(i * j)

print(r)

# 別方法 (リスト内包表記)
# やりすぎないこと 可読性が下がる for 1個 if 1個くらい
r = [i * j for i in t for j in t2 ]
print(r)