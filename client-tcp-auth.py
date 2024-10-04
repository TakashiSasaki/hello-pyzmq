# client-tcp.py
import zmq
import zmq.auth

# 認証をセットアップ
client_public_key, client_secret_key = zmq.auth.load_certificate('certs/client.key_secret')
server_public_key, _ = zmq.auth.load_certificate('certs/server.key')

context = zmq.Context()
socket = context.socket(zmq.SUB)

# 公開鍵認証の設定
socket.curve_secretkey = client_secret_key
socket.curve_publickey = client_public_key
socket.curve_serverkey = server_public_key

socket.connect("tcp://localhost:5555")  # TCPを使用

socket.setsockopt_string(zmq.SUBSCRIBE, "")  # すべてのメッセージを購読

while True:
    message = socket.recv_string()
    print(f"[CLIENT] Received: {message}")
