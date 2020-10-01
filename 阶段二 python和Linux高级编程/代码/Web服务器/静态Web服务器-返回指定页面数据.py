import socket


def main():
    # 创建服务器套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置端口复用
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

    # 绑定端口号
    tcp_server_socket.bind(("", 8000))

    # 设置监听
    tcp_server_socket.listen(128)

    # 循环接收客户端请求
    while True:
        # 等待客户端连接请求
        new_client, ip_port = tcp_server_socket.accept()

        # 接收客户端发送的信息
        recv_data = new_client.recv(4096)
        # 判断接收的数据长度是否为0
        if recv_data == 0:
            new_client.close()
            return

        recv_content = recv_data.decode("utf-8")
        print(recv_content)
        # 对数据进行分割
        request_list = recv_content.split(" ", 2)
        request_path = request_list[1]
        print(request_path)

        # 判断请求信息是否为"/",如果是根目录返回首页
        if request_path == "/":
            request_path = "/index.html"

        # 从文件中读取信息
        with open("static" + request_path, "rb") as file:
            file_data = file.read()

        # 把响应报文信息写成http协议格式
        # 响应行
        response_line = "HTTP/1.1 200 OK\r\n"
        # 响应头
        response_header = "Server: PWS1.0\r\n"
        # 响应体
        response_body = file_data
        respnse = (response_line +
                   response_header +
                   "\r\n").encode("utf-8") + response_body

        # 发送数据到客户端
        new_client.send(respnse)

        # 关闭服务客户端的套接字
        new_client.close()


if __name__ == '__main__':
    main()