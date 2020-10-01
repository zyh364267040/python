import multiprocessing


# 显示信息的任务
def showInfo(name, age):
    print(name, age)


if __name__ == "__main__":
    # 创建子进程
    # 以元组方式传参，元组里面的元素顺序要和函数的参数顺序保持一致
    sub_process = multiprocessing.Process(target=showInfo, args=("李四", 20))
    # 启动进程
    sub_process.start()

    # 以字典方式传参，字典里面的key要和函数里面的参数名保持一致，没有顺序要求
    sub_process = multiprocessing.Process(target=showInfo, kwargs={"age": 20, "name": "王五"})
    # 启动进程
    sub_process.start()

    # 一个参数用args,一个用kwargs
    sub_process = multiprocessing.Process(target=showInfo, args=("冯七",), kwargs={"age": 20})
    # 启动进程
    sub_process.start()