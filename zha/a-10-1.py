i=input('请输入数字：')
n=888
try:
    result=n/int(i)
    print(result)
    print('{}除以{}等于{}'.format(n,i,result))
except (ZeroDivisionError,ValueError) as e:
    print("异常发生：{}".format(e))