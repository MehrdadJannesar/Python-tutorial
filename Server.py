import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_ip = "localhost"
sock_port = 7000


sock.bind((sock_ip,sock_port))
sock.listen(10)

while True:

    server_time = time.ctime()

    c,addr = sock.accept()

    print("One client connected !")
    c.sendall(server_time.encode("utf-8"))
    c.close()
