# def test_func(x, l = []):
#     l.append(x)
#     return l
#空のリストを毎回生成したければ、以下のようにする
def test_func(x, l = None):
    if l is None:
        l = []
    l.append(x)
    return l


# y = [1, 2, 3]
# r = test_func(100, y)
# print(r)
#
# y = [1, 2, 3]
# r = test_func(200, y)
# print(r)

r = test_func(100)
print(r)

# Listは参照渡しなので、デフォルト引数で与えるべきではない
# 参照渡しのものはデフォルト引数として設定しない
r = test_func(100)
print(r)