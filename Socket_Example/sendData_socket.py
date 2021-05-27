import socket

UDP_IP = "192.168.1.210"
UDP_PORT = 5005
MESSAGE = b'123456'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
