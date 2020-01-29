import zmq
import sys

if len(sys.argv) !=2:
    port = 5555
else:
    try:
        port = int(sys.argv[1])
    except ValueError:
        print("Must enter port number")
        exit(-1)


context = zmq.Context()
socket = context.socket(zmq.REQ)

# the client connects to a socket at a specific address
socket.connect(f"tcp://localhost:{port}")

while True:
    send_message = input()
    socket.send(send_message.encode())
    if send_message == 'q':
        break

    # client waits for message
    recv_message = socket.recv().decode()
    print(recv_message)
