import socket

host = '192.168.8.13'
port = 5005

def initializeSocket(sock=None):
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def connect(sock):
    sock.connect((host, port))

def sendCommand(msg,sock):
    totalsent = 0
    while totalsent < 8000:
        sent = sock.send(msg[totalsent:])
        if sent == 0:
            raise RuntimeError("socket connection broken")
        totalsent = totalsent + sent
