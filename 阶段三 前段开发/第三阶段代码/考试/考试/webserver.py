import socket
import os
import threading
import miniwebframework


class WebServer(object):
    def __init__(self):
        # 创建服务器套接字
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置端口号复用
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # 绑定端口号
        server_socket.bind(("", 8000))
        # 设置监听
        server_socket.listen(128)
        self.server_socket = server_socket

    @staticmethod
    def handle_client_requset(new_socket):
        # 等待接收客户端数据
        recv_data = new_socket.recv(4096)
        # 判断接收数据长度是否为0
        if len(recv_data) == 0:
            new_socket.close()
            return
        recv_content = recv_data.decode("utf-8")
        recv_list = recv_content.split(" ", 2)
        request_content = recv_list[1]
        # 判断请求的页面是否为"/"
        if request_content == "/":
            request_content = "/index.html"

        # 判断是否是动态资源请求，后缀是.html的请求任务认为是动态资源请求
        if request_content.endswith(".html"):
            """动态资源请求"""
            # 动态资源请求找web框架进行处理，需要把请求参数给web框架
            # 准备给web框架的参数信息，都要放到字典里面
            env = {
                "request_content": request_content
                # 传入请求头信息，额外的参数可以在字典里面在进行添加
            }
            # 使用框架处理动态资源请求
            # 1. web框架需要把处理结果返回给Web服务器
            # 2. Web服务器负责把返回的结果封装成响应报文发送给浏览器
            status, headers, response_body = miniwebframework.handle_request(env)
            print(status, headers, response_body)
            # 响应行
            response_line = f"HTTP/1.1 {status}\r\n"
            # 响应头
            response_header = ""
            for header in headers:
                response_header += f"{header}\r\n"
            # 响应报文
            response = (response_line +
                        response_header +
                        "\r\n" +
                        response_body).encode("utf-8")
        else:
            # 判断文件是否存在
            if os.path.exists("static/" + request_content):
                # 响应行
                response_line = "HTTP/1.1 200 OK\r\n"
                # 相应头
                response_header = "Server: PWS/1.1\r\n"
                # 响应体
                with open("static" + request_content, "rb") as file:
                    response_body = file.read()
                # 发送给客户端的相应报文
                response = (response_line +
                            response_header +
                            "\r\n").encode("utf-8") + response_body
            else:
                # 响应行
                response_line = "HTTP/1.1 404 Not Found\r\n"
                # 相应头
                response_header = "Server: PWS/1.1\r\n"
                # 响应体
                with open("static/error.html", "rb") as file:
                    response_body = file.read()
                # 相应报文
                response = (response_line +
                            response_header +
                            "\r\n").encode("utf-8") + response_body
        # 发送数据到客户端
        new_socket.send(response)
        # 关闭服务于客户端的套接字
        new_socket.close()

    def run(self):
        # 循环等待接收连接请求
        while True:
            # 等待接收连接请求
            new_socket, ip_port = self.server_socket.accept()
            # 创建子线程
            sub_thread = threading.Thread(target=self.handle_client_requset, args=(new_socket, ))
            # 设置子线程守护主线程
            sub_thread.setDaemon(True)
            # 启动子线程
            sub_thread.start()


if __name__ == '__main__':
    webserver = WebServer()
    webserver.run()
