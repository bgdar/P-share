# gunakan screen untuk menjaga code
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, RoundedRectangle
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView

# Network
from Network.server import Server, get_ip_address

# COMPONENTS
from components.navigation import ButtonNavigation
from components.popup import CustomPopup


class DashboardScreen(Screen):

   # server = Server()
    def __init__(self, screen_manager: None, **kwargs):
        self.screen_manager = screen_manager
        super().__init__(**kwargs)
        # layout utama untuk screen dasboard
        mainLayot = BoxLayout(orientation="vertical")

        scroll = ScrollView()

        scroll.add_widget(centerItems())

        mainLayot.add_widget(self.menu())
        mainLayot.add_widget(scroll)

        if screen_manager:
            # jika ada buuton navigation rencannaya tambah di bagian paling bwh
            mainLayot.add_widget(ButtonNavigation(
                screen_manager=self.screen_manager))

        # tambahkan semua layout utama di DashboardScreen
        self.add_widget(mainLayot)

    def menu(self):
        divMenu = BoxLayout(orientation="horizontal", padding=20)

        judulMenu = Label(text="menu App", bold=True, color=(1, 0, 0, 1))

        # Tambah latar belakang ke divMenu
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
      #  divMenu.add_widget(create_check_ip_content())
        return divMenu


class centerItems(GridLayout):
    def __init__(self):
        super().__init__()
        width, height = Window.size
        self.padding = 10
        self.size_hint_y = None
        self.cols = 2
        self.spacing = 10  # jarak antar i:items

        # ⬇️ DITAMBAHKAN: Otomatis ubah tinggi layout berdasarkan jumlah widget di dalamnya
        self.bind(minimum_height=self.setter('height'))

        width, height = Window.size
        # ⬅️ Ubah: Gunakan update_layout untuk set awal cols
        self.update_layout((width, height))

        for items in menu:
            self.add_widget(self.cardItems(items["menu"], items["popup"]))

        self.update_layout(Window.size)

        Window.bind(size=self.on_window_resize)

    def cardItems(self, menu: str, popup: CustomPopup):
        '''setiap card items akan mmemiliki div sendiri'''
        divItems = BoxLayout(size_hint_y=None, height=100, padding=10)

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
        btn = Button(text=menu)
        btn.bind(on_press=lambda x: popup.show())
        divItems.add_widget(btn)
        return divItems

    def on_window_resize(self, instance, size):
        self.update_layout(size)

    def update_layout(self, size):
        width, height = size
        # untuk sekarang layout di pastikan manual
        self.cols = 2 if width >= 600 or height >= 800 else 1


# Factory functions supaya membuat content baru setiap kali popup ditampilkan
def create_menu1_content():
    content = BoxLayout(orientation='horizontal')
    content.add_widget(Label(text="Menu 1 content"))
    return content


def create_check_ip_content():
    content = BoxLayout(orientation='horizontal')
    content.add_widget(Label(text=get_ip_address()))
    return content


def create_menu3_content():
    content = BoxLayout(orientation='horizontal')
    content.add_widget(Label(text="Menu 3 content"))
    return content


def create_menu4_content():
    content = BoxLayout(orientation='horizontal')
    content.add_widget(Label(text="Menu 4 content"))
    return content


# Buat popup terpisah untuk setiap menu
menu1Popup = CustomPopup(posisi_popup=(
    100, 100), title="Menu 1", size_popup=(200, 300))
menu1Popup.set_content(create_menu1_content)

cekIpPopup = CustomPopup(posisi_popup=(
    100, 100), title="Your IP", size_popup=(200, 300))
cekIpPopup.set_content(create_check_ip_content)

menu3Popup = CustomPopup(posisi_popup=(
    100, 100), title="Menu 3", size_popup=(200, 300))
menu3Popup.set_content(create_menu3_content)

menu4Popup = CustomPopup(posisi_popup=(
    100, 100), title="Menu 4", size_popup=(200, 300))
menu4Popup.set_content(create_menu4_content)

menu = [
    # gunakan untuk mendapakan ip yg bisa di gunakan
    {"menu": "menu1", "to": "", "popup": menu1Popup},
    {"menu": "cek ip", "to": "", "popup": cekIpPopup},
    {"menu": "menu3", "to": "", "popup": menu3Popup},
    {"menu": "menu4", "to": "", "popup": menu4Popup},
]
