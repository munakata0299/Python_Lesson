# ジェネレータ
# l = ['Good morning', 'Good afternoon','Good night']
#
# for i in l:
#     print(i)
#
# print('#################')

def counter(num=10):
    for _ in range(num):
        yield 'run'


#yield イールド 生成する
def greeting():
    yield 'Good morning'
    # for i in range(1000000):
    #     print(i)
    yield 'Good afternoon'
    # for i in range(1000000):
    #     print(i)
    yield 'Good night'

# for g in greeting():
#     print(g)

g = greeting()
c = counter()

print(next(g))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

# print("@@@@@")

print(next(g))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
# print("@@@@@")

print(next(g))