import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)

socket.connect("tcp://localhost:5555")


def send_messages(num_msg, msg_length):
    print(f"Sending {num_msg} message(s) of {msg_length:,} byte")
    data = b"a" * msg_length
    messages = [data for i in range(num_msg)]

    start = time.perf_counter()

    for message in messages:
        socket.send(message)
        socket.recv()

    end = time.perf_counter()
    print(f"Duration: {end - start}")


send_messages(300, 1000)
send_messages(1, 20000000)

socket.send(b"q")
