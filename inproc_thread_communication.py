import zmq
import threading
import time

# サーバースレッド
def server_thread(context):
    socket = context.socket(zmq.PAIR)
    socket.bind("inproc://test")  # In-process通信を使用

    while True:
        message = "Hello from the server!"
        socket.send_string(message)
        print(f"Server sent: {message}")
        time.sleep(1)

# クライアントスレッド
def client_thread(context):
    socket = context.socket(zmq.PAIR)
    socket.connect("inproc://test")  # In-process通信を使用

    while True:
        message = socket.recv_string()
        print(f"Client received: {message}")

# 同一のzmqコンテキストを使用
context = zmq.Context()

# サーバースレッドを起動
server = threading.Thread(target=server_thread, args=(context,))
server.start()

# クライアントスレッドを起動
client = threading.Thread(target=client_thread, args=(context,))
client.start()

# メインスレッドを維持するための適当な処理
server.join()
client.join()
