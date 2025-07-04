# Task 2: Publishers and Subscribers

## Middleware Architectures Assignment 01

## **Objective**

Implement a **multi-client Publish/Subscribe middleware** using Python socket programming. The server must handle multiple concurrent clients, with each client acting as either a **Publisher** or a **Subscriber**. Messages from publishers are broadcast to all subscribers, enabling asynchronous communication between participants.
## **Features**

- **Concurrent Client Handling:** The server supports multiple clients simultaneously.
- **Role-based Clients:** Each client connects as either a **Publisher** or a **Subscriber** via a command-line argument.
- **Message Routing:**
    - Publishers send messages to the server.
    - Server forwards publisher messages to all connected subscribers.
    - Subscribers receive and display messages from publishers in real time.
- **CLI-based Interface:** All interactions occur via the command line, as required by assignment guidelines.
- **Graceful Termination:** Typing `terminate` disconnects the client from the server.


## **Directory Structure**

```
Task2_PubSub/
│
├── server.py           # Server implementation
├── client.py           # Client implementation
├── README.md           # This documentation file

```

## **How to Run**

### **1. Start the Server**

Open a terminal and run:

```bash
python server.py <PORT>
```

Example:

```bash
python server.py 5000
```


### **2. Start Clients**

Open multiple terminals for clients. Each client must specify:

- Server IP address
- Server port
- Role: `PUBLISHER` or `SUBSCRIBER`

**Publisher Example:**

```bash
python client.py 127.0.0.1 5000 PUBLISHER
```

**Subscriber Example:**

```bash
python client.py 127.0.0.1 5000 SUBSCRIBER
```


## **Usage Instructions**

- **Publishers:**
Type any message and press Enter to send to all subscribers.
Type `terminate` to disconnect.
- **Subscribers:**
Messages from publishers will appear automatically.
Type `terminate` to disconnect.


## **Sample Interaction**

**Server Output:**

```
Server listening on port 5000...
SUBSCRIBER connected from ('127.0.0.1', 54321)
PUBLISHER connected from ('127.0.0.1', 54322)
Received from PUBLISHER ('127.0.0.1', 54322): Hello, subscribers!
```

**Subscriber Output:**

```
[Received]: Hello, subscribers!
```

**Publisher Output:**

```
Enter message (type 'terminate' to exit): Hello, subscribers!
```


## **Notes**

- **Publisher messages are only delivered to subscribers.** Publishers do not receive messages from other publishers or themselves.
- **Multiple publishers and subscribers can be connected at the same time.**
- All communication is via the command line.
- Server handles multiple concurrent clients.
- Clients can be publishers or subscribers, as specified by the third command-line argument.
- Publisher messages are broadcast to all subscribers, not to other publishers.
- Application runs until `terminate` is entered by the user.


