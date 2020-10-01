import threading


def show_info(name, age):
    print(name, age)


if __name__ == '__main__':
    sub_thread = threading.Thread(target=show_info, args=("zhou", 30))
    sub_thread.start()

    sub_thread = threading.Thread(target=show_info, kwargs={"name": "zhou", "age": 31})
    sub_thread.start()