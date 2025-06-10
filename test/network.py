import socket


def get_ip_address():
    try:
        # Buat koneksi palsu ke IP internet (tidak benar-benar mengirim data)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))  # Google DNS, hanya untuk tahu IP interface
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"  # fallback jika offline


# Contoh penggunaan
ip_lokal = get_ip_address()
print(f"IP LAN saat ini: {ip_lokal}")
