import threading
import time


g_list = []


def add_data():
    for i in range(3):
        g_list.append(i)
        time.sleep(0.4)
    print(f"添加完列表是:{g_list}")


def read_data():
    print(f"读取的列表是:{g_list}")


if __name__ == '__main__':
    add_thread = threading.Thread(target=add_data)
    read_thread = threading.Thread(target=read_data)

    add_thread.start()
    # 让当前线程（主线程）等待添加数据的子线程执行完成以后再继续执行
    add_thread.join()
    read_thread.start()
