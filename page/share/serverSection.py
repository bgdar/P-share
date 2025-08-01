from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse

from kivymd.app import MDApp
import os
from threading import Thread
from components.infoPopup import InfoPopup
from components.assetsManagement import get_resource_path

from network.server import Server, get_ip_address


class ServerSection(BoxLayout):

    def __init__(self):
        super().__init__()
        self.orientation = 'vertical'
        self.padding = 10

        self.server_thread = None  # simpan thread

        self.app = MDApp.get_running_app()

        # untuk sekarang port di atur static dulu
        self.server = Server(get_ip_address(), port=5000)

        divCenterBtn = BoxLayout(orientation="horizontal", padding=15)
        divCenterBtn.add_widget(self.__btn_send_file(icon='send.png'))

        self.add_widget(divCenterBtn)
        self.add_widget(Label(text="server"))

    def __btn_send_file(self, icon=str) -> Button:
        '''
        @param icon : file img (file.png,file.jpg..)
        '''
        icon_path = get_resource_path('assets', 'icon', icon)
        btnIcon = Image(source=icon_path, allow_stretch=True)
        btn = Button(background_normal="", background_color=(
            0, 0, 0, 0), background_down="")

        with btn.canvas.before:
            Color(0.3, 0.5, 0.9, 1)
            self.elipse = Ellipse(size_hint=(None, None), size=(100, 100))

        btn.bind(size=self.update_graphics,  pos=self.update_graphics)
        btn.bind(on_press=lambda x: self.handleAction(x))

        btn.add_widget(btnIcon)
        return btn

    def handleAction(self, instace):

        # jalankan server untuk mengahdnle conection dari client
        # jalankan ke dalam Thread karena agar tidak meng freez ui
        # Jika server thread sudah berjalan
        if self.server_thread and self.server_thread.is_alive():
            print("Server sudah jalan, hentikan.")
            self.app.show_popup("server di hentikan", "info", 2)
            self.server.stop()  # pastikan server punya .stop() yang aman
            self.server_thread.join()  # tunggu thread selesai
            self.server_thread = None
        else:
            print("Server sedang dijalankan.")
            self.app.show_popup("server berjalan", "info", 2)
            self.server_thread = Thread(target=self.server.start, daemon=True)
            self.server_thread.start()

            # validasi
        if len(self.server.clientError) != -1:
            # InfoPopup(self.server.clientError,
            # type="warning", timer=1.5).Show_popup()
            return self.server.clientError
        else:
            # InfoPopup("server aktive ", type='info', timer=1.5).Show_popup()
            print("server aktive")

    def update_graphics(self, instace, *args):
        '''instace : subtarget yang mengikuti size dan pos'''

        btnsize = min(instace.height, instace.width)
        self.elipse.size = (btnsize, btnsize)
        self.elipse.pos = instace.pos
