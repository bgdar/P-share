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
        self.__host = host
        self.__port = port
        self.__save_folder = save_folder
        self.__server_socket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)
        os.makedirs(self.__save_folder, exist_ok=True)

    def start(self):
        '''mulai koneksi'''
        self.__server_socket.bind((self.__host, self.__port))
        self.__server_socket.listen()
        print(f"[🟢] Server menunggu koneksi di {self.__host}:{self.__port}")
        threading.Thread(target=self.__accept_connections, daemon=True).start()

    def __accept_connections(self):
        while True:
            conn, addr = self.__server_socket.accept()
            print(f"[+] Koneksi dari {addr}")
            threading.Thread(target=self.__handle_client,
                             args=(conn, addr), daemon=True).start()

    def __handle_client(self, conn: socket.socket, addr):
        """fungsi untuk menerima file dari client"""
        try:
            # Baca metadata (pakai pembacaan hingga newline)
            metadata_bytes = b""
            while not metadata_bytes.endswith(b"\n"):
                # terima data per byte 1 1 untuk membaca sampai '\n'
                chunk = conn.recv(1)
                if not chunk:
                    break
                metadata_bytes += chunk

            metadata = metadata_bytes.decode().strip()
            print("metadata yg di dapat:", metadata)

            # Pisahkan filename dan filesize
            filename, filesize = metadata.split("::")
            if filename:  # jika file name ada kirim pemberitahuan ke client
                conn.sendall(b'OK')

            filesize = int(filesize)
            print("file name", filename, "file size", filesize)

            # Simpan file
            filepath = os.path.join(self.__save_folder, filename)
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
