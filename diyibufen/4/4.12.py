def e(string):
    """
    string转换成float
    :param string:
    :return:
    """
    try:
      return float(string)
    except ValueError:
        print("Could not convert the string to a float.")

c=e("55.0")
print(c)


def d1(x):
    """
    除2
    :param x:
    :return:
    """
    return x/2
def d2(x):
    """
    乘4
    :param x:
    :return:
    """
    return x*4

y=d1(4)
z=d2(y)
print(z)

# def d(a=0, b=0):
#     a = input("type is int")
#     a=int(a)
#     a /= 2
#
#     b = a
#     b *= 4
#
#     print(a,b)
#
#
# d()


def c(a, b, c, d=1, e=2):
    """
    3个必填项，2个选填
    :param a:
    :param b:
    :param c:
    :param d:
    :param e:
    :return:
    """
    print(a + b + c + d + e)


c(3, 4, 5, d=2, e=1)


def b(string):
    """
    打印字符串
    :param string:
    :return:
    """
    print(string)


b("abccc")


def a():
    """
    平方
    :return:
    """
    a = input("type a number")
    a = int(a)
    print(a ** 2)


a()
