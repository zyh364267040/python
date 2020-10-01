import multiprocessing
import time


def dance():
    for i in range(3):
        print("跳舞中...")
        time.sleep(0.2)


def sing():
    for i in range(3):
        print("唱歌中...")
        time.sleep(0.2)


if __name__ == "__main__":
    dance_process = multiprocessing.Process(target=dance)
    dance_process.start()

    sing()
