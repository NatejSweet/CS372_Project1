import socket
import sys

port=28333
if len(sys.argv) == 2:
    port = int(sys.argv[1])
s = socket.socket()
#make it reuable
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#bind it to a port
s.bind(('localhost', port))
#listen
s.listen()
print("Listening on port "+str(port))
#loop
while True:
    #accept new connections(new socket)
    c, addr = s.accept()
    print("Got connection from", addr)
    #send/recieve data
    c.sendall("HTTP/1.1 200 OK \r\n Content-Type: text/plain \r\n Content-Length: 6 \r\n Connection: close \r\n \r\n Hello!".encode())
    #close the socket
    c.close()