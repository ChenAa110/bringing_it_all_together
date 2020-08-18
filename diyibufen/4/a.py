x = 1
y = 2
z = 3


def f():
    x = 4
    y = 5
    z = 6
    print(x)
    print(y)
    print(z)


print(x)
f()

try:
    a = input("type a number:")
    b = input("type another:")
    a = int(a)
    b = int(b)
    print(a / b)
except (ZeroDivisionError, ValueError):
    print("Invalid input.")
