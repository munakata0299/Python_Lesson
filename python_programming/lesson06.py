i = [1, 2, 3, 4, 5]
j = i
j[0] = 100
print('j=', j)
print('i=', i)

x = [1, 2, 3, 4, 5]
#y = x.copy()
y = x[:] #上と同じ
y[0] = 100
print('y=', y)
print('x=', x)

X = 20
Y = X
Y = 5
print(id(Y))
print(id(X))
print(Y)
print(X)

X = ['a', 'b']
Y = X
print(id(Y))
print(id(X))
print(Y)
print(X)