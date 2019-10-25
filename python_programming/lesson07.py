num_tuple = (10, 20)
print(num_tuple)

x, y = num_tuple
print(x, y)

x, y = 10, 20
print(x, y)
min, max = 0, 100
print(min, max)

#NG
# a, b, c, d, e, f = 'Mike', '1', '1', '1', 'e', 'f'
#OK
# a = 'Mike'
# b = '1'

i = 10
j = 20
temp = i
i = j
j = temp
print(i, j)

a = 100
b = 200
print(a, b)
a, b = b, a
print(a, b)
