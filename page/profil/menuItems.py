from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle

from database.session import session


# nantik gunakan ini ke tombol logout untuk menghapus chace dari session agar bisa di arahkan ke halaman login
# session.drop_data_sesion()


items = {
    "menu1": "daftar file",
    "menu2": "logout",
}


class MenuItem(BoxLayout):
    '''menu menu di bawah'''

    def __init__(self):
        super().__init__()
        self.orientation = 'vertical'
        self.padding = 10

        for item in items.values():
            item_widget = self.item(item=item)
            self.add_widget(item_widget)

    def item(self, item: str):
        '''setiap item punya containernya sendiri'''
        divItem = BoxLayout(orientation='horizontal', padding=5)
        with divItem.canvas.before:
            Color(82/255, 178/255, 245/255, 1)
            bgItem = Rectangle()

        def update_bgItem(instance, *args):
            bgItem.pos = instance.pos
            bgItem.size = instance.size

        divItem.bind(pos=update_bgItem, size=update_bgItem)

        divItem.add_widget(Label(text=item))
        return divItem
