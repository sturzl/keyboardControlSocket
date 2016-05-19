import socket, time
def initializeSocket():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 5007))

def sendCommand(command):
    client.send(command)
