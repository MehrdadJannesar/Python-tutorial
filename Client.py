import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock_ip = "localhost"
sock_port = 7000

sock.connect((sock_ip,sock_port))
print(sock.recv(1024))
