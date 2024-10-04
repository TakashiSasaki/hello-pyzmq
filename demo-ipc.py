# demo-ipc.py
import subprocess
import time

# サーバープロセスを起動
server_process = subprocess.Popen(["python", "server-ipc.py"])
time.sleep(1)  # サーバーの準備時間

# クライアントプロセスを起動
client_process = subprocess.Popen(["python", "client-ipc.py"])

# プロセスの終了を待つ
try:
    server_process.wait()
    client_process.wait()
except KeyboardInterrupt:
    server_process.terminate()
    client_process.terminate()
