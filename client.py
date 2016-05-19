# Networking & Security for Informatics - Assignment 4
# Programmer: Jason Lin

# Import socket library
from socket import *
import time

''' Helping Functions '''
def HTTP_GET(host, port):
    # Declare socket
    cSocket = socket(AF_INET, SOCK_STREAM)
    cSocket.settimeout(1.0)

    # Connect to the host
    try:
        cSocket.connect((host, port))
        print "Successfully connected to {} at port {}".format(host, str(port))

    except:
        print host + " cannot be connected to {} at port {}".format(host, str(port))

    # Send GET request
    try:
        z = cSocket.send("GET / HTTP/1.0 \r\nHost: " + host + "\r\nConnection: close\r\n\r\n")
        print "successfully sent " + str(z) + " bytes to port " + str(port)

    except:
        print "Cannot send data to port " + str(port)

    # Listen and store the response
    response = ''
    while True:
        received = cSocket.recv(4096)
        response+= received
    
        if len(received) == 0:
            break

    # discard the header and store only the content
    content = response.split('\r\n\r\n')

    cSocket.close()
    
    return content
    
    
''' Main Program '''
# Connect to proxy server
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(('127.0.0.1', 10000))

outputDict = {'Match':[], 'No match':[]}
    
for hostname in ['www.uiowa.edu', 'www.google.com', 'www.yahoo.com']:
    clientSocket.send(hostname)
    print 'Attempting to receive HTTP information from {}.'.format(hostname)
        
    proxyResponse = clientSocket.recv(60000)
    hostResponse = HTTP_GET(hostname, 80)[1]
        
    if proxyResponse == hostResponse:
        outputDict['Match'].append(hostname)
        print 'Proxy response for {} matches hostname response.'.format(hostname)
            
    else:
        outputDict['No match'].append(hostname)
        print 'Proxy response for {} does not match hostname response.'.format(hostname)
        
    # Wait 30 seconds to send next hostname
    time.sleep(30)

clientSocket.close()

output = open('output.txt', 'w')
output.write('Matches: {}'.format(', '.join(outputDict['Match'])) + "\n")
output.write('Non-matches: {}'.format(', '.join(outputDict['No match'])) +  "\n")
output.close()
