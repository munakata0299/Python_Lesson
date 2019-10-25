a = 1
b = 1

# aとbが等しい
print(a == b)

# aとbが異なる
print(a != b)

# aがbよりも小さい
print(a < b)

# aがbよりも大きい
print(a > b)

# aがb以下である
print(a <= b)

# aがb以上である
print(a >= b)

# aもbも新であれば真
print(a > 0 and b > 0)
if a > 0:
    if b > 0:
        print('a and b are positive')

if a > 0 and b > 0:
    print('a and b are positive')

# aまたはbが真であれば真
print(a > 0 or b > 0)
if a > 0:
    print('a or b are positive')
elif b > 0:
    print('a or b are positive')

if a > 0 or b > 0:
    print('a or b are positive')