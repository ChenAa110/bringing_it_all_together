class Account:
    __interest_rate=0.0568

    def __init__(self,owner,amount):
        self.owner=owner
        self.__amount=amount

    def __get_info(self):
        return "{0}金钱:{1}利率:{2}".format(self.owner,self.__amount,Account.__interest_rate)

    def desc(self):
        print(self.__get_info())

account=Account('tony',80000.0)
account.desc()
# account.__get_info()

print('name:{}'.format(account.owner))


class Dog:
    def __init__(self,name,age,sex='雄性'):
        self.name=name
        self.__age=age

    def run(self):
        print("{}在跑...".format(self.name))

    def get_age(self):
        return self.__age

    def set_age(self,age):
        self.__age=age

dog=Dog('qiuqiu',3)
dog.run()
print("狗年龄:{}".format(dog.get_age()))
dog.set_age(4)
print("修改后的狗年龄:{}".format(dog.get_age()))


class Dog1:
    def __init__(self, name, age, sex='雄性'):
        self.name = name
        self.__age = age

    def run(self):
        print("{}在跑...".format(self.name))

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

dog=Dog1('qiuqiu',3)
print("狗年龄:{}".format(dog.age))
dog.age =4
print("修改后的狗年龄:{}".format(dog.age))