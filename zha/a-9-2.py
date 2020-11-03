class Animal:
    def __init__(self, name):
        self.name = name

    def show_info(self):
        return "动物名字：{}".format(self.name)

    def move(self):
        print("动一动.....")


class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age


cat = Cat('Tom', 2)
cat.move()
print(cat.show_info())


class Horse:
    def __init__(self, name):
        self.name = name

    def run(self):
        print("horse run...")

    def show_info(self):
        return "horse name is :{}".format(self.name)


class Donkey:
    def __init__(self, name):
        self.name = name

    def run(self):
        print("Donkey run...")

    def roll(self):
        print("Donkey roll...")

    def show_info(self):
        return "Donkey name is :{}".format(self.name)


class Mule(Horse, Donkey):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def show_info(self):
        return "Mule name is :{},age is {}".format(self.name, self.age)


m = Mule('libao', 3)
m.run()
m.roll()
print(m.show_info())
