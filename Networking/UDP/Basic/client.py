import socket

msgFromClient = "Hello server"
bytersToSend = str.encode(msgFromClient)
serverAddressPort = ("127.0.0.1", 20001)
bufferSize  = 1024

# create a udp socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# send to server using create dudp socket
UDPClientSocket.sendto(bytersToSend, serverAddressPort)

msgFromServer = UDPClientSocket.recvfrom(bufferSize)

msg = "Message form Server {}".format(msgFromServer[0])
print(msg)