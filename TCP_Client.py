#
# TCP Client
#
import socket
import sys


serverName = 'localhost'
serverPort = 8000


clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

while True:
#sentence = 'GET /echo.php?message=hello HTTP/1.1\r\n\r\n'
    sentence = raw_input("Message:")
    clientSocket.send(sentence)
     

    status= clientSocket.recv(1024)


   
    print status

clientSocket.close()
