# di sini component untuk meng handle pengiriman file
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from network import Client
from kivy.clock import Clock
from kivy.uix.image import Image

from kivy.uix.widget import Widget

from kivy.core.window import Window

from components.Globalstate import Store
from components.assetsManagement import get_resource_path
from components.infoPopup import InfoPopup

from kivy.graphics import Color, Ellipse


class ClientSection(BoxLayout):

    def __init__(self):
        super().__init__()

        self.orientation = "vertical"

        # tukar posis jika file sudah di confirem maka mainBtn gunakan dan sebaliknya
        self.btnShare = None
        self.inputData = None
        self.mainLayout = None

        # tambahkan di awakl
        self.inputData = self.__InputData()
        self.add_widget(self.inputData)

        # windows yang bsai di gunakan untuk Update Layout
        self.update_layout(Window.size)
        Window.bind(size=self.on_window_resize)
        # self.add_widget(self.__InputIp())

    def __setClient(self, ipTujuan: str, port: int = 5000):
        '''gunakan untuk memasukan ip dan port server'''
        if ipTujuan:
            self.client = Client(ip_tujuan=ipTujuan, port=port)

    def mainBtn(self) -> FloatLayout:
        mainbtn = FloatLayout()
        toggleBtn = Button(text="confirm", size_hint=(0.3, 0.1), pos_hint={"right": 0.98, "top": 0.98}
                           )
        toggleBtn.bind(on_press=self._Confirms)

        mainbtn.add_widget(toggleBtn)

        return mainbtn

    def __InputData(self) -> BoxLayout:
        '''Form input untuk IP dan Port'''
        self.divTextInput = BoxLayout(
            orientation="vertical", padding=10, spacing=10, size_hint_x=None)
        self.textIp = TextInput(text="masukan ip tujuan ")
        self.textPort = TextInput(text="5000")

        btnConfirm = Button(text="Confirm Kirim")
        btnConfirm.bind(on_press=self._Confirms)

        self.divTextInput.add_widget(
            Label(text="Masukkan IP dan Port tujuan:"))
        self.divTextInput.add_widget(self.textIp)
        self.divTextInput.add_widget(self.textPort)
        self.divTextInput.add_widget(btnConfirm)

        return self.divTextInput

    def _Confirms(self, instace):
        # isi data client nya
        if self.inputData:
            try:
                ip = self.textIp.text.strip()
                port = int(self.textPort.text.strip())
                self.__setClient(ip, port)
            except Exception:
                InfoPopup('Format salah', 'warning', 2).Show_popup()
                return

            self.btnShare = self.__btn_send_file("send.png")
            self.mainLayout = self.mainBtn()
            self.mainLayout.add_widget(self.btnShare)

            self.add_widget(self.mainLayout)
            self.remove_widget(self.inputData)
            self.inputData = None

        elif self.mainLayout:
            self.remove_widget(self.mainLayout)
            self.mainLayout = None
            self.btnShare = None

            self.inputData = self.__InputData()
            self.add_widget(self.inputData)

    def __btn_send_file(self, icon=str) -> Button:
        '''
        @param icon : file img (file.png,file.jpg..)
        '''
        iconPath = get_resource_path('assets', 'icon', icon)

        btnIcon = Image(source=iconPath, allow_stretch=True)
        btn = Button(background_normal="", background_color=(
            0, 0, 0, 0), background_down="")

        with btn.canvas.before:
            Color(0.3, 0.5, 0.9, 1)
            elipse = Ellipse(size_hint=(None, None), size=(100, 100))
            self.update_graphics(elipse, btn.size, btn.pos)

        btn.bind(on_press=self._handleAction)
        btn.add_widget(btnIcon)

        return btn

    def _handleAction(self, instace):
        '''loop untuk tariding mengirim file yang di selecte'''
        # validasi file yang di simpan di store globa
        if len(Store.pathFileNames) == 1:
            self.client.send_file(Store.pathFileNames[0])
        elif len(Store.pathFileNames):
            for fileName in Store.pathFileNames:
                # kirim setelah 1 detik , jeda 1 detik
                Clock.schedule_once(
                    lambda dt: self.client.send_file(fileName), 1)
        else:
            print("file kosong di filename global")
            InfoPopup("kosong , pilih dulu file nya", 'info', 1.5).Show_popup()
            print("isi file global", Store.pathFileNames)
        # jalankan server untuk mengahdnle conetion dari client

        # Toggle balik ke form input
        if self.mainLayout:
            # Hapus tombol bulat
            self.remove_widget(self.mainLayout)
            self.mainLayout = None
            self.btnShare = None

            # Kembalikan ke input IP/port
            self.inputData = self.__InputData()
            self.add_widget(self.inputData)

    def update_graphics(self, instace, size, pos):
        '''instace : subtarget yang mengikuti size dan pos'''
        instace.size = size
        instace.pos = pos

    def on_window_resize(self, instance, size):
        ''''fungsi yang menerima perubahan untuk di gunakan '''
        self.update_layout(size)

    def update_layout(self, size):
        '''gunakan nantik untuk update layout jika ada perubahan  window'''
        width, height = size
        # manipulasi ukuran Windows
        # manipulasi ukuran windows 45%
        # RUMUS (misalnya ukuran windows 1280)
        # 1280 piksel * 0.45 = 576 piksel
        self.divTextInput.width = width * 0.45
