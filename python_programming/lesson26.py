# 関数定義 def は definition（デフィニッション）
# ()  :   まるかっこ, パレンティス（parenthesis）
# []  :   かくかっこ, ブラケット（bracket)
# {}  :   なみかっこ, ブレイシス(braces)

# 'hi'と表示する関数
# def say_something():
#     print('hi')

# 文字列を返す関数
def say_something():
    s = 'hi'
    return s

result = say_something()
print(result)

# type は function
print(type(say_something))

#関数定義をしてから呼び出す

#以下のような呼び出しでもOK
# f = say_something
# f()

# 渡された引数を表示する関数
# def what_is_this(color):
#     print(color)

# 渡された引数によって値を返却する関数
def what_is_this(color):
    if color == 'red':
        return 'tomato'
    elif color == 'green':
        return 'green pepper'
    else:
        return "I don't know"

result = what_is_this('red')
print(result)
result = what_is_this('green')
print(result)
result = what_is_this('yellow')
print(result)