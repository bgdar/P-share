from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager
from kivy.graphics import Color, RoundedRectangle
from kivy.uix.button import Button


daftarButton = [
    {"name_screen": "Dashboard", "to": "dashboard"},
    {"name_screen": "Sender", "to": "serder"},
    {"name_screen": "Setting", "to": "setting"}
]


'''buttons yang akan berada di bawah sebagai nav '''


class ButtonNavigation(FloatLayout):
    def __init__(self, screen_manager: ScreenManager, **kwargs):
        super().__init__(**kwargs)
        self.x = 0  # x dan y 0 agar fixed di bawah
        self.y = 0
        self.spacing = 10
        self.padding = 10
        self.size_hint_y = None  # agar tidka berpengaruk ke ukuran windows secra tinggi

        self.screen_manager = screen_manager

        with self.canvas:
            Color(0.12, 0.23, 0.37, 1)  # biru tua sebagai nav background
            bg = RoundedRectangle(
                radius=[10], pos=self.pos, size=self.size)

            def update_bg(instance, value):
                bg.pos = instance.pos
                bg.size = instance.size
            self.bind(pos=update_bg, size=update_bg)

        jumlahTombol = len(daftarButton)
        lebarPerTombol = 1 / jumlahTombol  # jika 1/2 = 0.05
        for index, screen in enumerate(daftarButton):
            screenBotton = Button(text=screen["name_screen"], pos_hint={
                                  "x": index * lebarPerTombol, "y": 0.01}, size_hint=(lebarPerTombol, 1), background_color=(0.22, 0.40, 0.96, 1), color=(1, 1, 1))

            # Membekukan nilai 'name' agar tidak semua tombol mengarah ke yang terakhir
            screenBotton.bind(on_press=lambda x,
                              name=screen["to"]: self.toNavigation(name))
            self.add_widget(screenBotton)

    def toNavigation(self, name_screen: str):
        self.screen_manager.current = name_screen
