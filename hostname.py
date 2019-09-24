import socket

def getHostIP():
    try:
        hostName = socket.gethostname()
        hostIP = socket.gethostbyname(hostName)
        print("Hostname :  ", hostName)
        print("IP : ", hostIP)
    except:
        print("Unable to get Hostname and IP")

getHostIP()
