class Rectangle():
    def __init__(self, w, l):
        self.w = w
        self.l = l

    def area(self):
        return self.w * self.l


class Date:
    def __init__(self):
        self.nums = [1, 2, 3, 4, 5]

    def change_data(self, index, n):
        self.nums[index] = n


date_one = Date()
date_one.change_data(0, 101)
print(date_one.nums)

date_two = Date()
date_two.nums[0] = 100
print(date_two.nums)


class PublicPriveateExample:
    def __init__(self):
        self.public = "safe"
        self._unsafe = "unsafe"

    def public_method(self):
        pass

    def _unsafe_methond(self):
        pass


print("Hello")
print(200)
print(200.1)

print(type("Hello"))
print(type(200))
print(type(200.1))


# shapes = [trl, sql, crl]
# for a_shape in shapes:
#     if type(a_shape)=="Triangle":
#         a_shape.draw_triangle()
#     if type(a_shape) == "Square":
#         a_shape.draw_square()
#     if type(a_shape)=="Circle":
#         a_shape.draw_Circle()
#
#
# for a_shape in shapes:
#     a_shape.draw()


class shape():
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print("""{} by {}        
        """.format(self.width, self.len))


class Square(shape):
    def area(self):
        return self.width * self.len
    def print_size(self):
        print("""I am {} by {}        
        """.format(self.width, self.len))



my_Square = Square(20, 100)
my_Square.print_size()
print(my_Square.area())



class Dog():
    def __init__(self,name,breed,owner):
        self.name=name
        self.breed=breed
        self.owner=owner

class Person():
    def __init__(self,name):
        self.name=name


mick=Person("Mick Jagger")
stan=Dog("Stanley","Bulldog",mick)
print(stan.owner.name)