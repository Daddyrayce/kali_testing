import os
import socket

s = socket.socket()
port=8080

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
    if command == "view_cwd":
        files = os.getcwd()
        files = str(files)
        s.send(files.encode())
        print("Command sent successfully")
        print("")
    elif command == "custom_dir":
        user_input = s.recv(5000)
        user_input = user_input.decode()
        files = os.listdir(user_input)
        files = str(files)
        s.send(files.encode())
        print("")
        print("Command has been executed yes yes.")
        print("") 

    elif command == "download_file":
        file_path = s.recv(5000)
        file_path = file_path.decode()
        file = open(file_path, "rb")
        data = file.read()
        s.send(data)
        print("")
        print("File has been sent successfully")
        print("")

    else:
        print("Command no recognized")
        print("")