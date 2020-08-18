class Square():
    square_list = []

    def __init__(self, s1):
        self.s1 = s1
        self.square_list.append(self)

    def calculate_perimeter(self):
        return self.s1 * 4


a_square = Square(29)
print(a_square.square_list)
print(Square.square_list)


# 修改Square类，要求在打印Square对象时，打印的信息为图形4个边的长度。例如，假设创建一个Square(29)，则应打印29 by 29 by 29 by 29。

class Square1():
    square_list = []

    def __init__(self, s1):
        self.s1 = s1
        self.square_list.append(self)

    def print_size(self):
        return ("""{} by {}  by {} by {}       
        """.format(self.s1, self.s1, self.s1, self.s1))

    def calculate_perimeter(self):
        return self.s1 * 4


a_square = Square1(29)
print(a_square.print_size())


# 编写一个函数，接受两个对象作为参数，如果为相同的对象则返回True，反之返回False

class ft():
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def cc(self):
       if self.a==self.b:
           return True
       else:
           return False
a=ft(2,2)
print(a.cc())



def compare(a,b):
    return a is b

print(compare(1,1))