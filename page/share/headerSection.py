from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Ellipse, RoundedRectangle, Color

from kivy.properties import StringProperty

from kivymd.uix.label import MDLabel

from kivymd.uix.button import MDRaisedButton
from kivy.core.window import Window
from kivy.uix.widget import Widget

from kivy.clock import Clock

from components.Globalstate import Store
from components.assetsManagement import get_all_files, get_resource_path
from typing import Tuple


class HeaderSection(BoxLayout):
    # observable property  : ynag bisa di bind ke UI
    # lenSelectPathFile = StringProperty()

    def __init__(self):
        super().__init__()
        self.padding = 10
        self.orientation = "vertical"
        self.size_hint_y = 0.2
        self.windowWidth, self.windowHeight = Window.size

        # self.lenSelectPathFile = str(len(Store.pathFileNames))

        self.add_widget(self.__headerContent())

    def __headerContent(self) -> BoxLayout:
        divHeader = BoxLayout(orientation="horizontal", height=15)
        with divHeader.canvas.before:
            Color(0.1, 0.82, 0.5, 0.5)
            divHeaderBg = RoundedRectangle(
                radius=[10], pos=divHeader.pos, size=divHeader.size
            )

        # update jika ada perubahan bacground
        divHeader.bind(
            size=lambda instance, value: self.update_bg_size(divHeaderBg, value),
            pos=lambda instance, value: self.update_bg_pos(divHeaderBg, value),
        )

        divHeader.add_widget(MDLabel(text="Header "))

        return divHeader

    def update_bg_size(self, rect: Widget, size: Widget.size):
        """Gunakan utnuk mengupdate bacground size element"""
        rect.size = size

    def update_bg_pos(self, rect: Widget, pos: Widget.pos):
        """Gunakan utnuk mengupdate bacground untuk pos element"""
        rect.pos = pos
