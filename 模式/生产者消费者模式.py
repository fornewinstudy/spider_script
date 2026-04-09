from queue import Queue
import threading
import time

def produer(q):
    """
    拼命的生产产品
    :return:
    """
    for i in range(500):
        q.put(f"商品{i}")

def consumer(q):
    """
    拼命的消耗产品
    :return:
    """
    while True:
        if q.empty():
            break
        print(q.get())
        time.sleep(0.1)

if __name__ == '__main__':
    # 仓库
    q = Queue(500)
    # 生产者
    t = threading.Thread(target=produer,args=(q,))
    t.start()
    t.join()
    # 消费者
    for i in range(10):
        t = threading.Thread(target=consumer,args=(q,))
        t.start()



























