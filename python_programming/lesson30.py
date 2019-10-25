# def say_something(word, word2, word3):
#     print(word)
#     print(word2)
#     print(word3)

# *(アスタリスク）を使用すると複数まとめて引数を渡せる
def say_something(word, *args):
    print('word = ', word)
    for arg in args:
        print(arg)

# t = ('Mike', 'Nancy')
# say_something('Hi!', *t)

say_something('Hi!', 'Mike', 'Nancy')