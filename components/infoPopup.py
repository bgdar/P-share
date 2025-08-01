from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle

from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRectangleFlatButton

from kivy.clock import Clock

from kivy.core.window import Window


class InfoPopup(MDCard):
    '''
    Info popup gunakan ketikan ada suatu notifikasi seperti warning ,info , succes atau error
    yang terletak di pojok kanan atas

    @title : Judul popup
    @type : succes,info, warning , error
    @time : berapa lama popup bertahan sebelum di close (misalnya 2=2detik)

    '''

    def __init__(self, title: str, type: str, timer: float, **kwargs):
        super().__init__(**kwargs)
        # property yang akan di gunakan
        self.title = title
        self.type = type
        self.timer = timer

        # atribut cardPopup
        self.size_hint = (0.3, None)  # width 30% of screen, height auto
        self.height = 100  # fixed ukuran  height
        self.pos_hint = {
            "top": 0.98,  # slightly below top edge
            "right": 0.98  # right edge with small margin
        }
        self.elevation = 24  # Maximum elevation for highest z-index
        self.padding = 10
        self.radius = [10]  # rounded corners

        self.add_widget(self.__content())

    def __content(self) -> BoxLayout:
        '''di sini menentukan type popup nya'''
        content = BoxLayout(orientation="vertical")
        content.add_widget(MDLabel(text=self.title))
        btnClose = MDRectangleFlatButton(text="close")
        content.add_widget(btnClose)

        btnClose.bind(on_release=self._dismiss)

        return content

    def show_popup(self):
        if self.type == 'success':
            self.md_bg_color = [0.2, 0.8, 0.4, 1]
        elif self.type == 'info':
            self.md_bg_color = [0.0, 0.75, 1.0, 1.0]
        elif self.type == 'warning':
            self.md_bg_color = [1.0, 0.65, 0.0, 1]
        elif self.type == 'error':
            self.md_bg_color = [0.2, 0.8, 0.4, 1.0]

            # setelah beberapa detik di berikan maka popup close
        Clock.schedule_once(self._dismiss, self.timer)

    def _dismiss(self, *arg):
        '''untuk menutup alias menghapus semua widget dalam card nya'''
        if self.parent:
            self.parent.remove_widget(self)

    # how to use  :
    # 1. saya siapkan di MainApp
    #  def show_popup(self, title: str, type: str, timer: float = 1.5):
    #     '''akses dengan app =
    #             from kivymd.app import MDApp
    #             MDApp.get_running_app()
    #           app.show_popup("Ini dari Komponen lain!")'''
    #     infoPopup = InfoPopup(title=title, type=type, timer=timer)
    #     infoPopup.show_popup()
    #     # Tambahkan ke screen aktif,
    #     self.screenManager.current_screen.add_widget(infoPopup)
    #
    # 2. sekarang bsai di gunkan di component lain dengan
    #  app = MDApp.get_running_app()
    #
    # atau tambahkan ke dalam widget FloatLayout
    # app.show_popup("click 2 kali untuk melihat", "success", 1.5)

    # Popup lama

# class InfoPopup:
#     '''
#     Info popup gunakan ketikan ada suatu notifikasi seperti warning ,info , succes atau error
#     yang terletak di pojok kanan atas
#
#     @title : Judul popup
#     @type : succes,info, warning , error
#     @time : berapa lama popup bertahan sebelum di close (misalnya 2=2detik)
#
#     '''
#
#     def __init__(self, title: str, type: str, timer: float):
#         self.title = title
#         self.type = type
#         self.popup = None  # tentukan popup di awal
#         self.timer = timer
#
#     def __content(self):
#         '''di sini menentukan type popup nya'''
#
#     def Show_popup(self):
#         divPopup = BoxLayout(orientation="horizontal", padding=10)
#         with divPopup.canvas.before:
#             if self.type == 'succes':
#                 Color(0.0, 0.8, 0.2, 0.5)  # Green
#             elif self.type == 'info':
#                 Color(0.2, 0.6, 0.95, 0.5)  # Light Blue
#             elif self.type == 'warning':
#                 Color(1.0, 0.7, 0.0, 0.5)
#             elif self.type == 'error':
#                 Color(0.9, 0.1, 0.1, 0.5)  # Red
#             self.wrappingDiv = Rectangle(pos=divPopup.pos, size=divPopup.size)
#
#             def update_bg(instance, value):
#                 self.wrappingDiv.pos = instance.pos
#                 self.wrappingDiv.size = instance.size
#
#         divPopup.bind(pos=update_bg, size=update_bg)
#
#         divPopup.add_widget(
#             Label(text=self.title, color=(1, 1, 1, 1), bold=True))
#
#         self.popup = Popup(title="", content=divPopup)
#
#         # pojok kanan atas
#         self.popup.size_hint = (None, None)
#         self.popup.size = (350, 120)
#         self.popup.auto_dismiss = False
#         self.popup.pos = (Window.width + self.popup.width,
#                           Window.height + self.popup.height)
#         self.popup.separator_height = 0
#         # self.popup.background = ''
#         self.popup.padding = 10
#         # self.popup.background=""
#
#         popup_margin = 10
#
#         self.popup.open()
#
#         # setelah beberapa detik di berikan maka popup close
#         Clock.schedule_once(lambda dt: self.popup.dismiss(), self.timer)
