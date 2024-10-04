# server-ipc.py
import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("ipc://zeromq-ipc")  # IPCを使用

time.sleep(1)

while True:
    message = "Hello from the server!"
    socket.send_string(message)
    print(f"[SERVER] Sent: {message}")
    time.sleep(1)  # 1秒ごとにメッセージを送信
