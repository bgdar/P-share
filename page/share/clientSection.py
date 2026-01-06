# di sini component untuk meng handle pengiriman file
from kivymd.app import MDApp
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDRaisedButton, MDRoundFlatButton, MDRectangleFlatButton
from kivymd.uix.boxlayout import MDBoxLayout

from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout

from kivy.properties import StringProperty

# from kivy.uix.textinput import TextInput
from network import Client
from kivy.clock import Clock
from kivy.uix.image import Image

from kivy.graphics import Color, Ellipse, RoundedRectangle
from kivy.core.window import Window
from kivy.uix.widget import Widget

from components.Globalstate import Store
from components.assetsManagement import get_all_files


from typing import Tuple


class ClientSection(BoxLayout):
    # observable property  : ynag bisa di bind ke UI
    lenSelectPathFile = StringProperty()

    def __init__(self):
        super().__init__()
        self.orientation = "vertical"
        self.spacing = 10
        # self.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        # Variabel utama
        self.inputData = None
        self.btnSend = None
        self.client: Client = None
        self.layoutData: MDCard = None  # ini card yang di sectionData

        # simpan ip
        self.ip = ""
        self.port = 0

        # Initialize divGridContainer early to avoid AttributeError
        self.divGridContainer = None

        self.app = MDApp.get_running_app()
        # Layout utama
        self.mainlayout = MDBoxLayout(orientation="horizontal")
        # manipulasi windows
        self.update_window(windowSize=Window.size)
        Window.bind(size=self.on_window_resize)

        self._update_selected_files_count()  # update counter awal

        # Tambah tombol utama di awal
        # self.btnSend = self.create_btn_send()

        # WIDGET UTAMAN DI ClientSection
        self.mainlayout.add_widget(self.sectionFile())
        self.mainlayout.add_widget(self.sectionData())

        self.add_widget(self.mainlayout)
        self.add_widget(self.sectionFooter())

    def __set_client(self, ip_tujuan: str, port: int = 5000):
        """Set koneksi client."""
        if ip_tujuan and port > 0:
            self.client = Client(ip_tujuan=ip_tujuan, port=port)

    def __InputData(self) -> BoxLayout:
        """Form input IP & Port (tampil bila data belum diisi)."""
        divTextInput = MDBoxLayout(
            orientation="vertical",
            padding=10,
            spacing=10,
            size_hint_x=None,
            pos_hint={"center_x": 0.5, "center_y": 0.5},
        )
        # gambar bacground
        with divTextInput.canvas.before:
            Color(0.75, 0.75, 0.75, 1)
            self.bgInputText = RoundedRectangle(
                size=divTextInput.size, pos=divTextInput.pos
            )

        divTextInput.bind(pos=self.update_bg, size=self.update_bg)

        self.textIp = MDTextField(hint_text="Masukan IP server", max_text_length=16)
        self.textPort = MDTextField(text="5000", max_text_length=6)

        btnConfirm = MDRaisedButton(text="Confirm")
        btnConfirm.bind(on_press=self._confirm_data)

        divTextInput.add_widget(MDLabel(text="Masukkan IP dan Port tujuan:"))
        divTextInput.add_widget(self.textIp)
        divTextInput.add_widget(self.textPort)
        divTextInput.add_widget(btnConfirm)

        self.update_layout(Window.size)
        Window.bind(size=self.on_window_resize)
        return divTextInput

    def create_btn_send(self) -> MDRaisedButton:
        """buat Tombol utama kirim file."""
        btn = MDRectangleFlatButton(
            icon="send", pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        btn.bind(on_press=self._confirm_send)
        return btn

    def _confirm_send(self, instance):
        """Cek apakah sudah ada IP & Port, jika belum tampilkan form input."""

        """ ada yang salah pada pengecekan btnSend di dalam layoutData yang type MDCard"""

        if not self.ip or self.port == 0:
            # Tampilkan form input
            if self.btnSend in self.layoutData.children:
                print("tombol ada di layoutData")
                self.layoutData.remove_widget(self.btnSend)
            self.inputData = self.__InputData()
            self.layoutData.add_widget(self.inputData)
        elif self.client.info:
            self.app.show_popup(self.client.info, "info", 2)
        else:
            # Jika IP & Port sudah diisi, langsung kirim file
            self._handle_action(instance)
            # informasi dari server
            self.app.show_popup("file sending", "info", 2)

    def _confirm_data(self, instance):
        """Konfirmasi input IP & Port dari form."""
        """ ada yang salah pada pengecekan btnSend di dalam layoutData yang type MDCard
"""
        try:
            self.ip = self.textIp.text.strip()
            self.port = int(self.textPort.text.strip())

            if not self.ip or self.port <= 0:
                self.app.show_popup(
                    "IP atau Port tidak valid", "warning", 2
                )  # tampilkna popup
                raise ValueError("IP atau Port tidak valid.")

            self.__set_client(ip_tujuan=self.ip, port=self.port)

            # Ganti form input dengan tombol kirim file kembali
            if self.inputData in self.layoutData.children:
                self.layoutData.remove_widget(self.inputData)
            self.btnSend = self.create_btn_send()
            self.layoutData.add_widget(self.btnSend)

        except ValueError:
            self.app.show_popup("Format IP/Port salah", "warning", 2)

    def _handle_action(self, instance):
        """Proses pengiriman file."""
        if not self.client:
            self.app.show_popup("Isi dulu IP dan Port", "warning", 2)
            return

        if len(Store.pathFileNames) == 0:
            self.app.show_popup("Kosong, pilih file dulu", "info", 1.5)
            return

        if len(Store.pathFileNames) == 1:
            self.client.send_file(Store.pathFileNames[0])
        else:
            for fileName in Store.pathFileNames:
                Clock.schedule_once(lambda dt: self.client.send_file(fileName), 1)

    # BAGIAN KIRI UNTUK PEMILIHAN FILE NYA ⚠️
    def sectionFile(self) -> MDCard:
        layout = MDCard(
            orientation="vertical",
            md_bg_color=[0.9, 0.9, 0.9, 1],
            padding=10,
            size_hint=(0.5, 1),
        )
        # bind untuk menampilkan data terbaru dari div container
        Store.bind(isRealoadFile=self._reaload_divGridContainer)
        scroll = ScrollView(bar_color=[0.23, 0.4, 0.5, 0.5], do_scroll_y=True)

        self.divGridContainer = GridLayout(size_hint_y=None, cols=1, spacing=(0, 10))

        self.divGridContainer.bind(
            minimum_height=self.divGridContainer.setter("height")
        )
        # isi setiap file nya di sini
        # baca file yang ada di folder assert/file
        files = get_all_files()
        for (
            file
        ) in (
            files
        ):  # ini sialisasi awal dan berubah nantik ketika _toggle_show_files berubah
            self.divGridContainer.add_widget(
                self.__btn_file(file["nameFile"], file["pathFile"])
            )

        # Tampilkan container jika ada file, sembunyikan jika tidak ada
        if files:
            self.divGridContainer.opacity = 1
            self.divGridContainer.disabled = False
        else:
            self.divGridContainer.opacity = 0
            self.divGridContainer.disabled = True
        scroll.add_widget(self.divGridContainer)

        layout.add_widget(scroll)
        # Buat label untuk jumlah file
        # Label yang akan berubah
        labelPathFile = MDLabel()
        labelPathFile.bind(size=labelPathFile.setter("text_size"))
        labelPathFile.text = self.lenSelectPathFile
        # lenSelectPathFile property di-bind dengan benar ke label menggunakan lambda function:
        self.bind(
            lenSelectPathFile=lambda instance, value: setattr(
                labelPathFile, "text", f"Selected: {value} file"
            )
        )
        layout.add_widget(labelPathFile)

        return layout

    def _reaload_divGridContainer(self, instance=None, value=None):
        """Di gunakan jika ada perubahan di store"""
        self.divGridContainer.clear_widgets()  # hapus isinya
        # tambhakan ulang
        for file in get_all_files():
            self.divGridContainer.add_widget(
                self.__btn_file(file["nameFile"], file["pathFile"])
            )
        # setelah semua di realod atur kembali ke False
        Store.toogle_realoadFile(False)
        # Tampilkan kembali container setelah reload
        self.divGridContainer.opacity = 1
        self.divGridContainer.disabled = False
        # Update counter setelah reload
        self._update_selected_files_count()

    def __btn_file(self, filename: str, pathFile: str) -> BoxLayout:

        btn = MDRaisedButton(text=filename)
        divbutton = BoxLayout(orientation="vertical", size_hint_y=None, height=30)
        divStatusClick = Widget(size_hint=(None, None), size=(25, 25))
        with divStatusClick.canvas.before:
            Color(1, 0, 0, 1)
            ellips = Ellipse(pos=divStatusClick.pos, size=(15, 15))
            # tetapkan atribut val ke ellips
        divStatusClick.bind(pos=lambda instance, val: setattr(ellips, "pos", val))
        # letakkan di bawah bind agar btn tidak tertimpa
        divbutton.add_widget(btn)
        # kondisi jika divInfoClick muncul tambahkan dan jika tidak hapus kembali
        btn.bind(
            on_press=lambda x: self.__trigrer_btn_file(
                x, pathFile, divbutton, divStatusClick
            )
        )

        return divbutton

    def __trigrer_btn_file(
        self, instance, pathFile: str, divbutton: BoxLayout, divStatusClick: Widget
    ):
        """fungsi yang terjadi saat setiap file di tekan"""
        print("path yang di dapat :", pathFile)
        if divStatusClick not in divbutton.children:
            divbutton.add_widget(divStatusClick)
            Store.setPathFileName(pathFile)
            # perbaharui
            self._update_selected_files_count()
        else:
            divbutton.remove_widget(divStatusClick)
            Store.removePathFileName(pathFile)
            # perbaharui
            self._update_selected_files_count()

    def _update_selected_files_count(self):
        """Update count selected files dan trigger property change"""
        self.lenSelectPathFile = str(len(Store.pathFileNames))

    def sectionData(self) -> MDCard:
        """ini section yang di sebelah kanan , untuk tombol dan"""
        self.layoutData = MDCard(
            orientation="vertical",
            md_bg_color=[0.9, 0.9, 0.9, 1],
            padding=10,
            size_hint=(0.5, 1),
        )
        # ada yang salah pada pengecekan btnSend di dalam layoutData yang type MDCard
        # daftar kan duluan untuk tombol btnSend
        self.btnSend = self.create_btn_send()
        self.layoutData.add_widget(self.btnSend)

        return self.layoutData

    # BAGIAN KIRI UNTUK PEMILIHAN FILE NYA ⚠️
    def sectionFooter(self) -> MDCard:
        layout = MDCard(
            orientation="horizontal",
            md_bg_color=[0.75, 0.75, 0.75, 1],
            size_hint_y=None,
            height="50dp",
            radius=[10],
        )
        layout.add_widget(MDLabel(text="footer"))
        return layout

    def on_window_resize(self, instance, size):
        self.update_layout(size)

    def update_layout(self, size):
        """Update ukuran layout input."""
        width, height = size
        if hasattr(self, "divTextInput"):
            self.divTextInput.width = width * 0.45

    def update_bg(self, instance, *arg):
        "gunakan untuk update bg (size , pos)"
        self.bgInputText.pos = instance.pos
        self.bgInputText.size = instance.size

    def on_window_resize(self, instance, windowSize):
        self.update_window(windowSize)

    def update_window(self, windowSize: Tuple[int, int]):
        """isi setiap perubahan windwos nya"""
        width, height = windowSize
        # update untuk grid
        if self.divGridContainer is not None:
            self.divGridContainer.cols = 2 if width >= 700 or height >= 850 else 1

        # ubah ukuran secton File dan Section Buttom
        self.mainlayout.orientation = (
            "horizontal" if width >= 700 or height >= 850 else "vertical"
        )
