from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel


class DaftarFile(Screen):
    def __init__(self, screen_manager: ScreenManager, **kwargs):
        super().__init__(**kwargs)
        self.screen_manager = screen_manager

        mainLAyout = MDBoxLayout(orientation="vertical")
        mainLAyout.add_widget(MDLabel(text="daftar file "))

        self.add_widget(mainLAyout)

    def _back(self):
        """ kembali ke halaman signUp"""
        self.screen_manager.current = "signUp"
