import socket
import threading


# 处理客户端信息的函数
def handle_client_request(new_socket):
    # 使用新的套接字接收客户端发送的数据
    recv_data = new_socket.recv(4096)
    # 判断接收到的数据长度，若为0，表示客户端已断开连接，关闭套接字
    if len(recv_data) == 0:
        new_socket.close()
        return

    recv_content = recv_data.decode("utf-8")
    recv_list = recv_content.split(" ", 2)
    recv_path = recv_list[1]
    if recv_path == "/":
        recv_path = "/index.html"
    try:
        with open("static" + recv_path, "rb") as file:
            file_data = file.read()
    except:
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

        # 发送数据到客户端
        new_socket.send(response)
    else:
        # 响应行
        response_line = "HTTP/1.1 200 OK\r\n"
        # 响应头
        response_header = "Server: PWS1.0\r\n"
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


if __name__ == '__main__':
    # 创建服务器套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置端口号复用
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

    # 绑定端口号
    tcp_server_socket.bind(("", 9000))

    # 设置监听
    tcp_server_socket.listen(128)

    # 循环等待接收客户端连接请求
    while True:
        # 等待接收客户端连接请求
        new_socket, ip_port = tcp_server_socket.accept()
        # 创建子线程
        sub_thread = threading.Thread(target=handle_client_request, args=(new_socket,))
        # 设置子线程守护主线程
        sub_thread.setDaemon(True)
        # 启动子线程
        sub_thread.start()

