import socket,os
# 创建socket对象
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sk.connect(("127.0.0.1", 8090))

def post_file(sk_obj, file_path):
    """
    :param sk_obj: socket 对象
    :param file_path: 文件路径
    :return:
    """
    # 发送文件大小
    file_size = os.stat(file_path).st_size
    sk_obj.sendall(str(file_size).encode("utf8"))

    # 发送文件名称
    file_name = os.path.split(file_path)[1]
    sk_obj.sendall(file_name.encode("utf8"))
    # 发送文件内容
    with open(file_path, "rb") as f:
        while file_size > 0:
            sk_obj.sendall(f.read(1024))
            file_size -= 1024

post_file(sk, "./test.txt")

#释放资源
sk.close()
