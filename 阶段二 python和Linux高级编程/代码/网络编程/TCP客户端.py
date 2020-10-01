import socket

if __name__ == '__main__':
    # 1. 创建tcp客户端套接字
    tcp_client_scoket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. 和服务段套接字建立连接
    tcp_client_scoket.connect(("192.168.0.104", 9090))
    while True:
        # send_contene = "hello, I'm Mac!"  #input()
        send_contene = input("请输入发送的信息：")
        # 对字符串进行编码成为二进制
        send_data = send_contene.encode("utf-8")

        # 3. 发送数据到服务端
        tcp_client_scoket.send(send_data)

    # 4. 接受服务端数据
    recv_data = tcp_client_scoket.recv(1024)
    recv_content = recv_data.decode("utf-8")
    print(recv_content)

    # 5. 关闭套接字
    tcp_client_scoket.close()
