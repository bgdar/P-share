import socket
import os


# example
# client = Client("192.168.1.42", port=5000)
# client.send_file("/home/user/Documents/fileku.txt")


class Client:
    def __init__(self, ip_tujuan: str, port: int = 5000):
        '''ip_tujuan = ip server dapatkan misalnya dari menu ip
           port       = port server tujuan 
        '''
        self.shareSucess = None
        self.__ip = ip_tujuan
        self.__port = port

    def send_file(self, filepath: str):
        if not os.path.exists(filepath):
            print(f"[!] File tidak ditemukan: {filepath}")
            return

        filename = os.path.basename(filepath)
        filesize = os.path.getsize(filepath)

        try:
            connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            connection.connect((self.ip, self.port))
            print(f"[📤] Mengirim file ke {self.ip}:{self.port} ...")

            # Kirim metadata
            connection.send(f"{filename}::{filesize}\n".encode())

            # tunggu ack dari server
            ack = connection.recv(1024).decode()
            if ack != 'OK':  # kirim byte OK
                print("[!] Gagal menerima ACK dari server.")
                return

            # Kirim isi file
            # 'rb' : baca binery nya
            with open(filepath, "rb") as f:
                while chunk := f.read(4096):
                    connection.send(chunk)

            print(f"[✓] File '{filename}' berhasil dikirim.")
            self.shareSucess = True
        except Exception as e:
            print(f"[!] Gagal mengirim file: {e}")
        finally:
            connection.close()
