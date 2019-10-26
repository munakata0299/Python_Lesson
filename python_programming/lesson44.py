# 独自例外処理の作成
# 以下は強制的にエラーを発生させる方法
# raise IndexError('test error')

# 以下では Exception classを継承してclassを作成する
class UppercaseError(Exception):
    pass


def check():
    words = ['APPLE', 'orange', 'banana']
    for word in words:
        if word.isupper():
            raise UppercaseError(word)

try:
    check()
except UppercaseError as exc:
    print('This is my fault. Go next')