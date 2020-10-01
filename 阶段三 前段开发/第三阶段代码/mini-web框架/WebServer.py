import socket
import threading


class WebServer(object):
    def __init__(self):
        # 创建服务器套接字
        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置端口号复用
        tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # 绑定端口号
        tcp_server_socket.bind(("", 8000))
        # 设置监听
        tcp_server_socket.listen(128)
        self.tcp_server_socket = tcp_server_socket

    @staticmethod
    def handle_client_request(new_socket):
        # 等待接收客户端请求数据
        request_data = new_socket.recv(4096)
        # 判断接收到的数据是否为空，如果为空表示客户端已断开连接
        if len(request_data) == 0:
            print("客户端已断开连接")
            # 关闭服务客户端的套接字
            new_socket.close()
            return

        request_content = (request_data.decode("utf-8")).split(" ", 2)
        request = request_content[1]
        # 判断数据请求为"/"，返回首页信息
        if request == "/":
            request = "/index.html"
        # 尝试打开文件，如果没有改文件则会报错
        try:
            # 打开客户端请求数据的相关页面
            with open("static" + request, "rb") as file:
                response_body = file.read()
        except Exception as e:
            print(e)
            # 没有该文件报错，则打开404状态文件返回
            with open("../static/error.html", "rb") as file:
                response_body = file.read()
            # 响应行
            response_line = "HTTP/1.1 404 Not Found\r\n"
            # 响应头
            response_header = "Server: PWS/1.0\r\n"
            response = (response_line +
                        response_header +
                        "\r\n").encode("utf-8") + response_body
            # 发送数据到客户端
            new_socket.send(response)
        else:
            # 响应行
            response_line = "HTTP/1.1 200 Ok\r\n"
            # 响应头
            response_header = "Server: PWS/1.0\r\n"
            response = (response_line +
                        response_header +
                        "\r\n").encode("utf-8") + response_body
            # 发送数据到客户端
            new_socket.send(response)
        finally:
            # 关闭套接字
            new_socket.close()

    def run(self):
        # 循环接收客户端连接请求
        while True:
            # 等待接收客户端连接请求
            new_socket, ip_port = self.tcp_server_socket.accept()
            # 创建子线程
            sub_thread = threading.Thread(target=self.handle_client_request, args=(new_socket,))
            # 设置子线程守护主线程
            sub_thread.setDaemon(True)
            # 启动子线程
            sub_thread.start()


if __name__ == '__main__':
    web_server = WebServer()
    web_server.run()
