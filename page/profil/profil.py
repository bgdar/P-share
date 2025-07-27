from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout

from .menuItems import MenuItem
from .ProfilHeader import ProfilHeader

# Components
from components.navigation import ButtonNavigation


class ProfilScreen(Screen):
    def __init__(self, screen_manager, **kwargs):
        self.screen_manager = screen_manager
        super().__init__(**kwargs)
        mainLayout = BoxLayout(orientation="vertical")
        # menu foto profil yg di atas
        self.add_widget(ProfilHeader())
        # menu item yg di tengah sampai bawah
        mainLayout.add_widget(MenuItem())

        # button navigasi di paling bawah
        if self.screen_manager:
            mainLayout.add_widget(ButtonNavigation(
                screen_manager=self.screen_manager))

        self.add_widget(mainLayout)
