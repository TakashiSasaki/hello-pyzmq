# key_generation.py
import zmq.auth
import os

# 必要なディレクトリが無ければ作成
certs_dir = 'certs'
if not os.path.exists(certs_dir):
    os.makedirs(certs_dir)

# 鍵の生成
server_public, server_secret = zmq.auth.create_certificates(certs_dir, 'server')
client_public, client_secret = zmq.auth.create_certificates(certs_dir, 'client')

print("Server Public Key:", server_public)
print("Server Secret Key:", server_secret)
print("Client Public Key:", client_public)
print("Client Secret Key:", client_secret)