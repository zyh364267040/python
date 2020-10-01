import threading


g_num = 0


def task():
    for i in range(1000000):
        global g_num
        g_num += 1

    print(g_num)


if __name__ == '__main__':
    sub_thread1 = threading.Thread(target=task)
    sub_thread2 = threading.Thread(target=task)

    sub_thread1.start()
    # 线程等待，让第一个线程先执行，然后在执行第二个线程，保证数据不会有问题
    sub_thread1.join()
    sub_thread2.start()
    # print(g_num)