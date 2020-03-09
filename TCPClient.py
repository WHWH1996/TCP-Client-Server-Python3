#!/usr/bin/python3

import socket
import time

#Create socket object
clientsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#host = '192.168.1.104'
host = socket.gethostname()

port = 4446

clientsocket.connect(('192.168.1.50', port)) #You can substitue the host with the server IP

message = clientsocket.recv(500000)

StartTime = time.time()
t1 = (time.time() - StartTime)
StartTime = time.time()
#Receiving a maximum of 1024 bytes
message = clientsocket.recv(1)

t2 = (time.time() - StartTime)
print(t1)
print(t2)

clientsocket.close()

print(message.decode('ascii'))
