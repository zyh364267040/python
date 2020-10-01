import socket


if __name__ == '__main__':
    # 创建客户端套接字
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 发送请求与服务器建立连接
    tcp_client_socket.connect(("192.168.18.4", 8888))

    # 向服务器发送信息
    # send_content = input("请输入发送到服务器的信息：")
    # send_content = "Hello,I'm client."
    send_content = ""
    send_data = send_content.encode("utf-8")
    tcp_client_socket.send(send_data)

    # 接收客户端发送的信息
    recv_data = tcp_client_socket.recv(1024)
    recv_content = recv_data.decode("utf-8")
    print(recv_content)

    # 关闭套接字
    tcp_client_socket.close()
