import socket
import threading
import sys
import chatclient as chatClient

class Server:
	#Sockets worden gebruikt door services en toepassingen die een verbinding tot stand moeten brengen met een andere host of andere hosts
#het internetadresfamilie voor IPv4  #het sockettype voor TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# List of connections/clients.
    connections = []
    def __init__(self):
		#Bind de socket aan een adres met de functie bind () 
		# Als u een lege string doorgeeft, accepteert de server verbindingen op alle beschikbare IPv4-interfaces
		#bind() wordt gebruikt om de socket te koppelen aan een specifieke netwerkinterface en poortnummer:
        self.sock.bind(('0.0.0.0', 10000))
       #Het luistert naar verbindingen van clients.
        self.sock.listen(1)
 
    def handler(self, chatConnection, ipAddress):
        defaultMessage = "Welcome to the chatroom. Please do not swear or spam or there with be consequences."	
        #defaultMessage wordt gestuurd naar de client, utf-8 ondersteunt de tekst bv de puntjes op de e
        chatConnection.send(bytes(defaultMessage, 'utf-8'))
        while True:
			#Data van de client die de server ontvangt
            userMessage = chatConnection.recv(1024)
            
            for connection in self.connections:
				#ipadress van de client, informatie van de verbinding van de client INFORMATIE OP DE SERVER TE ZIEN
                print(str(ipAddress[0]) + '-----' + str(chatConnection))
                #Message van de cleint wordt gestuurd naar de andere client
                connection.send(userMessage)
                # als de client weggaat, dan wordt de verbind afgesloten van de server
            if not userMessage:
				# str, ipadress wordt omgezet naar string
                print(str(ipAddress[0]) + ':' + str(ipAddress[1]), "disconnected")
                self.connections.remove(chatConnection)
                chatConnection.close()
                break

    def run(self):
        while True:
			
            chatConnection, ipAddress = self.sock.accept()
            chatConnectionThread = threading.Thread(target = self.handler, args = (chatConnection, ipAddress))
            chatConnectionThread.deamon = True
            chatConnectionThread.start()
            self.connections.append(chatConnection)
           #informatie wie met de server is connected
            print(str(ipAddress[0]) + ':' + str(ipAddress[1]), "connected")

if (len(sys.argv) > 1):
    client = chatClient.Client(sys.argv[1])
else:
    server = Server()
    server.run()

