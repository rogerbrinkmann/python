import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)

socket.bind("tcp://127.0.0.1:5555")

while True:
    message = socket.recv()
    socket.send(message)

    if message == b'q':
        break

