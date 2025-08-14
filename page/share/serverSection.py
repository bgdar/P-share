from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
# from kivy.uix.button import Button
from kivymd.uix.button import MDIconButton

from kivymd.app import MDApp
import os
from threading import Thread

from network.server import Server, get_ip_address


class ServerSection(BoxLayout):

    def __init__(self):
        super().__init__()
        self.orientation = 'vertical'
        self.padding = 10

        self.server_thread = None  # simpan thread

        self.app = MDApp.get_running_app()

        # untuk sekarang port di atur static dulu
        # self.server = Server(get_ip_address(), port=5000)
        self.server = None
        self.hostIp = get_ip_address()

        divCenterBtn = BoxLayout(orientation="horizontal", padding=15)
        divCenterBtn.add_widget(self.__btn_send_file(icon='server'))

        self.add_widget(divCenterBtn)
        self.add_widget(Label(text="server"))

    def __btn_send_file(self, icon=str) -> MDIconButton:
        '''
        @param icon : file img (file.png,file.jpg..)
        '''
        btn = MDIconButton(icon=icon)

        # btn.bind(size=self.update_graphics,  pos=self.update_graphics)
        btn.bind(on_press=lambda x: self.handleAction(x))

        return btn

    def handleAction(self, instace):
        """jalankan server untuk mengahdnle conection dari client
         jalankan ke dalam Thread karena agar tidak meng freez ui
         Jika server thread sudah berjalan"""
        if self.server_thread and self.server_thread.is_alive():
            print("Server sudah jalan, hentikan.")
            self.app.show_popup("server di hentikan", "info", 2)
            self.server.stop()  # pastikan server punya .stop() yang aman
            self.server_thread.join()  # tunggu thread selesai
            self.server_thread = None
            self.server = None
        else:
            print("Server sedang dijalankan.")
            self.server = Server(host=self.hostIp, port=5000)
            self.app.show_popup("server berjalan", "info", 2)

            self.server_thread = Thread(target=self.server.start, daemon=True)
            self.server_thread.start()

        if self.server.clientError:
            self.app.show_popup(self.server.clientError, "error", 3)

        else:
            # InfoPopup("server aktive ", type='info', timer=1.5).Show_popup()
            print("server aktive")
        # print("Thread ada:", self.server_thread is not None)
        # print("Thread hidup:", self.server_thread.is_alive()
        #       if self.server_thread else None)

    def update_graphics(self, instace, *args):
        '''instace : subtarget yang mengikuti size dan pos'''
        #
        # btnsize = min(instace.height, instace.width)
        # self.elipse.size = (btnsize, btnsize)
        # self.elipse.pos = instace.pos
        pass
