import socket


# 判断是否是主模块
if __name__ == '__main__':
    # 创建服务器套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置端口号复用
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

    # 绑定端口号
    tcp_server_socket.bind(("", 8000))

    # 设置监听
    tcp_server_socket.listen(128)

    # 循环接收客户端的连接请求
    while True:
        # 接收客户端连接请求
        new_client, ip_port = tcp_server_socket.accept()

        # 接收客户端的请求信息
        recv_data = new_client.recv(4096)
        print(recv_data)

        # 打开文件读取文件中的数据
        with open("static/index.html", "r") as file:
            file_data = file.read()

        # 将发送给客户端的信息转换成HTTP响应格式
        # 响应行
        response_line = "HTTP/1.1 200 OK\r\n"
        # 响应头
        response_header = "Server: PWS/1.0\r\n"
        # 响应体
        response_body = file_data

        # 把数据封装成HTTP响应报文格式
        response = response_line + response_header + "\r\n" + response_body
        # 把字符串编码成二进制
        response_data = response.encode("utf-8")

        # 发送响应报文数据到客户端
        new_client.send(response_data)

        # 关闭服务客户端的套接字
        new_client.close()
