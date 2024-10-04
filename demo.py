# demo.py
import subprocess
import time

# サーバープロセスを起動
server_process = subprocess.Popen(["python", "server.py"])
time.sleep(1)  # サーバーの準備時間

# クライアントプロセスを起動
client_process = subprocess.Popen(["python", "client.py"])

# プロセスの終了を待つ
try:
    server_process.wait()
    client_process.wait()
except KeyboardInterrupt:
    server_process.terminate()
    client_process.terminate()
