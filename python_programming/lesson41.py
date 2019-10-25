# ジェネレータ内包表記
def g():
    for i in range(10):
        yield i

g = g()
print(type(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))


#ジェネレータの内包表記
g = (i for i in range(10) if i % 2 == 0)
print(type(g))
print(g)

#タプルの場合は tupleとつける必要がある
g = tuple(i for i in range(10))
print(type(g))
print(g)