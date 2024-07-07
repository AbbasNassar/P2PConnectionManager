from datetime import datetime
import socket

serverPort = 5051
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Allow broadcast
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
# Bind to all network interfaces and port 5051
serverSocket.bind(('0.0.0.0', serverPort))
print("The server is ready to receive")
serverHostName = socket.gethostname()

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

arrayOfMessages = []


while True:
    message, address = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode()
    words = modifiedMessage.split()
    clientHostName = ' '.join(words[:1])
    senderName = ' '.join(words[1:3])
    remaining_words = ' '.join(words[3:])
    # Ignore messages from the server itself
    if clientHostName != serverHostName:
        if len(words) != 0 and remaining_words[1] != 'D':
            arrayOfMessages.append(remaining_words)
            modifiedMessage = "Received a message from " + senderName + " at " + current_time
            print(modifiedMessage)
    else:
        if remaining_words[1] == 'D':
            if len(arrayOfMessages) == 0:
                serverSocket.sendto("No messages received".encode(), address)
            elif int(remaining_words[0]) <= len(arrayOfMessages):
                index = int(remaining_words[0])
                serverSocket.sendto(arrayOfMessages[index - 1].encode(), address)
            else:
                serverSocket.sendto("Index is out of range".encode(), address)
        else:
            serverSocket.sendto("Message sent successfully :)".encode(), address)