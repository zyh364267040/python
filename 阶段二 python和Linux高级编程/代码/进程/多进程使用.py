import multiprocessing
import time


def task(task):
    for i in range(3):
        print(task)
        time.sleep(0.2)


def run():
    dance_process = multiprocessing.Process(target=task, args=("跳舞中...",))
    sing_process = multiprocessing.Process(target=task, args=("唱歌中...",))

    dance_process.start()
    sing_process.start()


if __name__ == '__main__':
    run()
