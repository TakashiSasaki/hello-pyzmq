# client-tcp.py
import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5555")  # TCPを使用

socket.setsockopt_string(zmq.SUBSCRIBE, "")  # すべてのメッセージを購読

# 接続確認のためのタイムアウト設定
timeout = 10  # 10秒間のタイムアウト
poller = zmq.Poller()
poller.register(socket, zmq.POLLIN)

start_time = time.time()
while True:
    socks = dict(poller.poll(timeout * 1000))
    if socket in socks and socks[socket] == zmq.POLLIN:
        message = socket.recv_string()
        print(f"[CLIENT] Received: {message}")
    elif time.time() - start_time > timeout:
        print("[CLIENT ERROR] Authentication failed or server not reachable within timeout period.")
        break