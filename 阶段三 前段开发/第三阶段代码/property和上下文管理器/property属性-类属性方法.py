class Person(object):
    def __init__(self):
        # 设置私有属性
        self.__age = 0

    def get_age(self):
        print("获取属性啦")
        return self.__age

    def set_age(self, new_age):
        print("设置属性啦")
        if (new_age >= 0) and (new_age < 130):
            self.__age = new_age
        else:
            print("成精了")

    age = property(get_age, set_age)


if __name__ == '__main__':
    person = Person()
    print(person.age)

    person.age = 50
    print(person.age)
