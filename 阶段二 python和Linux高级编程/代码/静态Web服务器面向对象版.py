import socket
import threading
import sys


class HttpWebServer(object):
    def __init__(self):
        # 创建服务器套接字
        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置端口号复用
        tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        params = sys.argv
        if len(params) != 2:
            port = 10000
        elif len(params) == 2:
            if not params[1].isdigit():
                port = 10000
        else:
            port = int(params[1])
        # 绑定端口号
        tcp_server_socket.bind(("", port))
        # 设置监听
        tcp_server_socket.listen(128)
        self.tcp_server_socket = tcp_server_socket

    @staticmethod
    def handle_server_request(new_socket):
        # 接收浏览器发送的数据
        recv_data = new_socket.recv(4096)
        # 判断返回数据长度为0，浏览器关闭，关闭服务浏览器的套接字
        if len(recv_data) == 0:
            new_socket.close()
            return
            # 获取浏览器发送的页面请求信息
        recv_list = recv_data.decode("utf-8").split(" ", 2)
        recv_path = recv_list[1]
        # 判断请求信息是"/"，返回首页
        if recv_path == "/":
            recv_path = "/index.html"
        try:
            # 打开请求网页
            with open("static" + recv_path, "rb") as file:
                file_data = file.read()
        except:
            # 打开请求网页
            with open("static/error.html", "rb") as file:
                file_data = file.read()
            # 响应行
            response_line = "HTTP/1.1 404 Not Found\r\n"
            # 响应头
            response_header = "Server: PWS1.0\r\n"
            # 响应体
            response_body = file_data
            response = (response_line +
                        response_header +
                        "\r\n").encode("utf-8") + response_body
            # 发送数据到浏览器
            new_socket.send(response)
        else:
            # 响应行
            response_line = "HTTP/1.1 200 Ok\r\n"
            # 响应头
            response_header = "Server: PWS1.0\r\n"
            # 响应体
            response_body = file_data
            response = (response_line +
                        response_header +
                        "\r\n").encode("utf-8") + response_body
            # 发送数据到浏览器
            new_socket.send(response)
        finally:
            # 关闭服务套接字
            new_socket.close()

    def run(self):
        # 循环接收连接请求
        while True:
            new_socket, ip_port = self.tcp_server_socket.accept()
            # 创建子线程
            sub_thread = threading.Thread(target=self.handle_server_request, args=(new_socket,))
            # 设置子线程守护主线程
            sub_thread.setDaemon(True)
            # 启动子线程
            sub_thread.start()

if __name__ == '__main__':
    web_server = HttpWebServer()
    web_server.run()