"""
Test Test ###############
"""

# 名前空間とスコープ

animal = 'cat'

def f():
    # print(animal)
    # animal = 'dog'
    global animal
    animal ='dog'
    print('local', locals())

def f2():
    """Test func doc"""
    print(f2.__name__)
    print(f2.__doc__)


f()
f2()
# print('global：', animal)
print('global：', __name__)
print('global：', globals())