class Person(object):
    def talk(self):
        print('talk')

    def run(self):
        print('person run')


class Car(object):
    def run(self):
        print('car run')


# 多重継承はできるが、あまりしないような設計をしたほうが良い
# 多重継承した親クラスに同じメソッドがあると最初に継承したクラスのメソッドのほうが優先して呼ばれる
class PersonCarRobot(Person, Car):
    def fly(self):
        print('fly')


person_car_robot = PersonCarRobot()
person_car_robot.talk()
person_car_robot.run()
person_car_robot.fly()

