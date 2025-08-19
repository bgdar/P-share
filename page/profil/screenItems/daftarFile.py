from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDIconButton


class DaftarFile(Screen):
    def __init__(self, screen_manager: ScreenManager, **kwargs):
        super().__init__(**kwargs)
        self.screen_manager = screen_manager

        mainLAyout = MDBoxLayout(orientation="vertical")

        btnback = MDIconButton(icon="arrow-left-bold-box")
        mainLAyout.add_widget(btnback)

        btnback.bind(on_press=self._back)

        mainLAyout.add_widget(MDLabel(text="daftar file commmin soon "))

        self.add_widget(mainLAyout)

    def _back(self, instace):
        """ kembali ke halaman profil"""
        self.screen_manager.current = "profil"
