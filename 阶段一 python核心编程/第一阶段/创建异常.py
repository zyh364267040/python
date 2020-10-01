# 创建一个异常，并使用这个异常
class ShortInputError(Exception):
    def __init__(self, lenght, min_len):
        self.lenght = lenght
        self.min_len = min_len

    def __str__(self):
        return f"您的密码长度是{self.lenght},密码长度最小为{self.min_len}"


def main():
    while True:
        try:
            password = input("请输入6位以上密码:")
            if len(password) < 6:
                raise ShortInputError
        except:
            print(ShortInputError(password, 6))
        else:
            print("密码设置成功")
            break


if __name__ == '__main__':
    main()
