import socket


def main():
    # 创建服务器套接字
    tcp_server_solket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置端口号复用
    tcp_server_solket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

    # 绑定端口号
    tcp_server_solket.bind(("", 8000))

    # 设置监听
    tcp_server_solket.listen(128)

    # 循环接收客户端请求
    while True:
        # 等待接收客户端连接请求
        new_cline, ip_port = tcp_server_solket.accept()

        # 接收客户端发送的信息
        recv_data = new_cline.recv(4096)
        if recv_data == 0:
            new_cline.close()
            return

        # 把收到的数据解码
        recv_content = recv_data.decode("utf-8")
        # 把数据按空格切分
        request_list = recv_content.split(" ", 2)
        request_path =request_list[1]

        if request_path == "/":
            request_path = "/index.html"

        try:
            with open("static" + request_path, "rb") as file:
                file_data = file.read()
        except Exception as e:
            # 响应行
            request_line = "HTTP/1.1 404 Not Found\r\n"
            # 响应头
            request_header = "Server: PWS1.0\r\n"
            # 读取404页面数据
            with open("static/error.html", "rb") as file:
                file_data = file.read()
            # 响应体
            request_body = file_data
            request = (request_line +
                       request_header +
                       "\r\n").encode("utf-8") + request_body
            # 把数据发送到客户端
            new_cline.send(request)
        else:
            # 响应行
            request_line = "HTTP/1.1 200 OK\r\n"
            # 响应头
            request_header = "Server: PWS1.0\r\n"
            # 响应体
            request_body = file_data
            request = (request_line +
                       request_header +
                       "\r\n").encode("utf-8") + request_body

            # 把数据发送到客户端
            new_cline.send(request)
        finally:
            # 关闭服务客户端的套接字
            new_cline.close()


# 判断是否主模块
if __name__ == '__main__':
    main()
