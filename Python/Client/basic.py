from config import *

client = socket(AF_INET,SOCK_STREAM)
types = [IPORT,PPORT,TPORT]
sock_type = 1
while (not (int(sock_type)>=1  and int(sock_type) <= 3)):
    sock_type = int(input("Which socket would you like to connect to? Enter 1 for iterative, 2 for polling or 3 for threaded.\n"))
sock_type -= 1
server_add = (HOST,IPORT)
client.connect(server_add)
sendMsg(client)
client.close()