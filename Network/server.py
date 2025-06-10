# network/server.py
import socket
import threading
import os

# example
# ip = get_ip_address()
# server = Server(host=ip, port=5000)
# server.start()


class Server:
    def __init__(self, host="0.0.0.0", port=5000, save_folder="received"):
        self.host = host
        self.port = port
        self.save_folder = save_folder
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        os.makedirs(self.save_folder, exist_ok=True)

    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()
        print(f"[🟢] Server menunggu koneksi di {self.host}:{self.port}")
        threading.Thread(target=self.accept_connections, daemon=True).start()

    def accept_connections(self):
        while True:
            conn, addr = self.server_socket.accept()
            print(f"[+] Koneksi dari {addr}")
            threading.Thread(target=self.handle_client,
                             args=(conn, addr), daemon=True).start()

    def handle_client(self, conn: socket.socket, addr):
        """fungsi untuk menerima file dari client"""
        try:
            metadata = conn.recv(1024).decode()
            filename, filesize = metadata.strip().split("::")
            filesize = int(filesize)

            filepath = os.path.join(self.save_folder, filename)
            with open(filepath, "wb") as f:
                received = 0
                while received < filesize:
                    data = conn.recv(4096)
                    if not data:
                        break
                    f.write(data)
                    received += len(data)

            print(f"[✓] File diterima dari {
                  addr} -> {filename} ({filesize} byte)")
        except Exception as e:
            print(f"[!] Error dari {addr}: {e}")
        finally:
            conn.close()


def get_ip_address():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

# def received_folder(): #fungsi untuk mengecek apakah folder ada jika tidak ada buatkan ,gunakna di class nantik
