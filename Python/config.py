# import socket
from socket import socket,AF_INET,SOCK_STREAM
HOST = '127.0.0.1'
IPORT = 9999
PPORT = 9998
TPORT = 9997
def sendMsg(sock): 
    message = "Hi! Sending connection message"
    sock.sendall(message.encode())