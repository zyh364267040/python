import socket
import threading


def handle_client_request(new_socket):
    # 等待接收客户端信息
    recv_data = new_socket.recv(4096)
    if len(recv_data) == 0:
        new_socket.close()
        return

    # 把接收到的数据解码
    recv_content = recv_data.decode("utf-8")
    # 把数据按空格剪切
    request_list = recv_content.split(" ", 2)
    request_path = request_list[1]

    # 如果返回的根目录则发送首页
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
        response_header = "Server: PWS1.0\r\n"
        # 响应体
        response_body = file_data
        response = (response_line +
                    response_header +
                    "\r\n").encode("utf-8") + response_body
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

        # 把数据发送给客户端
        new_socket.send(response)
    finally:
        # 关闭服务客户端的套接字
        new_socket.close()


def main():
    # 创建服务器套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置端口复用
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

    # 绑定端口
    tcp_server_socket.bind(("", 8888))

    # 设置监听
    tcp_server_socket.listen(128)

    # 循环接收客户端请求
    while True:
        # 等待接收客户端连接请求
        new_socket, ip_port = tcp_server_socket.accept()

        # 连接成功后，响应体报送交给子进程来完成，可以让多人同事连接服务器
        # 创建子线程
        sub_thread = threading.Thread(target=handle_client_request, args=(new_socket,))
        # 设置守护主线程
        sub_thread.setDaemon(True)
        # 启动子线程
        sub_thread.start()


if __name__ == '__main__':
    main()
