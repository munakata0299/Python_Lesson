some_list = [1, 2, 3, 4, 5]

# i = 0
# while i < len(some_list):
#     print(some_list[i])
#     i += 1

# 反復処理イテレータ inキーワードを用いる
# for i in some_list:
#     print(i)

# 一文字ずつ取り出して出力する
# for s in 'abcde':
#     print(s)

for word in ['My', 'name',  'is', 'Mike']:
    # if word == 'name':
    #     break
    if word == 'name':
        continue
    print(word)