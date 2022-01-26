# Erin J. Saijan
# HW-2

import socket

Max_Size = 1024

clientS = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "52.14.128.203" # The server's hostname
port = 45062 # The port used by the server

## Connecting to AWS
clientS.connect((host, port)) ##why is there 2 commas 

print("Connected")

## Sending data to AWS
data = open("file.txt", 'rb')

l = data.read(Max_Size)

clientS.send(l)

data.close()

clientS.shutdown(socket.SHUT_WR)
print("Finished, server responds with")
print(clientS.recv(1024).decode('utf-8'))

clientS.close()




