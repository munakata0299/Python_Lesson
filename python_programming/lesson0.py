print('test2')

a = 10
b = a
c = b
print(c)

num = 1
#num: int = 1 とも書く事が出来る
name = 'Mike'
is_ok = True
print(num, type(num))
print(name, type(name))
print(is_ok, type(is_ok))

num = name
print(num, type(num))

name = '1'
new_num = int(name)
print(new_num, type(new_num))