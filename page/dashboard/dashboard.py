# gunakan screen untuk menjaga code
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, RoundedRectangle
# from kivy.uix.button import Button
from kivymd.uix.button import MDIconButton
from kivymd.uix.label import MDLabel

from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.scrollview import ScrollView


# COMPONENTS
from components.navigation import ButtonNavigation
from components.assetsManagement import get_resource_path
from components.popup import CustomPopup
from components.infoPopup import InfoPopup


# Components Dashboard
from .menuCreate import Menu


class DashboardScreen(Screen):

    def __init__(self, screen_manager: ScreenManager, **kwargs):
        self.screen_manager = screen_manager
        super().__init__(**kwargs)
        # layout utama untuk screen dasboard
        mainLayot = BoxLayout(orientation="vertical")

        scroll = ScrollView()

        scroll.add_widget(centerItems())

        mainLayot.add_widget(self.menuHeader())
        mainLayot.add_widget(scroll)

        if screen_manager:
            # jika ada buuton navigation rencannaya tambah di bagian paling bwh
            mainLayot.add_widget(ButtonNavigation(
                screen_manager=self.screen_manager))

        # tambahkan semua layout utama di DashboardScreen
        self.add_widget(mainLayot)

    def menuHeader(self):
        divMenu = BoxLayout(orientation="horizontal", padding=20)

        judulMenu = Label(text="menu App", bold=True, color=(1, 0, 0, 1))

        # Tabah latar belakang ke divMenu
        with divMenu.canvas.before:
            # Gunakan rentang 0-1, bukan 0-255
            Color(82/255, 178/255, 245/255, 1)
            self.bg = RoundedRectangle(
                radius=[10], pos=divMenu.pos, size=divMenu.size)

        # Update posisi saat layout berubah ukuran
        def update_bg(instance, value):
            self.bg.pos = divMenu.pos
            self.bg.size = divMenu.size

        # agar jika ada perubahan maka akan di ikuti posisinya
        divMenu.bind(pos=update_bg, size=update_bg)

        divMenu.add_widget(judulMenu)

        return divMenu


class centerItems(GridLayout):
    '''menu menu item di bagin tengah'''

    def __init__(self):
        super().__init__()
        width, height = Window.size
        self.padding = 10
        self.size_hint_y = None
        self.cols = 2
        self.spacing = 10  # jarak antar i:items

        # ⬇️ Otomatis ubah tinggi layout berdasarkan jumlah widget di dalamnya
        self.bind(minimum_height=self.setter('height'))

        width, height = Window.size
        self.update_layout((width, height))

        for items in Menu:
            # panggil setiap card items
            self.add_widget(self.cardItems(
                items["menu"], items["icon"], items["popup"]))

        # manipulasi perubhan layout Windows nya
        self.update_layout(Window.size)
        Window.bind(size=self.on_window_resize)

    def cardItems(self, menu: str, icon: str, popup: CustomPopup) -> BoxLayout:
        '''setiap card items akan mmemiliki div sendiri'''
        divItems = BoxLayout(orientation="vertical",
                             size_hint_y=None, height=100, padding=10)

        with divItems.canvas.before:
            Color(0.9, 0.9, 0.9, 1)  # warna putih
            bg = RoundedRectangle(
                radius=[5], pos=divItems.pos, size=divItems.size)

            # Update posisi & ukuran latar belakang saat layout berubah
        def update_bg(instance, value):
            bg.pos = instance.pos
            bg.size = instance.size

        divItems.bind(pos=update_bg, size=update_bg)

        # gunakan nantik
        # btn.bind(on_press=partial(self.navigate_to, to))#tambah parameter 'to'
        # divItems.add_widget(btn)
        divItems.add_widget(MDLabel(text=menu))
        btn = MDIconButton(icon=icon, text_color=[1, 1, 1, 1], md_bg_color=(
            27/255, 30/255, 35/255, 1), theme_text_color="Custom", pos_hint={"center_x": 0.5, "center_y": 0.5})
        btn.bind(on_press=lambda x: self.__onClickBtnMenu(popup))
        divItems.add_widget(btn)

        return divItems

    def __onClickBtnMenu(self, popup: CustomPopup):
        ''' @popupInfo: cek di file menuCreate.py dari sini di kirimnya'''
        popup.show()

    def on_window_resize(self, instance, size):
        ''''fungsi yang menerima perubahan untuk di gunakan '''
        self.update_layout(size)

    def update_layout(self, size):
        '''gunakan nantik untuk update layout jika ada perubahan  window'''
        width, height = size
        # untuk sekarang layout di pastikan manual
        self.cols = 2 if width >= 600 or height >= 800 else 1
