import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)

# the server binds to a socket
# it can listen to a specific or to any address
socket.bind("tcp://*:5555")

while True:
    # server waits for message
    message = socket.recv()
    if message == b'q':
        break

    socket.send(message.upper())