import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)

# the client connects to a socket at a specific address
socket.connect("tcp://localhost:5555")

while True:
    send_message = input()
    socket.send(send_message.encode())
    if send_message == 'q':
        break

    # client waits for message
    recv_message = socket.recv().decode()
    print(recv_message)
