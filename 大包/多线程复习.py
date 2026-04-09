from queue import Queue
import os
import time
from threading import Thread
import requests
# 消费者
def consumer(q):
    while True:
        res=q.get()
        print(res)
        time.sleep(1)
        print('\033[45m%s 吃 %s\033[0m' %(os.getpid(),res))

# 生产者
def producer(q):
    for i in range(10):
        time.sleep(1)
        res='包子%s' %i
        q.put(res)
        print('\033[44m%s 生产了 %s\033[0m' %(os.getpid(),res))

if __name__ == '__main__':
    q = Queue()
    # 生成者
    t1 = Thread(target=producer,args=(q,))
    # 消费者
    t2 = Thread(target=consumer,args=(q,))
    t1.start()
    t2.start()
    t1.join()
    print('主')


































