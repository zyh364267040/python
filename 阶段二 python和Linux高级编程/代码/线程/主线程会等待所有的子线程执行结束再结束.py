import threading
import time


def task():
    while True:
        print("任务执行中...")
        time.sleep(0.5)


if __name__ == '__main__':
    sub_thread = threading.Thread(target=task, daemon=True)
    # 把子线程设置成为守护主线程，使用setDaemon(True),或设置参数daemon为True,Thread(daemon=True)
    # sub_thread.setDaemon(True)
    sub_thread.start()

    time.sleep(1)
    print("执行完毕")
