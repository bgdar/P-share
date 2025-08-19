from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel

# from kivy.uix.button import Button
from kivymd.uix.button import MDIconButton

from kivymd.app import MDApp
import os
from threading import Thread
from typing import Callable

from network.server import Server, get_ip_address


class ServerSection(BoxLayout):

    def __init__(self):
        super().__init__()
        self.orientation = "vertical"
        self.padding = 10

        self.app = MDApp.get_running_app()

        # untuk sekarang port di atur static dulu
        # self.server = Server(get_ip_address(), port=5000)
        self.server = None
        self.server_thread = None  # simpan thread
        self.hostIp = get_ip_address()

        # self.mainLayout = FloatLayout()
        self.mainLayout = MDBoxLayout(orientation="horizontal", spacing="10dp")

        self.mainLayout.add_widget(self.serctionLeft())
        self.mainLayout.add_widget(self.btn_send())
        self.mainLayout.add_widget(self.serctionRight())

        self.add_widget(self.mainLayout)

    def serctionLeft(self) -> MDCard:
        layout = MDCard(
            orientation="vertical",
            radius=[15],
            md_bg_color=[0.75, 0.75, 0.75, 1],
            size_hint=(0.5, 1),
            padding=10,
        )
        layout.add_widget(MDLabel(text="server"))
        return layout

    def btn_send(self) -> MDCard:
        layout = MDCard(
            orientation="vertical",
            radius=[50],
            md_bg_color=[0.5, 0.5, 0.5, 1],
            padding=10,
        )
        btn: MDIconButton = self._btn(self.handleServerStart, icon="server")
        btn.disabled = self.is_server_running()
        print("infon ", self.is_server_running())
        layout.add_widget(btn)
        return layout

    def serctionRight(self) -> MDCard:
        layout: MDCard = MDCard(
            orientation="vertical",
            radius=[15],
            md_bg_color=[0.75, 0.75, 0.75, 1],
            padding=10,
            size_hint=(0.5, 1),
        )
        btnClose: MDIconButton = self._btn(self.handleServerClose, icon="close")
        # Disable close button if server is not running
        btnClose.disabled = self.is_server_running()
        print("infon ", self.is_server_running())
        layout.add_widget(btnClose)
        return layout

    def handleServerClose(self, instace):
        if self.is_server_running():
            print("Server sudah jalan, hentikan.")
            self.app.show_popup("server di hentikan", "info", 2)
            self.server.stop()  # pastikan server punya .stop() yang aman
            self.server_thread.join()  # tunggu thread selesai
            self.server_thread = None
            self.server = None

    def handleServerStart(self, instace):
        if not self.is_server_running():
            print("Server sedang dijalankan.")
            self.server = Server(host=self.hostIp, port=5000)
            self.app.show_popup("server berjalan", "info", 2)

            self.server_thread = Thread(target=self.server.start, daemon=True)
            self.server_thread.start()

    def _btn(
        self, handleAction: Callable[[MDIconButton], None], icon=str
    ) -> MDIconButton:
        """
        @param icon : file img (file.png,file.jpg..)
        """
        btn = MDIconButton(icon=icon, pos_hint={"center_x": 0.5, "center_y": 0.5})
        # btn.bind(size=self.update_graphics,  pos=self.update_graphics)
        btn.bind(on_press=handleAction)
        return btn

    def is_server_running(self) -> bool:
        return self.server_thread and self.server_thread.is_alive() and self.server

    def update_graphics(self, instace, *args):
        """instace : subtarget yang mengikuti size dan pos"""
        #
        # btnsize = min(instace.height, instace.width)
        # self.elipse.size = (btnsize, btnsize)
        # self.elipse.pos = instace.pos
        pass
