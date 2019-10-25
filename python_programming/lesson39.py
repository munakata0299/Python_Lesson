# 辞書の内包表記

w = ['mon', 'tue', 'wed']
f = ['coffee', 'milk', 'water']

d = {}
for x, y in zip(w, f):
    d[x] = y

print(d)

# やり方
d = {x: y for x, y in zip(w, f)}
print(d)