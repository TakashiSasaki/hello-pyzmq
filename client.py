# client.py
import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5555")  # TCPを使用

socket.setsockopt_string(zmq.SUBSCRIBE, "")  # すべてのメッセージを購読

while True:
    message = socket.recv_string()
    print(f"Received: {message}")
