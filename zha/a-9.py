class Dog:
    def __init__(self,name,age,sex='雌性'):
        self.name=name
        self.age=age
        self.sex=sex

    def run(self):
        print("{}在跑....".format(self.name))

    def speak(self,sound):
        print('{}在叫."{}"!'.format(self.name,sound))

d=Dog('球球',2)
d1=Dog('哈哈',1,'雄性')
d2=Dog(name='dd',sex='不是个东西',age=3)

print('我们家狗狗名叫{0},{1}岁{2}'.format(d.name,d.age,d.sex))
print('我们家狗狗名叫{0},{1}岁{2}'.format(d1.name,d1.age,d1.sex))
print('我们家狗狗名叫{0},{1}岁{2}'.format(d2.name,d2.age,d2.sex))
d.run()
d.speak('laji，垃圾')


class Account:
    interest_rate=0.0568

    def __init__(self,owner,amount):
        self.owner=owner
        self.amount=amount

    @classmethod
    def interest_by(cls,amt):
        return cls.interest_rate*amt

account=Account('Tony',800000.0)

print('账户名称:{}'.format(account.owner))
print('账户金额:{}'.format(account.amount))
print('利率:{}'.format(Account.interest_rate))
print('利率:{}'.format(account.interest_rate))
interest=Account.interest_by(12000.0)
print('计算利息：{0:.4f}'.format(interest))
interest1=account.interest_by(12000.0)
print('计算利息：{0:.4f}'.format(interest1))