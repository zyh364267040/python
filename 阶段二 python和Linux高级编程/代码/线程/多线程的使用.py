import threading
import time


def dance():
    # 获取当前线程
    current_thread = threading.current_thread()
    print("dance:", current_thread)

    for i in range(3):
        print("跳舞中...")
        time.sleep(0.4)


def sing():
    # 获取当前线程
    current_thread = threading.current_thread()
    print("sing:", current_thread)

    for i in range(3):
        print("唱歌中...")
        time.sleep(0.4)


if __name__ == '__main__':
    # 获取当前线程
    current_thread = threading.current_thread()
    print("main:", current_thread)

    sub_dance = threading.Thread(target=dance)
    sub_sing = threading.Thread(target=sing)

    sub_dance.start()
    sub_sing.start()