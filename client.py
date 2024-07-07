import socket

firstName = "Abbas"
lastName = "Nassar"
serverPort = 5051
hostName = socket.gethostname()
ip_address = socket.gethostbyname(hostName)
defaultGateway = "26.0.0.0"
subnetMask = '255.0.0.0'
broadcastAddress = '26.255.255.255'
# Create a UDP socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Allow broadcasting
clientSocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

while True:
    print('Select the type of message you want to send: ')
    print('1- Send message to peers.')
    print('2- Get a message from the server.')
    print('3- Exit.')
    Selection = int(input())
    if Selection == 1:
        message = input('Input message: ')
        message = hostName + " " + firstName + " " + lastName + " " + message
        clientSocket.sendto(message.encode(), (broadcastAddress, serverPort))
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        print(modifiedMessage.decode())
    elif Selection == 2:
        message = input('Input message(ND where N is the the number of the message you want to retrieve): ')
        message = hostName + " " + firstName + " " + lastName + " " + message
        clientSocket.sendto(message.encode(), (ip_address, serverPort))
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        print(modifiedMessage.decode())

    elif Selection == 3:
        print('Program is terminated.')
        clientSocket.close()
        break
    else:
        print('Invalid input')