from config import *
# Initialise the socket on port 9997 with the host IP 
it_serv = socket(AF_INET,SOCK_STREAM)
print(str(HOST) + " " + str(IPORT))
it_serv.bind((HOST,IPORT))
# Listen for 10 connections - only handled one by one
it_serv.listen(10)
def handleRequest(): 
    host, add = it_serv.accept()
    data = host.recv(1024)
    if len(data)==0: 
        host.close()
    print(data.decode())
    message = "Iterative server recieved: " + data.decode() 
    host.sendall(message.encode())
    host.close()
running = True
while (running): 
    print("Server listening for connections...")
    handleRequest()
it_serv.close()