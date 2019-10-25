def menu(entree = 'beef', drink = 'wine', desert = 'ice'):
    print('entree = ', entree)
    print('drink = ',drink)
    print('desert = ',desert)

# menu('beef', 'beer', 'ice')

# menu(entree='beef', desert='ice', drink='beer')

# 以下でもOK(第一引数は省略可）
# menu('beef', desert='ice', drink='beer')

#以下はNG
# menu( desert='ice', 'beef', drink='beer')

# デフォルト引数が設定されていれば以下の呼び出しでOK
menu()

#デフォルト引数が設定されていても、上書き可能
menu(entree='chicken', drink='beer')
