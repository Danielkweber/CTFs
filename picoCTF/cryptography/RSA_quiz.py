import socket
import sys

host = '2019shell1.picoctf.com'
port = 2611

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

while input('Read?') == 'y':
    data = sock.recv(65536)
    print(data)

answer = input('Reponse?')

sock.send('Y'.encode())

while input('Read?') == 'y':
    data = sock.recv(65536)
    print(data)