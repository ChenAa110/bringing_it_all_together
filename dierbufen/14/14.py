class Rectangle():
    def __init__(self, w, l):
        self.w = w
        self.l = l

    def print_size(self):
        print("""{} by {}        
        """.format(self.w, self.l))


my_Rectangle = Rectangle(20, 100)
my_Rectangle.print_size()


class Rectangle1():
    recs = []

    def __init__(self, w, l):
        self.w = w
        self.l = l
        self.recs.append((self.w, self.l))

    def print_size(self):
        print("""{} by {}        
        """.format(self.w, self.l))


r1 = Rectangle1(10, 14)
r2 = Rectangle1(10, 21)
r3 = Rectangle1(10, 31)
print(Rectangle1.recs)


class Lion:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


Lion = Lion("Dilbert")
print(Lion)


class AlwaysPositive:
    def __init__(self, number):
        self.n = number

    def __add__(self, other):
        return abs(self.n + other.n)


a = AlwaysPositive(-20)
b = AlwaysPositive(30)
print(a + b)


class Person:
    def __init__(self):
        self.name = 'Bob'
bob=Person()
same_bob=bob
print(bob is same_bob)
another_bob=Person()
print(bob is another_bob)

x=10
if x is None:
    print("x is None")
else:
    print("x is not None")

x=None
if x is None:
    print("x is None")
else:
    print("x is not None")