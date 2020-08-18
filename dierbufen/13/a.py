class Rectangle():
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_perimeter(self):
        return self.width * 2 + self.length * 2


class Square():
    def __init__(self, s1):
        self.s1 = s1

    def calculate_perimeter(self):
        return self.s1 * 4


rectangle = Rectangle(20, 30)
square = Square(10)

print(rectangle.calculate_perimeter())
print(square.calculate_perimeter())


class Square():
    def __init__(self, s1):
        self.s1 = s1

    def calculate_perimeter(self):
        return self.s1 * 4

    def change_size(self, new_size):
        self.s1 += new_size


square = Square(10)
print(square.s1)
square.change_size(2)
print(square.s1)


# 创建一个叫Shape的类。在其中定义一个叫what_am_i的方法，
# 被调用时打印"Iam s shape"。调整上个挑战中的Square和Rectangle类，使其继承Shape类，然后创建Sqaure和Rectangle对象，并在二者上调用新方法。

class Shape():
    def __init__(self):
        pass

    def what_am_i(self):
        print("Iam s shape")


class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_perimeter(self):
        return self.width * 2 + self.length * 2


class Square(Shape):
    def __init__(self, s1):
        self.s1 = s1

    def calculate_perimeter(self):
        return self.s1 * 4


rectangle = Rectangle(20, 30)
square = Square(10)
rectangle.what_am_i()
square.what_am_i()



class Horse():
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner


class Rider():
    def __init__(self, name):
        self.name = name

rider=Rider("Jack")
horse=Horse("Rose",rider)
print(horse.owner.name)