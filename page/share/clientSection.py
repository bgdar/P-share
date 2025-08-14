# di sini component untuk meng handle pengiriman file
from kivymd.app import MDApp
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton, MDRoundFlatButton

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
# from kivy.uix.textinput import TextInput
from kivymd.uix.boxlayout import MDBoxLayout
from network import Client
from kivy.clock import Clock
from kivy.uix.image import Image


from kivy.core.window import Window

from components.Globalstate import Store
from components.assetsManagement import get_resource_path
from components.infoPopup import InfoPopup

from kivy.graphics import Color, Ellipse


class ClientSection(BoxLayout):

    def __init__(self):
        super().__init__()
        self.orientation = "vertical"

        # Variabel utama
        self.inputData = None
        self.btnSend = None
        self.client: Client = None
        self.ip = ""
        self.port = 0

        self.app = MDApp.get_running_app()

        # Layout utama
        self.mainFloatLayout = FloatLayout()
        self.add_widget(self.mainFloatLayout)

        # Tambah tombol utama di awal
        self.btnSend = self.create_btn_send()
        self.add_widget(self.btnSend)

    def __set_client(self, ip_tujuan: str, port: int = 5000):
        """Set koneksi client."""
        if ip_tujuan and port > 0:
            self.client = Client(ip_tujuan=ip_tujuan, port=port)

    def create_btn_send(self) -> MDRaisedButton:
        """Tombol utama kirim file."""
        btn = MDRaisedButton(text="file-send", size_hint=(0.3, 0.1))
        btn.bind(on_press=self._confirm_send)
        return btn

    def __input_data(self) -> BoxLayout:
        """Form input IP & Port (tampil bila data belum diisi)."""
        self.divTextInput = MDBoxLayout(
            orientation="vertical",
            padding=10,
            spacing=10,
            size_hint_x=None
        )

        self.textIp = MDTextField(
            hint_text="Masukan IP server", max_text_length=16
        )
        self.textPort = MDTextField(
            text="5000", max_text_length=6
        )

        btnConfirm = MDRaisedButton(text="Confirm")
        btnConfirm.bind(on_press=self._confirms)

        self.divTextInput.add_widget(
            MDLabel(text="Masukkan IP dan Port tujuan:"))
        self.divTextInput.add_widget(self.textIp)
        self.divTextInput.add_widget(self.textPort)
        self.divTextInput.add_widget(btnConfirm)

        self.update_layout(Window.size)
        Window.bind(size=self.on_window_resize)
        return self.divTextInput

    def _confirm_send(self, instance):
        """Cek apakah sudah ada IP & Port, jika belum tampilkan form input."""
        if not self.ip or self.port == 0:
            # Tampilkan form input
            if self.btnSend in self.children:
                self.remove_widget(self.btnSend)
            self.inputData = self.__input_data()
            self.add_widget(self.inputData)
        else:
            # Jika IP & Port sudah diisi, langsung kirim file
            self._handle_action(instance)
            # informasi dari server
            self.app.show_popup(self.client.info, "info", 2)

    def _confirms(self, instance):
        """Konfirmasi input IP & Port dari form."""
        try:
            self.ip = self.textIp.text.strip()
            self.port = int(self.textPort.text.strip())

            if not self.ip or self.port <= 0:
                raise ValueError("IP atau Port tidak valid.")

            self.__set_client(ip_tujuan=self.ip, port=self.port)

            # Ganti form input dengan tombol kirim file
            if self.inputData in self.children:
                self.remove_widget(self.inputData)
            self.btnSend = self.create_btn_send()
            self.add_widget(self.btnSend)

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
                Clock.schedule_once(
                    lambda dt: self.client.send_file(fileName), 1)

    def on_window_resize(self, instance, size):
        self.update_layout(size)

    def update_layout(self, size):
        """Update ukuran layout input."""
        width, height = size
        if hasattr(self, 'divTextInput'):
            self.divTextInput.width = width * 0.45
