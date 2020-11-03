class ask (Exception):
    def __init__(self,message):
        super().__init__(message)


i=input("请输入数字：")
n=888
try:
    result=n/int(i)
    print(result)
    print('{}除以{}等于{}'.format(n,i,result))
except ZeroDivisionError as e:
    # print("不能除以0，异常：{}".format(e))
    raise ask('不能除以0')
except ValueError as e:
    # print("输入的是无效数字，异常：{}".format(e))
    raise ask('输入的是无效数字')



