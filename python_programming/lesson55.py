# 外においておくことも可能だが、関連があるの絵であれば、クラスの中で定義する
def about(year):
    print('about human {}'.format(year))


class Person(object):

    kind = 'human'

    def __init__(self):
        self.x = 100

    @classmethod
    def what_is_your_kind(cls):
        return cls.kind

    @staticmethod
    def about(year):
        print('about human {}'.format(year))


# 変数に代入する際にパレンティスの括弧()がついているとオブジェクト（インスタンス）が生成される
a = Person()
# オブジェクトが生成されているので self.xで値を取得することができる
print(a.x)
# クラス変数にもアクセスすることができる
print(a.kind)
# オブジェクトが生成されていれば、インスタンスメソッドを呼ぶことができる
print(a.what_is_your_kind())

# 変数に代入する際にパレンティスの括弧()がついていないとクラスを指し示すだけ
b = Person
# こちらはオブジェクトが生成されているないので、以下のように書いても値が取得できない
# print(b) //NG インスタンス変数にはアクセスできない
# オブジェクトが生成されていなくても、クラス変数にはアクセスすることができる
print(b.kind)
# オブジェクトが生成されていないとインスタンスメソッドを呼ぶことができないが、
# クラスメソッドであれば呼び出すことができる
print(b.what_is_your_kind())

# クラス変数やクラスメソッドには以下のようにアクセスすることも可能
print(Person.kind)
print(Person.what_is_your_kind())

# スタティックメソッドは以下のように呼びだ出すことができる
Person.about(1999)