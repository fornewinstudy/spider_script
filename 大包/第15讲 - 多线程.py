# 简单实现多线程
# import time
# import threading # 线程模块

# 单线程效果
# def sing():
#     for i in range(3):
#         print("正在唱歌...%d"%i)
#         time.sleep(1)
#
# def dance():
#     for i in range(3):
#         print("正在跳舞...%d"%i)
#         time.sleep(1)

# sing()
# dance()

# 多线程效果
# def sing():
#     for i in range(3):
#         print("正在唱歌...%d"%i)
#         time.sleep(1)
#
# def dance():
#     for i in range(3):
#         print("正在跳舞...%d"%i)
#         time.sleep(1)
#
# if __name__ == '__main__':
#     # sing()
#     # dance()
#     # 实例化线程类
#     te = threading.Thread(target=sing)
#     te2 = threading.Thread(target=dance)
#     # 执行线程，用start()方法
#     te.start()
#     te2.start()


# 线程阻塞和守护线程
# import time
# import threading
# import random
#
# def fm(n):
#     print(f"{n}号演员在吃饭")
#     time.sleep(random.random()*3)
#     print(f'{n}号演员吃完了')
#
# if __name__ == '__main__':
#     # # 先定义一个列表
#     # lst = []
#     # for i in range(5):
#     #     # target=fm在这个后面加()等于调用，所以不能加
#     #     # args=(i,) 添加参数，后面必须是元组
#     #     t = threading.Thread(target=fm,args=(i,))
#     #     lst.append(t)
#     #     t.start()
#     # for a in lst:
#     #     # 用join阻塞线程
#     #     a.join()
#     #
#     # print("时间到了，集合开始表演了！！！")
#
#     # 先定义一个列表
#     lst = []
#     for i in range(5):
#         t = threading.Thread(target=fm, args=(i,))
#         # 设置守护线程
#         # 当主线程执行完毕，不管子线程有没有执行完毕都会停止执行
#         # 守护线程一定要设置到线程执行的前面，不然报错
#         t.setDaemon(True)
#         t.start()
#     time.sleep(1.5)
#     print("时间到了，集合开始表演了！！！")


# 查看线程数量和创建时间
# import time
# import threading
# import random
#
# def fn(n):
#     print(f"我是一个线程————{n}")
#     time.sleep(1)
#
#
# if __name__ == '__main__':
#     for i in range(5):
#         t = threading.Thread(target=fn, args=(i,))
#         t.start()
#         # 线程创建的时间是在执行start之后才会执行
#         print(len(threading.enumerate()))
#         break
#     # threading.enumerate() 查看线程的数量
    # print(len(threading.enumerate()))


# 面向对象的写法
# import time
# import threading
# import random
#
# class Threading(threading.Thread):
#     def __init__(self, n):
#         # 继承
#         super().__init__()
#         self.n = n
#     def run(self):
#         print('做烧饼中')
#         time.sleep(1)
#         print(f'{self.n}号烧饼做完了')
#
# if __name__ == '__main__':
#     for n in range(3):
#         t = Threading(n)
#         t.start()


# 资源竞争和互斥锁
# import threading
# import time
# import random
# lock = threading.Lock()
#
# n = 0
# def teat1():
#     # 声明全局变量
#     global n
#     for i in range(10000000):
#         # 加锁
#         lock.acquire()
#         n += 1
#         # 解锁
#         lock.release()
#
# def teat2():
#     global n
#     for i in range(10000000):
#         lock.acquire()
#         n += 1
#         lock.release()
#
# if __name__ == '__main__':
#     t = threading.Thread(target=teat1)
#     t2 = threading.Thread(target=teat2)
#     t.start()
#     t2.start()
#     t.join()
#     t2.join()
#     print(n)


# 队列的常见的操作
from queue import Queue
# 实例化队列
# q = Queue(3)
# 判断队列是否为空
# print(q.empty())  # True
# 给队列加数据
# q.put(1)
# q.put(2)
# q.put(3)
# 看队列大小
# print(q.qsize())
# 判断队列是否满了
# print(q.full()) # True
# 拿数据
# s = q.get()
# print(s)
# s = q.get()
# print(s)
# s = q.get()
# print(s)
# # 当数据超出范围，不会报错而会一直执行
# s = q.get()
# print(s)

# 初始化Queue(maxsize)：创建一个先进先出的队列。
# empty()：判断队列是否为空。
# full()：判断队列是否满了。
# get()：从队列中取最后一个数据。
# put()：将一个数据放到队列中。
# qsize(): 看队列大小







