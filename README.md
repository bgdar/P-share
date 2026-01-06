<h1 align="center"> P Share</h1>

<p align="center">
  Aplikasi berbagi file lokal yang berjalan melalui koneksi <b>TCP</b>. <br />
  Saat client membuka aplikasi, IP akan otomatis disimpan, <br />
  dan proses transfer dapat dimulai setelah client menambahkan alamat IP server.
</p>

### 🔧 Tech Stack

<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=python,git,vim,linux,supabase&perline=5" />
  </a> <br />
  <img src="https://img.shields.io/badge/Kivy-2.3.0-green?logo=appveyor" />
  <img src="https://img.shields.io/badge/Editor-Neovim-brightgreen?logo=neovim&logoColor=white" />
</p>

### Depedenci

1. `Kivy` : Library utama untuk GUI
2. `Plyer` : Untuk akses file fia Android/iOS
3. `TinyDB` : database local noSql
4. `kivyMd` : untuk **icons** dengan widget baru
   ![pictogrammers](https://pictogrammers.com/library/mdi/)
5. `suprabase` : untuk menyimpan data secara cloud
   pswd (databse) : P-share*-0w*

### page,

> fitur untuk aplikasi _Berbagi File Lokal_ | Python + kivy (tanpa internet, via socket TCP)

<div align="center">
<pre>
┌─────────────┐         WiFi LAN         ┌──────────────┐
│   Client    │  ─────────────────────▶  │    Server    │
│ (Pengirim)  │                          │  (Penerima)  │
└─────────────┘                          └──────────────┘
</pre>

</div>

- server menunggu file masuk dan client akan mengirimkan file
- salah satu aplikasi harus berperan sebagai server, dan yang lain sebagai client.

1.  **Halaman Utama (Dashboard)**

- management file
- Status koneksi: “Tersambung ke jaringan lokal” / “Tidak tersambung”

2.  **Share (Sender | Receiver)**
    **Serder** atau Client

- Tombol **Pilih File / Folder**
- Daftar file yang akan dikirim
- Input alamat IP perangkat penerima
- Tombol **Kirim**
- Progress bar pengiriman
- Notifikasi sukses/gagal
- Receiver\_\_ atau Server
- Tombol **Mulai Menerima**
- Menampilkan alamat IP lokal (untuk diketik oleh pengirim)
- Daftar file yang diterima
- Opsi folder tujuan penyimpanan
- Progress bar penerimaan

3. **Profil**

- Ganti port komunikasi (default: 9090)
- Folder default penyimpanan

4. **Login**
   handle login data di simpan di folder database

- sesion di simpan secara sementara di file sesion.json dan di kelola oleh sesion.py , sesuai di `Auth`

| Struktur Folder | Deskripsi                                                          |
| --------------- | ------------------------------------------------------------------ |
| `assets/file`   | Folder hasil upload pengguna (digunakan client & diatur di profil) |
| `tets/`         | Folder uji coba                                                    |
| `Network/`      | Backend & logika koneksi TCP                                       |
| `receiver/`     | Folder penyimpanan file hasil transfer dari client                 |
| `database`      | Folde menyimpan data (user login ,pathfile ,..)                    |
| `user`          | folder menyimpan UI untuk user (login dan register)                |

### Quote

- nama function yang mengembalikan Widget seperti , Boxlayout , Mdcard , ..
  penaman function nya di awali **widget<nama_function>**
- nama function yang menghandle buton di awalin dengan **_<nama_event>_<nama_btn>**

### Database sturctur | konsep

database.json = menyimpan isi database user (name,password,pathfile)
session.json = untuk menyimpan namauser yang sedang login saat ini untuk **cache**

`Auth` :
saat user memasukan nama otomatis sesion yang sebelumnya akan di drop dan di buat sesion baru yang akan di hapus ketika user logout , pada menu signUp data user yang di register akan di simpan di database

- sesion : selanjutnya saya tambah data waktu , yang di mana kalau sudah sampai batasnya , maka gunakan untk menghapus sesion

### daftar Warna

Warna-warna ini dikonversi ke format **Kivy rgba** (range 0–1), sehingga langsung bisa digunakan pada properti seperti `.md_bg_color`, `.text_color`, dll :

- `Hitam Abu Gelap (background utama)` = [27/255, 30/255, 35/255, 1] #1B1E23
- `Biru Neon` = [0.0, 0.639, 1.0, 1] # #00A3FF
- `Biru Laut` = [0.117, 0.564, 1.0, 1] # #1E90FF
- `Merah Terang` = [1.0, 0.231, 0.188, 1] # #FF3B30
- `Hijau Mint` = [0.596, 1.0, 0.596, 1] # #98FB98
- `Putih Bersih` = [1.0, 1.0, 1.0, 1] # #FFFFFF
- `Abu Lembut` = [0.75, 0.75, 0.75, 1] # #BFBFBF
- `Ungu Neon` = [0.6, 0.4, 1.0, 1] # #9966FF
- `Amber Hangat` = [1.0, 0.749, 0.0, 1] # #FFBF00
- `Kuning Lemon` = [1.0, 1.0, 0.4, 1] # #FFFF66
- `Cyan Soft` = [0.529, 0.808, 0.922, 1] # #87CEEB
  ** warna untuk Hover , Press , focus**
- `Hitam Abu Lebih Gelap (hover)` = [20/255, 22/255, 26/255, 1] #14161A
- `Biru Neon Gelap` = [0.0, 0.45, 0.71, 1] # #0073B5
- `Biru Laut Gelap` = [0.08, 0.4, 0.7, 1] # #1466B2
- `Merah Gelap` = [0.75, 0.15, 0.13, 1] # #BF261F
- `Hijau Mint Gelap` = [0.4, 0.8, 0.4, 1] # #66CC66
- `Putih Abu` = [0.9, 0.9, 0.9, 1] # #E6E6E6
- `Abu Gelap` = [0.5, 0.5, 0.5, 1] # #808080
- `Ungu Neon Gelap` = [0.45, 0.3, 0.75, 1] # #724CBE
- `Amber Gelap` = [0.8, 0.6, 0.0, 1] # #CC9900
- `Kuning Lemon Gelap` = [0.8, 0.8, 0.3, 1] # #CCCC4D
- `Cyan Soft Gelap` = [0.35, 0.6, 0.75, 1] # #5999BF
  warna untuk popup info
- `Success` = [0.2, 0.8, 0.4, 1] # #33CC66 — hijau lembut tapi mencolok
- `Error` = [0.9, 0.2, 0.2, 1] # #E63333 — merah terang kontras di latar gelap
- `Warning` = [1.0, 0.65, 0.0, 1] # #FFA500 — oranye terang (seperti amber neon)
- `Info` = [0.0, 0.75, 1.0, 1] # #00BFFF — biru terang segar untuk notifikasi/info

### konfigurasi

Konfigurasi Plyer (untuk Android)
Tambahkan ke buildozer.spec:

```bash
requirements = python3,kivy,plyer
android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE
```
