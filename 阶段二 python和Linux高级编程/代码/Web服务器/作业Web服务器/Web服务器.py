import socket
import multiprocessing
import sys


class HttpWebServer(object):
    def __init__(self, port):
        # 创建服务器套接字
        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置端口复用
        tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

        # 绑定端口
        tcp_server_socket.bind(("", port))

        # 设置监听
        tcp_server_socket.listen(128)
        self.tcp_server_socket = tcp_server_socket

    @staticmethod
    def handle_server_request(new_socket):
        # 接收客户端信息
        recv_data = new_socket.recv(4096)
        if len(recv_data) == 0:
            new_socket.close()
            return
        recv_list = (recv_data.decode("utf-8")).split(" ", 2)
        request_path = recv_list[1]

        if request_path == "/":
            request_path = "/index.html"

        try:
            with open("static" + request_path, "rb") as file:
                file_data = file.read()

        except:
            with open("static/error.html", "rb") as file:
                file_data = file.read()
            # 响应行
            response_line = "HTTP/1.1 404 Not Found\r\n"
            # 响应头
            response_header = "Server: ZWS1.0\r\n"
            # 响应体
            response_body = file_data
            response = (response_line +
                        response_header +
                        "\r\n").encode("utf-8") + response_body

            # 发送数据到客户端
            new_socket.send(response)
        else:
            # 响应行
            response_line = "HTTP/1.1 200 OK\r\n"
            # 响应头
            response_header = "Server: ZWS1.0\r\n"
            # 响应体
            response_body = file_data
            response = (response_line +
                        response_header +
                        "\r\n").encode("utf-8") + response_body

            # 发送数据到客户端
            new_socket.send(response)
        finally:
            # 关闭服务客户端的套接字
            new_socket.close()

    def start(self):
        # 循环接收连接请求
        while True:
            # 等待客户端连接请求
            new_socket, ip_port = self.tcp_server_socket.accept()
            # 创建子进程
            sub_process = multiprocessing.Process(target=self.handle_server_request,
                                                  args=(new_socket,))
            sub_process.daemon = True
            # 启动子进程
            sub_process.start()
            if not sub_process.is_alive():
                sub_process.terminate()


def main():
    terminal_content = sys.argv
    if len(terminal_content) != 2:
        port = 9000
    elif  not terminal_content[1].isdigit():
        port = 9000
    else:
        port = int(terminal_content[1])

    web_server = HttpWebServer(port)
    web_server.start()


if __name__ == '__main__':
    main()
