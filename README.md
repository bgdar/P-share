<h1 align="center"> P Share</h1>

<p align="center">
  Aplikasi berbagi file lokal yang berjalan melalui koneksi <b>TCP</b>. <br />
  Saat client membuka aplikasi, IP akan otomatis disimpan, <br />
  dan proses transfer dapat dimulai setelah client menambahkan alamat IP server.
</p>

---

## 🔧 Tech Stack

<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=python,git,vim,linux&perline=4" />
  </a> <br />
  <img src="https://img.shields.io/badge/Kivy-2.3.0-green?logo=appveyor" />
  <img src="https://img.shields.io/badge/Editor-Neovim-brightgreen?logo=neovim&logoColor=white" />
</p>

---

### **daftar page,fitur  untuk aplikasi *Berbagi File Lokal* | Python + kivy (tanpa internet, via  socket TCP):

```
┌─────────────┐         WiFi LAN         ┌──────────────┐
│   Client    │  ─────────────────────▶  │    Server    │
│ (Pengirim)  │                          │  (Penerima)  │
└─────────────┘                          └──────────────┘
```

- server menunggu file masuk dan client akan mengirimkan file
-  salah satu aplikasi harus berperan sebagai server, dan yang lain sebagai client.

 1. **Halaman Utama (Dashboard)**
* management file 
* Status koneksi: “Tersambung ke jaringan lokal” / “Tidak tersambung”

 2. **Share (Sender | Receiver)**
__Serder__ atau Client
* Tombol **Pilih File / Folder**
* Daftar file yang akan dikirim
* Input alamat IP perangkat penerima
* Tombol **Kirim**
* Progress bar pengiriman
* Notifikasi sukses/gagal
__Receiver__ atau Server
* Tombol **Mulai Menerima**
* Menampilkan alamat IP lokal (untuk diketik oleh pengirim)
* Daftar file yang diterima
* Opsi folder tujuan penyimpanan
* Progress bar penerimaan

3. Profil 
* Ganti port komunikasi (default: 9090)
* Folder default penyimpanan

## project Screenshot
<p align="center">
  <img src="./assets/img/sampel.png" alt="sampel project" width="70%" />
</p>


### konfigurasi 

Aktifkan virtual env di linux
```bash
source shareXPython/bin/activate
``` 

### Dependencies
Kivy: Library utama untuk GUI

Plyer: Untuk akses file Android/iOS

Konfigurasi Plyer (untuk Android)
Tambahkan ke buildozer.spec:
```bash
requirements = python3,kivy,plyer
android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE
```

---
| Struktur Folder     | Deskripsi                                                          |
| ------------------- | ------------------------------------------------------------------ |
| `assets/file`       | Folder hasil upload pengguna (digunakan client & diatur di profil) |
| `tets/`             | Folder uji coba                                                    |
| `Network/`          | Backend & logika koneksi TCP                                       |
| `Network/client.py` | Modul client socket                                                |
| `receiver/`         | Folder penyimpanan file hasil transfer dari client                 |

