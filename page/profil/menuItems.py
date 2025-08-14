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
        '''item menu dan setiap item punya containernya sendiri'''
        divItem = BoxLayout(orientation='horizontal',
                            # [left, top, right, bottom] atau 2 value
                            padding=[10, 8],
                            spacing=10,
                            size_hint_y=None,  # Supaya height bisa diatur manual
                            height=50)

        with divItem.canvas.before:
            Color(27/255, 30/255, 35/255, 1)
            self.bgItem = Rectangle()

        divItem.bind(pos=self.update_bgItem, size=self.update_bgItem)

        btnTrigger = MDTextButton(text=item, text_color=[0.9, 0.9, 0.9, 1])
        divItem.add_widget(btnTrigger)

        btnTrigger.bind(
            on_release=lambda instance, i=item: self._handleBtnTrigger(
                instance, i)
        )

        return divItem

    def _handleBtnTrigger(self, instace, item: str):
        print("items dan ", item)
        if item == "setings":
            self.screen_manager.current = "settings"
        elif item == "daftar file":
            self.screen_manager.current = "daftar-file"

    def update_bgItem(self, instance, *args):
        """gunakan jika ada perubahan lebar atau posisi untuk megsejajarkan antara sub dengn pembungusnya"""
        self.bgItem.pos = instance.pos
        self.bgItem.size = instance.size
