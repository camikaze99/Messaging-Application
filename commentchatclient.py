import socket
import threading
import sys
import chatserver as chatServer

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connections = []

class Client:
	#Sockets worden gebruikt door services en toepassingen die een verbinding tot stand moeten brengen met een andere host of andere hosts
#het internetadresfamilie voor IPv4  #het sockettype voor TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def sendMessage(self):
        while True:
			#Input, wat je typt in de terminal
			#Wordt gestuurd naar de socket
            self.sock.send(bytes(input(""), 'utf-8'))
#            print(str(a[0]) + ':' + str(a[1]), " said this")

    def __init__(self, address):
		#Connect met de server
        self.sock.connect((address, 10000))

        iThread = threading.Thread(target = self.sendMessage)
        iThread.deamon = True
        iThread.start()

        while True:
            userMessage = self.sock.recv(1024)
              # als de client weggaat, dan wordt de verbind afgesloten van de server
            if not userMessage:
                break
            print(address + ":" + str(userMessage, 'utf-8'))
#            print(str(userMessage, 'utf-8'))

if (len(sys.argv) > 1):
    client = Client(sys.argv[1])
else:
    server = chatServer.Server()
    server.run()

