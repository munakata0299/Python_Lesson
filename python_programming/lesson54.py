class Person(object):
    # self をつけないとクラス変数になる
    kind = 'human'

    def __init__(self, name):
        self.name = name

    def who_are_you(self):
        print(self.name, self.kind)


a = Person('A')
a.who_are_you()
b = Person('B')
b.who_are_you()

class T(object):

    words = []

    def add_words(self, word):
        self.words.append(word)


c = T()
c.add_words('Add 1')
c.add_words('Add 2')

d = T()
d.add_words('Add 3')
d.add_words('Add 4')

# クラス変数は共有されるので、違うインスタンスで値を追加しても前に追加したものが残る
# クラス変数もあまり使わないほうがよい
# それぞれに値を保持したい場合は selfを使用する
print(c.words)




