import time


# 路由列表
route_list = []


# 定义带有参数的装饰器
def route(path):
    # 装饰器
    def decorator(func):
        # 添加路由到路由列表
        route_list.append((path, func))
        def inner():
            return func()
    # 返回装饰器
    return decorator


# 获取个人中心数据
@route("/center.html")
def center():
    # 状态信息
    status = "200 Ok"
    # 响应头信息
    response_header = [("Server: PWB/2.0",)]
    # 1. 打开指定模板文件，读取模板中的数据
    with open("template/center.html", "r") as file:
        file_data = file.read()
    # 2. 查询数据库，模板里面的模板变量({%content%})替换成以后从数据库里面查询的数据
    # web框架处理后的数据
    # 获取当前时间
    data = time.ctime()
    response_body = file_data.replace("({%content%})", data)
    return status, response_header, data


# 处理没有找到的动态资源
def not_found():
    # 状态信息
    status = "404 Not Found"
    # 响应头信息
    response_header = [("Server: WPS/2.0",)]
    # web框架处理后的数据
    data = "Not Found"
    return status, response_header, data


# 处理动态资源请求
def handle_request(env):
    # 获取动态资源路径
    requset_path = env["request_path"]
    # 遍历路由列表，匹配请求的url
    for path, func in route_list:
        if requset_path == path:
            # 找到指定路由，执行对应的函数
            return func()
        else:
            # 没有动态资源数据，返回404
            return not_found()
