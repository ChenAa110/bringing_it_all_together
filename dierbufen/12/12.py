class Orange:
    a = 0

    # def increment(self):
    #     global a
    #     a += 1

    def __init__(self, w, c):
        self.weight = w
        self.color = c
        print("Create!")


orl = Orange(10, "dark orange")
print(orl)
print(orl.weight)

orl.weight = 100
print(orl.weight)


class Rectamgle():
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def area(self):
        return self.width * self.len

    def change_size(self, w, l):
        self.width = w
        self.len = l

rectamgle=Rectamgle(10,20)
print(rectamgle.area())
rectamgle.change_size(20,30)
print(rectamgle.area())