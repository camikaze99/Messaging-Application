import socket
import threading
import sys
import chatserver as chatServer

class Client:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def sendMessage(self):
        while True:
            self.sock.send(bytes(input(""), 'utf-8'))
#            print(str(a[0]) + ':' + str(a[1]), " said this")

    def __init__(self, address):
        self.sock.connect((address, 10000))

        iThread = threading.Thread(target = self.sendMessage)
        iThread.deamon = True
        iThread.start()

        while True:
            userMessage = self.sock.recv(1024)
            if not userMessage:
                break
#            print(address + ":" + str(userMessage, 'utf-8'))
#            print(str(userMessage, 'utf-8'))

if (len(sys.argv) > 1):
    client = Client(sys.argv[1])
else:
    server = chatServer.Server()
    server.run()
