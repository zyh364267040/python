import socket
import threading


def handle_client_request(new_socket):
    # 等待接收客户端发送信息
    recv_data = new_socket.recv(1024)
    if len(recv_data) == 0:
        print("客户端已断开连接.")
        new_socket.close()
        return
    recv_content = recv_data.decode("utf-8")
    print(recv_content)

    # 发送信息到客户端
    # send_content = input("请输入要发生的信息：")
    send_content = "Hello,I'm Server."
    send_data = send_content.encode("utf-8")
    new_socket.send(send_data)

    new_socket.close()


if __name__ == '__main__':
    # 创建服务器套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置端口号复用
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

    # 绑定端口号
    tcp_server_socket.bind(("", 8888))

    # 设置监听
    tcp_server_socket.listen(128)

    # 循环接收客户端连接请求
    while True:
        # 等待客户端连接请求
        new_socket, ip_port = tcp_server_socket.accept()
        # 创建子线程
        sub_thread = threading.Thread(target=handle_client_request, args=(new_socket,))
        # 设置子线程守护主线程
        sub_thread.setDaemon(True)
        # 启动子线程
        sub_thread.start()


