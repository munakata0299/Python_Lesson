count = 0

#途中 breskで抜けた場合にはelseは実行されない
while count < 5:
    if count == 1:
        break
    print(count)
    count += 1
else:
    print('done')