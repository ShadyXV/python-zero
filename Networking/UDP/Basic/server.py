import socket

localIP  = "127.0.0.1"
localPort = 20001
bufferSize = 1024

msgFromServer = "Hello UDP CLient"
bytesToSend = str.encode(msgFromServer)

## creating a datagram socket

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to addrss and ip

UDPServerSocket.bind((localIP, localPort))


print("UDP server up and running")

while(True) :
  bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
  message = bytesAddressPair[0]
  address = bytesAddressPair[1]
  clientMsg = "Message from Client: {}".format(message)
  clientIP = "Client IP AddressL {}".format(address)

  print(clientMsg)
  print(clientIP)

  UDPServerSocket.sendto(bytesToSend, address)