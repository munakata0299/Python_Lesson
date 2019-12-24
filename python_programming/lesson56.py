class Word(object):

    # __XXX__　は特殊メソッド
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return 'Word!!!!!!'

    def __len__(self):
        return len(self.text)

    def __add__(self, word):
        return self.text.lower() + word.text.lower()

    def __eq__(self, word):
        return self.text.lower() == word.text.lower()

w = Word('test')
w2 = Word('############')
# 以下の場合__str__が呼ばれる
print(w)
# 以下の場合__len__が呼ばれる
print(len(w))
# 以下の場合__add__が呼ばれる
print(w + w2)
# 以下の場合__eq__が呼ばれる
print(w == w2)
