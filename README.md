# shareXPython

Apliaksi bekerja dengan coneksi TCP saat client membuka App maka akan menyimpan ip saat ini dari client
untuk terhubung maka client perlu menambah ip server maka file tarsfer bisa di lakukan


<prv>
    ┌─────────────┐         WiFi LAN         ┌──────────────┐
    │   Client    │  ─────────────────────▶  │    Server    │
    │ (Pengirim)  │                          │  (Penerima)  │
    └─────────────┘                          └──────────────┘
 </prv>
- server menunggu file masuk dan client akan mengirimkan file
-  salah satu aplikasi harus berperan sebagai server, dan yang lain sebagai client.

### **daftar halaman dan fitur** secara singkat untuk aplikasi *Berbagi File Lokal*  dengan Python + kivy (tanpa internet, via  socket TCP):

 1. **Halaman Utama (Dashboard)**

* Pilihan: **Kirim File** atau **Terima File**
* Status koneksi: “Tersambung ke jaringan lokal” / “Tidak tersambung”

 2. **Mode Pengirim (Sender)**

* Tombol **Pilih File / Folder**
* Daftar file yang akan dikirim
* Input alamat IP perangkat penerima
* Tombol **Kirim**
* Progress bar pengiriman
* Notifikasi sukses/gagal

 3. **Mode Penerima (Receiver)**

* Tombol **Mulai Menerima**
* Menampilkan alamat IP lokal (untuk diketik oleh pengirim)
* Daftar file yang diterima
* Opsi folder tujuan penyimpanan
* Progress bar penerimaan

 4. **Pengaturan (Opsional)**

* Ganti port komunikasi (default: 9090)
* Folder default penyimpanan
* Mode otomatis buka file setelah diterima

### konfigurasi 

Aktifkan virtual env di linux
```bash
source shareXPython/bin/activate
``` 


### folder

- `tets` : uji coba 

- `Network` : folder konfigurasi backend untuk sinyal proses pengiriman file 
    1. client.py = adalah tiap tiap client yang terhubung 


