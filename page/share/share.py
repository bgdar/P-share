from kivy.uix.screenmanager import Screen
from components.navigation import ButtonNavigation
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.carousel import Carousel
import os
from components.assetsManagement import get_resource_path

from .serverSection import ServerSection
from .clientSection import ClientSection
from .headerSection import HeaderSection


# ini halaman di mana pengirim file akan mengirimkan ke server alias penerima-nya
class ShareScreen(Screen):
    def __init__(self, screen_manager: None, **kwargs):
        super().__init__(**kwargs)
        self.screen_manager = screen_manager

        mainLayout = BoxLayout(orientation="vertical")
        # mainLayout.add_widget(Label(text="page serder"))

        # header di paling atas untuk menangani management file
        mainLayout.add_widget(HeaderSection())
        # menu pada bagian tengah yang menagani file di kirim
        # gunakan teknik slide nantik untuk memilih sebegai pegirim atau penerima
        mainLayout.add_widget(self._ServerClientSlider())

        if screen_manager:
            mainLayout.add_widget(ButtonNavigation(
                screen_manager=self.screen_manager))

        self.add_widget(mainLayout)

    def _ServerClientSlider(self):
        self.carousel = Carousel(direction='right', loop=True)

        divSlider = BoxLayout(orientation="vertical")

        self.carousel.add_widget(ClientSection())
        self.carousel.add_widget(ServerSection())

        # untuk menampung navnya
        btnNav = BoxLayout(size_hint_y=0.1)

        btn_prev = Button(text="<", font_size=24)
        btn_next = Button(text=">", font_size=24)

        btnNav.add_widget(btn_prev)
        btnNav.add_widget(btn_next)

        btn_prev.bind(on_press=self.prev_slide)
        btn_next.bind(on_press=self.next_slide)

        # gabungkan hingga menjadi slide show
        divSlider.add_widget(self.carousel)
        divSlider.add_widget(btnNav)

        return divSlider

    def next_slide(self, instance):
        self.carousel.load_next(mode='next')

    def prev_slide(self, instance):
        self.carousel.load_previous()
