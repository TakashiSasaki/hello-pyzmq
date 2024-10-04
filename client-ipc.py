# client-ipc.py
import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("ipc://zeromq-ipc")  # IPCを使用

socket.setsockopt_string(zmq.SUBSCRIBE, "")  # すべてのメッセージを購読

while True:
    message = socket.recv_string()
    print(f"[CLIENT] Received: {message}")
