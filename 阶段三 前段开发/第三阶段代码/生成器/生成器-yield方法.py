# 在函数里面看到有yield关键字，那么这个函数就是生成器了
def my_generator(n):
    for i in range(n):
        print("开始生成数据")
        # 当程序执行到yield关键字的时候代码暂停并把结果返回
        # 再次启动生成器的时候会在暂停的位置继续往下执行
        yield i
        print("生成完毕")


if __name__ == '__main__':
    values = my_generator(4)
    # 获取生成器下一个值
    # print(next(values))
    # print(next(values))
    # print(next(values))
    # print(next(values))
    # print(next(values))

    for value in values:
        print(value)
