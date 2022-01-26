# Erin J. Saijan
# HW-2

import socket

MAX_FILE_SIZE = 1024

serverS = socket.socket()

host = socket.gethostname()
port = 45062

print("Connecting to: " + host + ":" + port.__str__())

serverS.bind((host, port))

print("Configuring Listen")

serverS.listen(10)

s, addr = serverS.accept()

print("Connection from " + addr.__str__())

rec = s.recv(MAX_FILE_SIZE).decode('utf-8')

print("Client sent: " + rec)

chars = 0
words = 0
lines = 0

Whitespace = True
for char in rec:
    chars += 1
    if(char == ' ' or char == '\t' or char == '\n') and not Whitespace:
        words += 1
        Whitespace = True
    else:
        Whitespace = False
    if(char == '\n'):
        lines += 1

print("There are " + chars.__str__() + " chars, "
	+ words.__str__() + " words, and " + lines.__str__() +
	" lines")

s.send(bytes("Chars are: " + chars.__str__() + 
	"\nWords are: " + words.__str__() + 
	"\nLines are: " + lines.__str__(), 'utf-8'))

