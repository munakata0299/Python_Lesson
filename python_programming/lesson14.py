y = (1, 2, 3)
x = 1

if x in y:
    print('in')

if 100 not in y:
    print('not in')

a = 1
b = 2

#NG
if not a == b:
    print('Not equal')

#Good
if a != b:
    print('Not equal')

is_ok = True

#notキーワードはboolの時に使うのが望ましい
if not is_ok:
    print(('hello'))

