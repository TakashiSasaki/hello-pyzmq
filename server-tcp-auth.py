# server-tcp-auth.py
import zmq
import zmq.auth
import time

# 認証をセットアップ
server_public_key, server_secret_key = zmq.auth.load_certificate('certs/server.key_secret')

context = zmq.Context()
socket = context.socket(zmq.PUB)

# 公開鍵認証の設定
socket.curve_secretkey = server_secret_key
socket.curve_publickey = server_public_key
socket.curve_server = True  # サーバーモードであることを示す

socket.bind("tcp://*:5555")  # TCPを使用

time.sleep(1)

while True:
    message = "Hello from the server!"
    socket.send_string(message)
    print(f"[SERVER] Sent: {message}")
    time.sleep(1)  # 1秒ごとにメッセージを送信
