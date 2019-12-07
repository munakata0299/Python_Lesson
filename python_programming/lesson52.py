import abc


class Person(metaclass=abc.ABCMeta):
    def __init__(self, age=1):
        self.age = age

    # drive メソッドをPersonクラスで定義しないで
    # 子クラスで実装するとしたときに実装し忘れてしまう可能性がある
    # 必ず実装してほしいメソッドがある場合には抽象クラスを使用する
    # Pythonではあまり推奨されていない
    @abc.abstractmethod
    def drive(self):
        pass


class Baby(Person):
    def __init__(self, age=1):
        if age < 18:
            super().__init__(age)
        else:
            raise ValueError

    def drive(self):
        raise  Exception('No drive')


class Adult(Person):
    def __init__(self, age=18):
        if age >= 18:
            super().__init__(age)
        else:
            raise ValueError

    def drive(self):
        print('ok')


baby = Baby()
adult = Adult()

class Car(object):
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('run')

    def ride(self, person):
        person.drive()


class ToyotaCar(Car):
    def run(self):
        print('fast')


class TeslaCar(Car):
    def __init__(self, model='Model S',
                 enable_auto_run=False,
                 passwd='123'):
        # self.model = model
        super().__init__(model)
        #  __(アンダースコア２個）をつけるとクラスの中からはアクセスできるが
        # クラスの外からはアクセスできなくなる
        self.__enable_auto_run = enable_auto_run
        self.passwd = passwd

    @property
    def enable_auto_run(self):
        return self.__enable_auto_run

    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        if self.passwd == '456':
            self.__enable_auto_run = is_enable
        else:
            raise ValueError

    def run(self):
        print('super fast')

    def auto_run(self):
        print('auto run')


car = Car()
car.ride(adult)
car.run()

print('###############')
toyota_car = ToyotaCar('Lexus')
print(toyota_car.model)
toyota_car.run()
print('###############')
tesla_car = TeslaCar('Model S', passwd='456')
print(tesla_car.model)
tesla_car.run()
tesla_car.auto_run()
tesla_car.enable_auto_run = True
# tesla_car.__enable_auto_run = True としてしまうと
# 後からデータ構造体として定義されてしまってバグの原因となることがあるので
# 便利だけど注意すること
print(tesla_car.enable_auto_run)


class T(object):
    pass


t = T()
t.name = 'Mike'
print (t.name)