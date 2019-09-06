import socket
import threading
import sys
import chatclient as chatClient

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connections = []

class Server:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connections = []
    def __init__(self):
        self.sock.bind(('0.0.0.0', 10000))
        self.sock.listen(1)

    def handler(self, c, a):
        while True:
            data = c.recv(1024)
            for connection in self.connections:
                connection.send(data)
            if not data:
                print(str(a[0]) + ':' + str(a[1]), "disconnected")
                self.connections.remove(c)
                c.close()
                break

    def run(self):
        while True:
            c, a = self.sock.accept()
            cThread = threading.Thread(target = self.handler, args = (c, a))
            cThread.deamon = True
            cThread.start()
            self.connections.append(c)
            print(str(a[0]) + ':' + str(a[1]), "connected")

if (len(sys.argv) > 1):
    client = chatClient.Client(sys.argv[1])
else:
    server = Server()
    server.run()

#stopServer = input()
#if stopServer == 'stopthisserver':
#print("Shutting down...")
#cThread._Thread__stop()
