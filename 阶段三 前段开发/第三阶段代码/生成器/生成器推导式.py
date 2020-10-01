my_generator = (pow(i, 2) for i in range(4))
print(my_generator)

# 生成器取值使用next函数获取生成器中的下一个值
# print(next(my_generator))
# print(next(my_generator))
# print(next(my_generator))
# print(next(my_generator))
# print(next(my_generator))
# 当生成器已经没有值时，会抛出StopIteration，表示生成器生成数据完毕

for value in my_generator:
    print(value)
