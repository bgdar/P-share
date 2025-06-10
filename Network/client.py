import socket
import os


# example
# client = Client("192.168.1.42", port=5000)
# client.send_file("/home/user/Documents/fileku.txt")

class Client:
    def __init__(self, ip_tujuan: str, port: int = 5000):
        '''ip_tujuan = ip server dapatkan misalnya dari menu ip'''
        self.ip = ip_tujuan
        self.port = port

    def send_file(self, filepath: str):
        if not os.path.exists(filepath):
            print(f"[!] File tidak ditemukan: {filepath}")
            return

        filename = os.path.basename(filepath)
        filesize = os.path.getsize(filepath)

        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((self.ip, self.port))
            print(f"[📤] Mengirim file ke {self.ip}:{self.port} ...")

            # Kirim metadata
            s.send(f"{filename}::{filesize}\n".encode())

            # Kirim isi file
            with open(filepath, "rb") as f:
                while chunk := f.read(4096):
                    s.send(chunk)

            print(f"[✓] File '{filename}' berhasil dikirim.")
        except Exception as e:
            print(f"[!] Gagal mengirim file: {e}")
        finally:
            s.close()
