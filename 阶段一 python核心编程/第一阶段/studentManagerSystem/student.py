# 创建学员类
class Student(object):
    def __init__(self, name, gender, tel):
        self.name = name
        self.gender = gender
        self.tel = tel

    def __str__(self):
        return f"姓名{self.name},性别{self.gender}手机号{self.tel}"


# 验证代码
if __name__ == '__main__':
    student = Student("zhou", "nan", 111)
    print(student)
