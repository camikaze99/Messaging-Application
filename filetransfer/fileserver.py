import socket

s = socket.socket()
hostName = socket.gethostname()
hostIP = socket.gethostbyname(hostName)
port = 5000
s.bind((hostIP, port))
s.listen(1)
print(hostName + "//" + hostIP)
print("Waiting for any incoming connections ... ")
conn, addr = s.accept()
print(addr, "Has connected to the server")

filename = input(str("Please enter the filename of the file : "))
file = open(filename , 'rb')
file_data = file.read(1024)
conn.send(file_data)
print("Data has been transmitted successfully")
