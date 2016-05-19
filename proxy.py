# Networking & Security for Informatics - Assignment 4
# Programmer: Jason Lin

# Import socket library
from socket import *
import time

''' Helping Functions '''
def HTTP_GET(host, port):
    # Declare socket
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.settimeout(1.0)

    # Connect to the host
    try:
        clientSocket.connect((host, port))
        print "Successfully connected to port " + str(port)

    except:
        print host + " cannot be connected to port " + str(port)

    # Send GET request
    try:
        z = clientSocket.send("GET / HTTP/1.0 \r\nHost: " + host + "\r\nConnection: close\r\n\r\n")
        print "successfully sent " + str(z) + " bytes to port " + str(port)

    except:
        print "Cannot send data to port " + str(port)

    # Listen and store the response
    response = ''
    while True:
        received = clientSocket.recv(4096)
        response+= received
    
        if len(received) == 0:
            break

    # discard the header and store only the content
    content = response.split('\r\n\r\n')

    clientSocket.close()
    
    return content
    
def closeSockets():
    serverSocket.close()
    client.close()


''' Main Program '''
# Establish connection to client
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('127.0.0.1', 10000))
serverSocket.listen(1)

client, address = serverSocket.accept()
print 'Client socket established at port 10000.'

cache = {}

# Server implementation
while True:
    currentHostname = client.recv(100)
    print 'Hostname "{}" received.'.format(currentHostname)
    
    # If the requested hostname does not have a cache entry
    if currentHostname not in cache:
        GETinfo = HTTP_GET(currentHostname, 80)
        currTime = time.time()
        cache[currentHostname] = [GETinfo[1], currTime]
        
        client.send(GETinfo[1])
        print 'Response sent from remote server.'
        
    # If the requested hostname has a cache entry
    else:
        # If the info is not stale
        if (time.time() - cache[currentHostname][1]) < 60:
            client.send(cache[currentHostname][0])
            print 'Response sent from cache.'
            
        # If the info is stale
        else:
            currTime = time.time()
            GETinfo = HTTP_GET(currentHostname, 80)
            cache[currentHostname] = [GETinfo[1], currTime]
            
            client.send(GETinfo[1])
            print 'Response sent from remote server.'

