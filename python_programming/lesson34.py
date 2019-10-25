# クロージャー（後から実行したいときに使う？）
# 最初に引数を設定して、後々用途に応じて使い分ける時に使う

# def outer(a, b):
#
#     def inner():
#         return a + b
#
#     return inner

# 以下のように書くとinnerのアドレスが返ってくる
# print(outer(1, 2))

# print('#####')
#
# f = outer(1, 2)
# r = f()
# print(r)


def circle_area_func(pi):
    def circle_area(radius):
        return pi * radius * radius

    return circle_area

cal1 = circle_area_func(3.14)
cal2 = circle_area_func(3.141592)

print(cal1(10))
print(cal2(10))