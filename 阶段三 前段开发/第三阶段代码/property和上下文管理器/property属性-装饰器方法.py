class Person(object):
    def __init__(self):
        # 设置私有属性
        self.__age = 0

    @property  # 当对象调用age属性的时候会执行下面的方法
    def age(self):
        return self.__age

    @age.setter  # 当对象调用age属性设置值得时候会调用下面的方法
    def age(self, new_age):
        print("获取属性啦")
        if (new_age >= 0) and (new_age < 130):
            self.__age = new_age
        else:
            print("成精了")


if __name__ == '__main__':
    person = Person()
    print(person.age)

    person.age = 70
    print(person.age)
