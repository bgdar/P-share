from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle

from kivy.clock import Clock

from kivy.core.window import Window


class InfoPopup:
    '''
    Info popup gunakan ketikan ada suatu notifikasi seperti warning ,info , succes atau error
    yang terletak di pojok kanan atas

    @title : Judul popup
    @type : succes,info, warning , error
    @time : berapa lama popup bertahan sebelum di close (misalnya 2=2detik)

    '''

    def __init__(self, title: str, type: str, timer: int):
        self.title = title
        self.type = type
        self.popup = None  # tentukan popup di awal
        self.timer = timer

    def __content(self):
        '''di sini menentukan type popup nya'''

    def Show_popup(self):
        divPopup = BoxLayout(orientation="horizontal", padding=10)
        with divPopup.canvas.before:
            if self.type == 'succes':
                Color(0.0, 0.8, 0.2, 0.5)  # Green
            elif self.type == 'info':
                Color(0.2, 0.6, 0.95, 0.5)  # Light Blue
            elif self.type == 'warning':
                Color(1.0, 0.7, 0.0, 0.5)
            elif self.type == 'error':
                Color(0.9, 0.1, 0.1, 0.5)  # Red
            self.wrappingDiv = Rectangle(pos=divPopup.pos, size=divPopup.size)

            def update_bg(instance, value):
                self.wrappingDiv.pos = instance.pos
                self.wrappingDiv.size = instance.size

        divPopup.bind(pos=update_bg, size=update_bg)

        divPopup.add_widget(
            Label(text=self.title, color=(1, 1, 1, 1), bold=True))

        self.popup = Popup(title="", content=divPopup)

        # pojok kanan atas
        self.popup.size_hint = (None, None)
        self.popup.size = (350, 120)
        self.popup.auto_dismiss = False
        self.popup.pos = (Window.width + self.popup.width,
                          Window.height + self.popup.height)
        self.popup.separator_height = 0
        # self.popup.background = ''
        self.popup.padding = 10
        # self.popup.background=""

        popup_margin = 10

        self.popup.open()

        # setelah beberapa detik di berikan maka popup close
        Clock.schedule_once(lambda dt: self.popup.dismiss(), self.timer)
