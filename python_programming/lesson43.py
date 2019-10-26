# 例外処理
l = [1, 2, 3]
i = 5
# リスト削除
# del l

try:
    # l[i]
    () + l
except IndexError as ex:
    print("Don't woory {}".format(ex))
except NameError as ex:
    print(ex)
#Pythonでは全てのExceptionをキャッチして何のExceptionか分からないまま進むのはNG
except Exception as ex:
    print('other:{}'.format(ex))
else:
    print('done')
finally:
    print('clean up')

# elseは何も問題なく抜けた場合のみ実行される
# finallyは例外をキャッチしてもしなくても必ず実行される