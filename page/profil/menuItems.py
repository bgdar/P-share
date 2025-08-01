from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager

from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDTextButton

from kivy.graphics import Color, Rectangle

from database.session import session

# nantik gunakan ini ke tombol logout untuk menghapus chace dari session agar bisa di arahkan ke halaman login
# session.drop_data_sesio


items: list[str] = ["setings", "daftar file", "logout"]


class MenuItem(BoxLayout):
    '''menu menu di bawah'''

    def __init__(self, screen_manager: ScreenManager):
        super().__init__()
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 15

        self.screen_manager = screen_manager

        for item in items:
            item_widget = self.item(item=item)
            self.add_widget(item_widget)

    def item(self, item: str) -> BoxLayout:
        '''setiap item punya containernya sendiri'''
        divItem = BoxLayout(orientation='horizontal', padding=5)
        with divItem.canvas.before:
            Color(27/255, 30/255, 35/255, 1)
            bgItem = Rectangle()

        def update_bgItem(instance, *args):
            bgItem.pos = instance.pos
            bgItem.size = instance.size

        divItem.bind(pos=update_bgItem, size=update_bgItem)

        btnTrigger = MDTextButton(text=item)
        divItem.add_widget(btnTrigger)

        btnTrigger.bind(
            on_release=lambda instace: self._handleBtnTrigger(instace, item))

        return divItem

    def _handleBtnTrigger(self, instace, item: str):
        print("items dan ", item)
        if item == "setings":
            self.screen_manager.current = "settings"
        elif item == "daftar file":
            self.screen_manager.current = "daftar-file"
