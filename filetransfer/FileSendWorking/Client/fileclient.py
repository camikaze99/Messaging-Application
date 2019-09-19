import socket

s = socket.socket()
serverAddress = input(str("Please enter the host address of the sender : "))
port = 5000
s.connect((serverAddress, port))
print("Connected ... ")

fileContent = s.recv(2014)
file = open("Recv.txt", 'wb')
file.write(fileContent)
file.close()
print("File has been received successfully.")
