# di sini component untuk meng handle pengiriman file

from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from network import Client
from kivy.clock import Clock
from kivy.uix.image import Image

from components.Globalstate import Store

import os
import time
from kivy.graphics import Color, Ellipse


class ClientSection(BoxLayout):

    def __init__(self):
        super().__init__()

        self.orientation = "vertical"
        # pada bagian ini hanya button saja dulu yang terlihat
        self.add_widget(self.__btn_send_file("send.png"))

    def setClient(self, ipTujuan: str, port: int):
        '''gunakan untuk memasukan ip server'''
        if ipTujuan:
            self.client = Client(ip_tujuan=ipTujuan, port=port)

    def __btn_send_file(self, icon=str) -> Button:
        '''
        @param icon : file img (file.png,file.jpg..)
        '''
        # pathIcon = os.path.join(os.path.dirname(__file__), "../assets/icon/")

        base_dir = os.path.dirname(os.path.abspath(__file__))

        # Naik dua folder: dari /page/share/ -> ke root project
        icon_path = os.path.join(base_dir, "..", "..", "assets", "icon", icon)
        full_path = os.path.abspath(icon_path)

        print("Final icon path:", full_path)
        print("Exists?", os.path.exists(full_path))

        print("Exists?", os.path.exists(full_path))

        btnIcon = Image(source=full_path, allow_stretch=True)
        btn = Button(background_normal="", background_color=(
            0, 0, 0, 0), background_down="")

        with btn.canvas.before:
            Color(0.3, 0.5, 0.9, 1)
            elipse = Ellipse(size_hint=(None, None), size=(100, 100))
            self.update_graphics(elipse, btn.size, btn.pos)

        btn.bind(on_press=self._handleAction)

        btn.add_widget(btnIcon)
        return btn

    def _handleAction(self):
        '''loop untuk tariding mengirim file yang di selecte'''
        if len(Store.pathFileNames == 1):
            self.client.send_file(Store.pathFileNames)
        elif len(Store.pathFileNames):
            for fileName in Store.pathFileNames:
                # kirim setelah 1.5 detik , jeda 1.5 detik
                Clock.schedule_once(
                    self.client.send_file(Store.pathFileNames), 1.5)
        else:
            print("file kosong di filename global")
        # jalankan server untuk mengahdnle conetion dari client

    def update_graphics(self, instace, size, pos):
        '''instace : subtarget yang mengikuti size dan pos'''
        instace.size = size
        instace.pos = pos
