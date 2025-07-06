import sys
import os

# JANGAN DI UBAH MENGGGUNAKAN NVIM Tambahkan parent directory ke Python path

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

# Import langsung dari file
sys.path.append(os.path.join(parent_dir, 'network'))
from network import Server , get_ip_address


ip = get_ip_address()
print(f"Server IP: {ip}")

server = Server(host=ip, port=5000)
server.start()

# Menjaga server tetap berjalan
try:
    while True:
        pass  # Server berjalan di background thread
except KeyboardInterrupt:
    print("\n[!] Server dihentikan")
