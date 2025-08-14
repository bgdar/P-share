# gunakan screen untuk menjaga code
from kivy.uix.gridlayout import GridLayout

from kivymd.uix.progressbar import MDProgressBar
from kivymd.uix.label import MDLabel

from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, RoundedRectangle, Rectangle
# from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.scrollview import ScrollView


# COMPONENTS
from components.navigation import ButtonNavigation
from components.assetsManagement import get_all_files

from .centerItems import centerItems


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

        divMenu.add_widget(self._infoFile())
        judulMenu = Label(text="menu App", bold=True, color=(1, 0, 0, 1))
        # progrres bar di sebelah kanan

        # Tabah latar belakang ke divMenu
        with divMenu.canvas.before:
            # Gunakan rentang 0-1, bukan 0-255
            Color(27/255, 30/255, 35/255, 1)
            self.bg = RoundedRectangle(
                radius=[10], pos=divMenu.pos, size=divMenu.size)

        # agar jika ada perubahan maka akan di ikuti posisinya
        divMenu.bind(pos=self.update_bg, size=self.update_bg)

        divMenu.add_widget(judulMenu)

        return divMenu

    def _infoFile(self) -> BoxLayout:
        ''' mengembalikan text info file saat ini '''
        layout = BoxLayout(orientation="vertical", pos_hint={
                           "center_x": 0.5, "center_y": 0.5})
        lenfile = len(get_all_files())
        # untuk saat ini masih statis

        label: MDLabel = MDLabel(text=str(lenfile), size=(
            50, 50), size_hint=(None, None))
        label.md_bg_color = [1.0, 1.0, 1.0, 1]

        layout.add_widget(label)

        with layout.canvas.before:
            Color(0.08, 0.4, 0.7, 1)
            Rectangle(size=(50, 50))

        return layout

    def update_bg(self, instance, *agrs):
        "update posisi saat layout beruabh ukuran"
        self.bg.pos = instance.pos
        self.bg.size = instance.size
