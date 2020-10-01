# 2. 让主进程退出之前先让子进程销毁
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
    sub_process.start()

    # 主进程延时0.5秒钟
    time.sleep(0.5)
    # 退出主进程以前，先让子进程进行销毁
    sub_process.terminate()
    print("Over")