import threading
import time

value=[]

def thread_body():
    print('t1子线程开始。。。')
    for n in range(2):
        print('t1子线程执行。。。')
        value.append(n)
        time.sleep(2)
    print('t1子线程结束。')

print('主线程开始执行...')

t1=threading.Thread(target=thread_body())
t1.start()
# t1.join()

print('value={0}'.format(value))
print('主线程继续执行...')