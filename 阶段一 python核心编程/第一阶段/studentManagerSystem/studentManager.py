# 学员管理系统
from student import *


class ManagerSystem(object):
    def __init__(self):
        # 存储学员信息列表
        self.student_list = []

    # 程序入口
    def run(self):
        # 1. 加载已保存的学员信息
        self.load_student()

        while True:
            # 2. 功能菜单
            self.show_menu()

            # 3. 用户输入功能序号
            menu_num = int(input("请输入功能序号："))

            # 4. 选择序号功能
            if menu_num == 1:
                print("请添加学员")
                self.add_student()
            elif menu_num == 2:
                print("请删除学员")
                self.del_student()
            elif menu_num == 3:
                print("修改学员信息")
                self.modify_student()
            elif menu_num == 4:
                print("查询学员信息")
                self.search_student()
            elif menu_num == 5:
                print("显示所有学员信息")
                self.show_all_student()
            elif menu_num == 6:
                print("保存学员信息")
                self.save_student()
            elif menu_num == 7:
                print("退出系统")
                break
            else:
                print("您输入的功能序号有误")

    def load_student(self):
        """加载学员信息"""
        # 不知道student.data是否存在使用try，避免程序异常
        try:
            f = open("student.data")
        except:
            f = open("student.data", "w")
        else:
            data = f.read()
            new_list = eval(data)
            self.student_list = [Student(i["name"], i["gender"], i["tel"]) for i in new_list]
        finally:
            f.close()

    # 该方法不涉及函数调用等信息，可以使用静态类方法
    @staticmethod
    def show_menu():
        """功能菜单"""
        print("----------请输入功能序号：----------")
        print("1:添加学员")
        print("2:删除学员")
        print("3:修改学员信息")
        print("4:查询学员信息")
        print("5:显示所有学员信息")
        print("6:保存学员信息")
        print("7:退出系统")

    def add_student(self):
        """添加学员"""
        name = input("请输入姓名：")
        gender = input("请输入性别：")
        tel = input("请输入手机号：")
        # 创建学员对象
        student = Student(name, gender, tel)
        # 把学员信息添加到学员的列表中
        self.student_list.append(student)
        print("添加成功，添加的学员信息是：", end="")
        print(student)

    def del_student(self):
        """删除学员"""
        del_name = input("请输入要删除的学员的姓名：")
        for i in self.student_list:
            if del_name == i.name:
                self.student_list.remove(i)
                print("该学员已删除")
                break
        else:
            print("查无此人！")


    def modify_student(self):
        """修改学员信息"""
        modify_name = input("请输入修改学员的姓名：")
        for i in self.student_list:
            if modify_name == i.name:
                i.name = input("请输入修改后的姓名：")
                i.gender = input("请输入修改后的性别：")
                i.tel = input("请输入修改后的手机号：")
                print(f"修改后的姓名{i.name},性别{i.gender},手机号{i.tel}")
                break
        else:
            print("查无此人！")

    def search_student(self):
        """查询学员信息"""
        search_name = input("请输入要查询的学员姓名：")
        for i in self.student_list:
            if search_name == i.name:
                print(f"查询到的学员信息为：姓名{i.name},性别{i.gender},手机号{i.tel}")
                break
        else:
            print("查无此人！")

    def show_all_student(self):
        print("姓名\t性别\t手机号")
        for i in self.student_list:
            print(f"{i.name}\t{i.gender}\t{i.tel}")

    def save_student(self):
        """保存学员信息"""
        f = open("student.data", "w")
        # 把存在学员列表中的数据转换成字典形式保存到文件中
        new_list = [i.__dict__ for i in self.student_list]
        f.write(str(new_list))
        f.close()


# 验证
if __name__ == '__main__':
    manager_system = ManagerSystem()
    manager_system.run()
