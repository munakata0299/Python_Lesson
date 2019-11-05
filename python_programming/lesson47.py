# 組み込み関数
import builtins

builtins.print('')
print(globals())

ranking = {
    'A': 100,
    'B': 85,
    'C': 95,
}

# for key in ranking:
#     print(key)

print(sorted(ranking, key=ranking.get, reverse=True))