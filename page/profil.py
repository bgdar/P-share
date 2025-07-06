from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

from kivy.graphics import Color, Rectangle, Ellipse


# Components
from components.navigation import ButtonNavigation


class ProfilScreen(Screen):
    def __init__(self, screen_manager, **kwargs):
        self.screen_manager = screen_manager
        super().__init__(**kwargs)
        mainLayout = BoxLayout(orientation="vertical")

        # menu foto profil yg di atas
        mainLayout.add_widget(self.profilCard())
        # menu item yg di tengah sampai bawah
        mainLayout.add_widget(MenuItem())

        if self.screen_manager:
            mainLayout.add_widget(ButtonNavigation(
                screen_manager=self.screen_manager))

        self.add_widget(mainLayout)

    def profilCard(self):
        '''card yg paling atas'''
        divProfilCard = BoxLayout(orientation='horizontal', padding=10)
        divProfilCard.add_widget(self.fotoProfilCard())

        divProfilCard.add_widget(Label(text="profil"))

        return divProfilCard

    def fotoProfilCard(self):
        ''' ini lingkaranya yg menampung foto profil'''
        self.divFotoProfilCard = BoxLayout(orientation='horizontal')
        with self.divFotoProfilCard.canvas.before:
            Color(0.8, 0.8, 0.8, 1)  # Warna abu-abu terang
            self.ellipse = Ellipse(pos=(100, 100), size=(150, 150))

        self.divFotoProfilCard.bind(
            pos=self.update_bgCicler, size=self.update_bgCicler)
        return self.divFotoProfilCard

    def update_bgCicler(self, *args):
        self.ellipse.pos = self.divFotoProfilCard.pos
        self.ellipse.size = self.divFotoProfilCard.size


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
        divItem = BoxLayout(orientation='horizontal', padding=10)
        with divItem.canvas.before:
            Color(82/255, 178/255, 245/255, 1)
            bgItem = Rectangle()

        def update_bgItem(instance, *args):
            bgItem.pos = instance.pos
            bgItem.size = instance.size

        divItem.bind(pos=update_bgItem, size=update_bgItem)

        divItem.add_widget(Label(text=item))
        return divItem
