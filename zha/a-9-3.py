class Animal:
    def speak(self):
        print('动物叫，但不知道是什么动物')

class Dog(Animal):
    def speak(self):
        print('狗叫：旺旺的叫')

class Cat(Animal):
    def speak(self):
        print('猫叫：喵喵的叫')

class Car:
    def speak(self):
        print('dududu')

def start(obj):
    obj.speak()

start(Car())
an1=Dog()
an2=Cat()
an1.speak()
an2.speak()