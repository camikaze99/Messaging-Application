import socket
import threading
import sys
import chatclient as chatClient

class Server:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# List of connections/clients.
    connections = []
    def __init__(self):
        self.sock.bind(('0.0.0.0', 10000))
# Listens for 1 active connection.
        self.sock.listen(1)

    def handler(self, chatConnection, ipAddress):
        defaultMessage = "Welcome to the chatroom. Please do not swear or spam or there with be consequences."

        chatConnection.send(bytes(defaultMessage, 'utf-8'))
        while True:
            userMessage = chatConnection.recv(1024)
            for connection in self.connections:
                print(str(ipAddress[0]) + '-----' + str(chatConnection))
                connection.send(userMessage)
            if not userMessage:
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
            print(str(ipAddress[0]) + ':' + str(ipAddress[1]), "connected")

if (len(sys.argv) > 1):
    client = chatClient.Client(sys.argv[1])
else:
    server = Server()
    server.run()
