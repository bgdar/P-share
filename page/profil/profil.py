from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.scrollview import ScrollView
from .menuItems import MenuItem
from .ProfilHeader import ProfilHeader

# Components
from components.navigation import ButtonNavigation


class ProfilScreen(Screen):
    def __init__(self, screen_manager, **kwargs):
        self.screen_manager = screen_manager
        super().__init__(**kwargs)
        mainLayout = BoxLayout(orientation="vertical")
        # menu foto profil yg di atas , ini bisa di jadikan latar belakang
        # self.add_widget(ProfilHeader())
        mainLayout.add_widget(ProfilHeader())

        itemsScrolll = ScrollView()
        itemsScrolll.add_widget(MenuItem(self.screen_manager))
        mainLayout.add_widget(itemsScrolll)

        # button navigasi di paling bawah
        if self.screen_manager:
            mainLayout.add_widget(ButtonNavigation(
                screen_manager=self.screen_manager))

        self.add_widget(mainLayout)
