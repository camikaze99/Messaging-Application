import socket

s = socket.socket()
serverAddress = input(str("Please enter the host address of the sender : "))
port = 5000
s.connect((serverAddress, port))
print("Connected ... ")

filename = input(str("Please enter a filename for the incoming file : "))
file = open(filename, 'wb')
file_data = s.recv(1024)
file.write(file_data)
file.close()
print("File has been received successfully.")
