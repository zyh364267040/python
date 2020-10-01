# 当子进程进入无线循环，主进程无法等到子进程退出，解决办法：主进程退出子进程销毁
# 1. 让子进程设置成为守护主进程，主进程退出子进程销毁，子进程会依赖主进程
import multiprocessing
import time


def task():
    while True:
        print("任务执行中...")
        time.sleep(0.2)


# 判断是否是直接执行的模块，程序入口模块

# 编制 python 写法，直接执行的模块，需要加水判断是否是主模块的代码
if __name__ == "__main__":
    # 创建子进程
    sub_process = multiprocessing.Process(target=task)
    # 把子进程设置成为守护主进程，以后主进程退出子进程直接销毁
    sub_process.daemon = True
    sub_process.start()

    # 主进程延时0.5秒钟
    time.sleep(0.5)
    print("Over")