s = "My name is Mike. Hi Mike."
print(s)
is_start = s.startswith('My')
print(is_start)
is_start = s.startswith('X')
print(is_start)

print("################")

print(s.find('Mike')) #最初に見つかったindex
print(s.rfind('Mike')) #後ろからで最初に見つかったindex
print(s.count('Mike')) #含まれる単語の個数
print(s.capitalize()) #先頭の文字だけ大文字に変更
print(s.title()) #全ての単語の先頭を大文字に変更
print(s.upper()) #全て大文字に変更
print(s.lower()) #全て小文字に変更
print(s.replace('Mike', 'Nancy')) #文字列の置き換え



