# demo-tcp-auth-fail.py
import subprocess
import time

# サーバープロセスを起動
server_process = subprocess.Popen(["python", "server-tcp-auth.py"])
time.sleep(1)  # サーバーの準備時間

# 鍵を持たないクライアントプロセスを起動（認証に失敗することを確認するため）
client_process = subprocess.Popen(["python", "client-tcp.py"], stderr=subprocess.PIPE)

# プロセスの終了を待つ
try:
    start_time = time.time()
    timeout = 10  # 10秒間待機してから接続確認
    while True:
        if time.time() - start_time > timeout:
            if client_process.poll() is None:
                print("[CLIENT ERROR] Client failed to authenticate within the timeout period.")
                client_process.terminate()
                break
        if server_process.poll() is not None and client_process.poll() is not None:
            break
except KeyboardInterrupt:
    server_process.terminate()
    client_process.terminate()