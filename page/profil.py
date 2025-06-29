from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout

# Components
from components.navigation import ButtonNavigation


class ProfilScreen(Screen):
    def __init__(self, screen_manager, **kwargs):
        self.screen_manager = screen_manager
        super().__init__(**kwargs)
        mainLayout = BoxLayout(orientation="vertical")

        if self.screen_manager:
            mainLayout.add_widget(ButtonNavigation(
                screen_manager=self.screen_manager))

        self.add_widget(mainLayout)
