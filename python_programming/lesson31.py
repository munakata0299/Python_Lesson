# def menu(entree = 'beef', drink = 'wine'):
#     print(entree, drink)

# keyword arguments
# def menu(**kwargs):
#     # print(kwargs)
#     for k, v in kwargs.items():
#         print(k, v)

# menu(entree = 'beef', drink = 'coffee')

# d = {
#     'entree': 'beef',
#     'drink': 'ice coffee',
#     'desert': 'ice',
# }


# menu(**d)

# food:普通の引数
# args:複数の引数（タプル）
# kwargs:複数の引数（辞書）
# args と kwargsの順番は逆ではいけない

def menu(food, *args, **kwargs):
    print(food)
    print(args)
    print(kwargs)

menu('banana', 'apple', 'orange', entree = 'beef', drink = 'coffee')