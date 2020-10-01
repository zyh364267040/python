import threading


g_num = 0


# 创建互斥锁
# 互斥锁可以保证同一时刻只有一个线程去执行代码，能够保证全局变量的数据没有问题
# 线程等待和互斥锁都是把多任务改成单任务去执行，保证了数据的准确性，但是执行新能会下降
lock = threading.Lock()


def task():
    # 上锁
    lock.acquire()
    for i in range(1000000):
        global g_num
        g_num += 1
    print(g_num)
    # 释放锁
    lock.release()


if __name__ == '__main__':
    sub_thread1 = threading.Thread(target=task)
    sub_thread2 = threading.Thread(target=task)

    sub_thread1.start()
    sub_thread2.start()