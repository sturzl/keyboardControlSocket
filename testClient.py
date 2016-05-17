import socket
import sys
from thread import *

def start_socket(): 
    #begins socket connection to client and returns the socket instance
    HOST = '192.168.8.103' # Symbolic name meaning all available interfaces
    PORT = 5005 # Arbitrary non-privileged port

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print 'Socket created'

    #Bind socket to local host and port
    try:
        s.bind((HOST, PORT))
    except socket.error , msg:
        print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]

    print 'Socket bind complete'

    #Start listening on socket
    s.listen(10)
    print 'Socket now listening'
    return s

    #Function for handling connections. This will be used to create threads
def clientthread(conn):
    #Sending message to connected client
    conn.send('Welcome to the server. Type something and hit enter\n') #send only takes
    #infinite loop so that function doesnt terminate and thread doesnt end.
    #waits until receives data from client then sends reply
    data = ''
    while True:

        #Receiving from client
        data = conn.recv(1024)
        reply = 'OK...' + data
        if not data:
            break
        print data
        conn.send(data)
        #do stuff with data

    #came out of loop
    conn.close()
    return data
