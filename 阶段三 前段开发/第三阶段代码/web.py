import socket
import os
import threading
import framework


class WebServer(object):
    def __init__(self):
        # 创建套接字
        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置端口号复用
        tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # 绑定端口号
        tcp_server_socket.bind(("", 8000))
        # 设置监听
        tcp_server_socket.listen(128)
        self.tcp_server_socket = tcp_server_socket

    # 处理客户端数据的函数
    @staticmethod
    def handle_client_requset(new_socket):
        # 等待接收数据
        recv_data = new_socket.recv(4096)
        # 判断接收的数据长度，客户端是否关闭
        if len(recv_data) == 0:
            print("浏览器已关闭")
            new_socket.close()
            return

        # 把接收到的数据解码，按空格分隔，取出浏览器请求的页面路径
        request_path = (recv_data.decode("utf-8").split(" ", 2))[1]
        # 如果请求的页面为"/",返回首页
        if request_path == "/":
            request_path = "/index.html"

        # 判断路径是".html",为动态请求，交给web框架处理
        if request_path.endswith(".html"):
            # 给web框架传参，格式为字典
            env = {"request_path": request_path}
            status, headers, response_body = framework.handle_request(env)
            # 响应行
            response_line = f"HTTP/1.1 {status}\r\n"
            # 响应头
            response_header = ""
            # 遍历得到的响应头信息
            for header in headers:
                response_header += f"{header}\r\n"
            # 响应报文
            response = (response_line +
                        response_header +
                        "\r\n" +
                        response_body).encode("utf-8")
        else:
            # 判断请求的页面是否存在
            if os.path.exists("static/" + request_path):
                # 文件存在
                # 按照响应报文格式，返回给浏览器数据
                # 响应行
                response_line = "HTTP/1.1 200 OK\r\n"
                # 响应头
                response_header = "Server: PWS/1.0\r\n"
                # 响应体
                with open("static" + request_path, "rb") as file:
                    response_body = file.read()
                # 响应报文
                response = (response_line +
                            response_header +
                            "\r\n").encode("utf-8") + response_body
            else:
                # 文件不存在
                # 响应行
                response_line = "HTTP/1.1 404 Not Found\r\n"
                # 响应头
                response_header = "Server: PWS/1.0\r\n"
                # 响应体
                with open("static/error.html", "rb") as file:
                    response_body = file.read()
                # 响应报文
                response = (response_line +
                            response_header +
                            "\r\n").encode("utf-8") + response_body
        # 发送数据到客户端
        new_socket.send(response)
        # 关闭服务客户端的套接字
        new_socket.close()

    def run(self):
        # 循环等待接收连接请求
        while True:
            # 等待接收连接请求
            new_socket, ip_port = self.tcp_server_socket.accept()
            # 创建子线程
            sub_thread = threading.Thread(target=self.handle_client_requset, args=(new_socket,))
            # 设置子线程守护主线程
            sub_thread.setDaemon(True)
            # 启动子线程
            sub_thread.start()


if __name__ == '__main__':
    webserver = WebServer()
    webserver.run()
