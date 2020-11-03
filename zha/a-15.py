import threading
import time

t = threading.current_thread()
print(t.name)

print(threading.active_count())

t = threading.main_thread()
print(t.name)


def thred_body():
    t = threading.current_thread()
    for n in range(5):
        print('第{0}次执行程序{1}'.format(n, t.name))
        time.sleep(1)
    print('线程第{0}执行完成'.format( t.name))


t1 = threading.Thread(target=thred_body)

t2 = threading.Thread(target=thred_body, name='MyThred')
t1.start()
t2.start()


class SmallThred(threading.Thread):
    def __init__(self,name=None):
        super().__init__(name=name)

    def run(self) :
        t=threading.current_thread()
        for n in range(5):
            print('第{0}次执行程序{1}'.format(n, t.name))
            time.sleep(2)
        print('线程第{0}执行完成'.format( t.name))


t1=SmallThred()
t2=SmallThred(name='ohMythread')
t1.start()
t2.start()