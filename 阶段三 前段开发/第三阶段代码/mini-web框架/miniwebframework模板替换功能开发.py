import time
# web框架的职责专门负责处理动态资源请求


# 获取首页数据
def index():
    # 状态信息
    status = "200 OK"
    # 响应头信息
    response_header = [("Server", "WPS/2.0")]
    # 1. 打开指定模板文件，读取模板文件中的数据
    with open("../template/index.html", "r") as file:
        file_data = file.read()
    # 2. 查询数据库，模板里面的模板变量({%content%})替换成以后从数据库里面查询的数据
    # web框架处理后的数据
    # 获取当前时间
    data = time.ctime()
    response_body = file_data.replace("{%content%}", data)
    # 这里返回的事元组
    return status, response_header, response_body


# 处理没有找到的动态资源
def not_found():
    # 状态信息
    status = "404 Not Found"
    # 响应头信息
    response_header = [("Server", "WPS/2.0")]
    # web框架处理后的数据
    data = "Not Found"
    # 这里是元组
    return status, response_header, data


# 处理动态资源请求
def handle_request(env):
    # 获取动态的请求资源路径
    request_path = env["request_content"]
    print("动态资源请求的地址:", request_path)
    # 判断请求的动态资源路径，选择指定的函数处理对应的动态资源请求
    if request_path == "/index.html":
        # 获取首页数据
        result = index()
        # 把处理后的结果返回给Web服务器使用，让Web服务器拼接响应报文时使用
        return result
    else:
        # 没有动态资源数据，返回404状态信息
        result = not_found()
        # 把处理的结果返回给Web服务器使用，让Web服务器拼接响应报文时使用
        return result
