from kivy.uix.screenmanager import Screen
from components.navigation import ButtonNavigation
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

# ini halaman di mana pengirim file akan mengirimkan ke server alias penerima-nya


class SerderScreen(Screen):
    def __init__(self, screen_manager: None, **kwargs):
        super().__init__(**kwargs)
        self.screen_manager = screen_manager

        mainLayout = BoxLayout(orientation="vertical")
        mainLayout.add_widget(Label(text="page serder"))

        if screen_manager:
            mainLayout.add_widget(ButtonNavigation(
                screen_manager=self.screen_manager))

        self.add_widget(mainLayout)


class CenterSection():
    '''bagian tengan yang terdapat tombol bulat untuk mengirikkan file'''
