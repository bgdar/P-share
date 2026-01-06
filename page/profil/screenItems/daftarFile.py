from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDIconButton, MDFlatButton
from kivymd.uix.scrollview import ScrollView

from components.assetsManagement import get_all_files


class DaftarFile(Screen):
    def __init__(self, screen_manager: ScreenManager, **kwargs):
        super().__init__(**kwargs)
        self.screen_manager = screen_manager

        mainLayout = MDBoxLayout(orientation="vertical")

        mainLayout.add_widget(self.widgetHeader())
        mainLayout.add_widget(self.widgetDaftarFile())

        self.add_widget(mainLayout)

    def on_press_back(self, instace):
        """kembali ke halaman profil"""
        self.screen_manager.current = "profil"

    def widgetHeader(self) -> MDBoxLayout:
        headerLaypout = MDBoxLayout(orientation="horizontal", spacing=10)

        btnback = MDIconButton(icon="arrow-left-bold-box")
        btnback.bind(on_press=self.on_press_back)

        headerLaypout.add_widget(btnback)
        return headerLaypout

    def widgetDaftarFile(self) -> MDBoxLayout:
        daftarfile = MDBoxLayout(orientation="vertical")
        # ini menu di atas atau colom jika di table
        colomn = MDBoxLayout(orientation="horizontal")
        colomn.add_widget(MDLabel(text="nama file"))
        colomn.add_widget(MDLabel(text="jumlah file"))
        colomn.add_widget(MDLabel(text="delete"))

        scroll = ScrollView()
        for file in get_all_files():
            scroll.add_widget(MDFlatButton(text=file["nameFile"], padding=6))

        daftarfile.add_widget(colomn)
        daftarfile.add_widget(scroll)
        return daftarfile
