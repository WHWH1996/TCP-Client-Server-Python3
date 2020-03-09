#!/usr/bin/python3

import socket

#Creating the socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host = socket.gethostname() #Host is the server IP
port = 4446 #Port to listen on 

#Binding to socket
serversocket.bind((host, port)) #Host will be replaced/substitued with IP, if changed and not running on host

#Starting TCP listener
serversocket.listen(3)

while True:
    #Starting the connection 
    clientsocket,address = serversocket.accept()

    print("received connection from i %s" % str(address))
    
    #Message sent to client after successful connection
    message = 'hello! Thank you for connecting to the server' + "\r\n"
    
    clientsocket.send(message.encode())

    clientsocket.close()
