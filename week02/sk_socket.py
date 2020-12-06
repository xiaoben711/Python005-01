import socket

sk = socket.socket()
sk.bind(("127.0.0.1", 8090))
sk.listen()

def get_file(sk_obj):
    """
    接收文件的函数
    :param sk_obj:
    :return:
    """
    # 接收文件大小
    file_size = sk_obj.recv(1024).decode("utf8")
    # 接收文件名称
    file_name = sk_obj.recv(1024).decode("utf8")

    # 接收文件内容
    with open(f"./{file_name}", "wb") as f:
        while file_size > 0:
           f.write(sk_obj.recv(1024))
           file_size -= 1024

conn, addr = sk.accept()

get_file(conn)

# 释放资源
conn.close()
sk.close()
