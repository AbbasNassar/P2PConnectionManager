# UDP Client-Server Communication System

This project implements a simple client-server communication system using UDP sockets. The client can send messages to peers, request specific messages from the server, and terminate the connection. The server handles receiving messages from clients, storing them, and responding to client requests for specific messages.

## Prerequisites
* A local network environment: `Radmin VPN` software simulates connecting remote devices on one Ethernet switch.

## Usage
1. **Start the server:** The server will start and bind to port `5051`. It will be ready to receive messages.
2. **Start the client:** The client provides a menu with three options:
   * Send a message to peers.
   * Retrieve a message from the server.
   * Exit the program.

### Client-Side
The client allows users to:
* Send a message to peers by broadcasting it.
* Request a specific message from the server by specifying its index.
* Terminate the connection.

### Server-Side
The server handles:
* Receiving messages from clients and storing them.
* Responding to client requests for specific messages based on their index.
* Ignoring messages sent by the server itself.

## Code Structure
### `client.py`
* **Initialization:**
  * Sets up client details such as `firstName`, `lastName`, `serverPort`, `hostName`, `ip_address`, `defaultGateway`, `subnetMask`, and `broadcastAddress`.
  * Creates a UDP socket and allows broadcasting.
* **Main Loop:**
  * Prompts the user to select the type of message to send.
  * Sends messages to peers or retrieves messages from the server based on user input.
  * Closes the socket and exits the program when the user chooses to exit.

### `main.py`
* **Initialization:**
  * Sets up the server port and creates a UDP socket.
  * Allows broadcast and binds the socket to all network interfaces on port 5051.
  * Initializes a list to store received messages.
* **Main Loop:**
  * Waits for incoming messages.
  * Processes incoming messages by appending them to the message list if they are from clients.
  * Sends the requested message back to the client if the message retrieval command is received.

## Notes
* Ensure the server is running before attempting to send or retrieve messages using the client.
* The server listens on port 5051 and accepts messages from any network interface.
